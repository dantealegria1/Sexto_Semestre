set nocompatible
filetype off

set rtp+=~/.vim/bundle/Vundle.vim
call vundle#begin()

Plugin 'VundleVim/Vundle.vim'
Plugin 'scrooloose/nerdtree'
Plugin 'airblade/vim-gitgutter'
Plugin 'morhetz/gruvbox'

call vundle#end()
filetype plugin indent on
filetype plugin on

set number
set autoindent
set expandtab
set encoding=utf-8
