if exists('g:loaded_completor_neosnippet_plugin')
  finish
endif

let g:loaded_completor_neosnippet_plugin = 1
let s:py = has('python3') ? 'py3' : 'py'


function! s:err(msg)
  echohl Error
  echo a:msg
  echohl NONE
endfunction


function! s:import_python()
  try
    exe s:py 'import completor_neosnippet'
  catch /^Vim(python):/
    call s:err('Fail to import completor_neosnippet')
    return
  endtry

  try
    exe s:py 'import completor, completers.common'
  catch /^Vim(python):/
    call s:err('Fail to import completor')
    return
  endtry

  try
    exe s:py 'completor.get("common").hooks.append(completor_neosnippet.Neosnippet.filetype)'
  catch /^Vim(python):/
    call s:err('Fail to add neosnippet hook')
  endtry
endfunction


function! s:enable()
  call s:import_python()
  call s:disable()
endfunction


function! s:disable()
  augroup completor_neosnippet
    autocmd!
  augroup END
endfunction


augroup completor_neosnippet
  autocmd!
  autocmd InsertEnter * call s:enable()
augroup END
