if exists('g:loaded_completor_neosnippet_plugin')
  finish
endif

let g:loaded_completor_neosnippet_plugin = 1
let s:py = has('python3') ? 'py3' : 'py'


function! s:enable()
  exe s:py 'import completor_neosnippet'
  exe s:py 'import completor, completers.common'
  exe s:py 'completor.get("common").hooks.append(completor_neosnippet.Neosnippet.filetype)'
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
