%global tl_name texfot
%global tl_revision 77286

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.54
Release:	%{tl_revision}.1
Summary:	Filter clutter from the output of a TeX run
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/support/texfot
License:	pd
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/texfot.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/texfot.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Requires:	texlive(texfot.bin)
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package provides a small Perl script to filter the online output
from a TeX run, attempting to show only those messages which probably
deserve some change in the source. The TeX invocation itself need not
change.

