%global tl_name sansmathaccent
%global tl_revision 77682

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	Correct placement of accents in sans-serif maths
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/fonts/sansmathaccent
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/sansmathaccent.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/sansmathaccent.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Sans serif maths (produced by the beamer class or the sfmath package)
often has accents positioned incorrectly. This package fixes the
positioning of such accents when the default font (cmssi) is used for
sans serif maths. It will have no effect if used in a document that does
not use the beamer class or the sfmath package.

