#!/bin/bash

# Basic Setup
sudo dnf autoremove libreoffice-writer libreoffice-calc libreoffice-impress

sudo rpm --import https://gitlab.com/paulcarroty/vscodium-deb-rpm-repo/-/raw/master/pub.gpg
printf "[gitlab.com_paulcarroty_vscodium_repo]\nname=gitlab.com_paulcarroty_vscodium_repo\nbaseurl=https://paulcarroty.gitlab.io/vscodium-deb-rpm-repo/rpms/\nenabled=1\ngpgcheck=1\nrepo_gpgcheck=1\ngpgkey=https://gitlab.com/paulcarroty/vscodium-deb-rpm-repo/-/raw/master/pub.gpg" |sudo tee -a /etc/yum.repos.d/vscodium.repo

sudo dnf install git gcc libgcc binutils-gold glibc-devel codium

# Rust Setup
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh

PATH=$PATH:~/.cargo/bin && echo 'PATH=$PATH:~/.cargo/bin' >> ~/.bash_profile 
