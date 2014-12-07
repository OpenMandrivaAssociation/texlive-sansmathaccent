# revision 30187
# category Package
# catalog-ctan /fonts/sansmathaccent
# catalog-date 2013-04-30 15:48:45 +0200
# catalog-license lppl1.3
# catalog-version undef
Name:		texlive-sansmathaccent
Version:	20130430
Release:	8
Summary:	Correct placement of accents in sans-serif maths
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/fonts/sansmathaccent
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/sansmathaccent.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/sansmathaccent.doc.tar.xz
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
%{_texmfdistdir}/fonts/map/dvips/sansmathaccent/sansmathaccent.map
%{_texmfdistdir}/fonts/tfm/public/sansmathaccent/mathkerncmssi10.tfm
%{_texmfdistdir}/fonts/tfm/public/sansmathaccent/mathkerncmssi12.tfm
%{_texmfdistdir}/fonts/tfm/public/sansmathaccent/mathkerncmssi17.tfm
%{_texmfdistdir}/fonts/tfm/public/sansmathaccent/mathkerncmssi8.tfm
%{_texmfdistdir}/fonts/tfm/public/sansmathaccent/mathkerncmssi9.tfm
%{_texmfdistdir}/fonts/tfm/public/sansmathaccent/mathkerncmssxi10.tfm
%{_texmfdistdir}/fonts/tfm/public/sansmathaccent/mathkerncmssxi12.tfm
%{_texmfdistdir}/fonts/tfm/public/sansmathaccent/mathkerncmssxi17.tfm
%{_texmfdistdir}/fonts/tfm/public/sansmathaccent/mathkerncmssxi8.tfm
%{_texmfdistdir}/fonts/tfm/public/sansmathaccent/mathkerncmssxi9.tfm
%{_texmfdistdir}/fonts/vf/public/sansmathaccent/mathkerncmssxi10.vf
%{_texmfdistdir}/fonts/vf/public/sansmathaccent/mathkerncmssxi12.vf
%{_texmfdistdir}/fonts/vf/public/sansmathaccent/mathkerncmssxi17.vf
%{_texmfdistdir}/fonts/vf/public/sansmathaccent/mathkerncmssxi8.vf
%{_texmfdistdir}/fonts/vf/public/sansmathaccent/mathkerncmssxi9.vf
%{_texmfdistdir}/tex/latex/sansmathaccent/ot1mathkerncmss.fd
%{_texmfdistdir}/tex/latex/sansmathaccent/sansmathaccent.sty
%doc %{_texmfdistdir}/doc/fonts/sansmathaccent/README
%doc %{_texmfdistdir}/doc/fonts/sansmathaccent/sansmathaccent.pdf
%doc %{_texmfdistdir}/doc/fonts/sansmathaccent/sansmathaccent.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts tex doc %{buildroot}%{_texmfdistdir}
