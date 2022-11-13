Name:		texlive-texfot
Version:	64507
Release:	1
Summary:	Filter clutter from the output of a TeX run
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/support/texfot
License:	PD
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/texfot.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/texfot.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea
Provides:	texlive-texfot.bin = %{EVRD}

%description
The package provides a small Perl script to filter the online
output from a TeX run, attempting to show only those messages
which probably deserve some change in the source. The TeX
invocation itself need not change.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_bindir}/texfot
%{_texmfdistdir}/scripts/texfot/texfot.pl
%doc %{_mandir}/man1/texfot.1*
%doc %{_texmfdistdir}/doc/man/man1/texfot.man1.pdf
%doc %{_texmfdistdir}/doc/support/texfot/README

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_bindir}
pushd %{buildroot}%{_bindir}
ln -sf %{_texmfdistdir}/scripts/texfot/texfot.pl texfot
popd
mkdir -p %{buildroot}%{_datadir}
cp -fpar texmf-dist %{buildroot}%{_datadir}
mkdir -p %{buildroot}%{_mandir}/man1
mv %{buildroot}%{_texmfdistdir}/doc/man/man1/*.1 %{buildroot}%{_mandir}/man1
