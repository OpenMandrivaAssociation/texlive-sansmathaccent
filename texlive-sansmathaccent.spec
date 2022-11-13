Name:		texlive-sansmathaccent
Version:	53628
Release:	1
Summary:	Correct placement of accents in sans-serif maths
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/fonts/sansmathaccent
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/sansmathaccent.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/sansmathaccent.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Sans serif maths (produced by the beamer class or the sfmath
package) often has accents positioned incorrectly. The package
fixes the positioning of such accents when the default font
(cmssi) is used for sans serif maths.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/fonts/map/dvips/sansmathaccent
%{_texmfdistdir}/fonts/tfm/public/sansmathaccent
%{_texmfdistdir}/fonts/vf/public/sansmathaccent
%{_texmfdistdir}/tex/latex/sansmathaccent
%doc %{_texmfdistdir}/doc/fonts/sansmathaccent

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts tex doc %{buildroot}%{_texmfdistdir}
