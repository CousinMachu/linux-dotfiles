set nocompatible              " be iMproved, required
filetype off                  " required

set smartcase

" Vim-Plug
call plug#begin('~/.vim/plugged')
Plug 'lervag/vimtex'
" Plug 'jiangmiao/auto-pairs'
" Plug 'jlanzarotta/bufexplorer'
" Plug 'kien/ctrlp.vim'
" Plug 'scrooloose/nerdtree'
" Plug 'xolox/vim-misc'
" Plug 'xolox/vim-notes'
" if has('nvim')
"   Plug 'Shougo/deoplete.nvim', { 'do': ':UpdateRemotePlugins' }
" else
"   Plug 'Shougo/deoplete.nvim'
"   Plug 'roxma/nvim-yarp'
"   Plug 'roxma/vim-hug-neovim-rpc'
" endif
" Plug 'deoplete-plugins/deoplete-jedi'
" Plug 'Shougo/deoplete-clangx'
" Plug 'wokalski/autocomplete-flow'
" Plug 'prabirshrestha/async.vim'
" Plug 'prabirshrestha/vim-lsp'
" Plug 'Shougo/neco-syntax'
Plug 'vim-airline/vim-airline'
Plug 'vim-airline/vim-airline-themes'
Plug 'w0rp/ale'
call plug#end()

" ALE
let g:ale_set_highlights = 0

" Airline/status bar
let g:airline_powerline_fonts=1
let g:airline#extensions#tabline#enabled=1
let g:airline_theme="bubblegum"
let g:notes_directories = ['~/cloud/Documents/USC/notes']

" deoplete
let g:deoplete#enable_at_startup = 1

" vimtex
let g:vimtex_enabled = 1
let g:vimtex_compiler_method = "latexmk"
let g:tex_flavor = 'latex'
let maplocalleader = ","
let g:vimtex_quickfix_autoclose_after_keystrokes = 2

syntax on
filetype plugin indent on
source ~/.colemak.vim
