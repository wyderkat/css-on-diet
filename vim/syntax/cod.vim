" Vim syntax file
" Language:	CSS 3
" Based On: css.vim (from Vim 7.3)
" Original Author: Claudio Fleiner <claudio@fleiner.com>
" Maintainer: fremff <sorathone@gmail.com>
" Last Change: 2013-05-08
" Version: 1.3.0


" For version 5.x: Clear all syntax items
" For version 6.x: Quit when a syntax file was already loaded
if !exists("main_syntax")
  if version < 600
    syntax clear
  elseif exists("b:current_syntax")
    finish
  endif
  let main_syntax = 'css'
endif

syn case ignore

" Selectors

"  HTML tags
syn keyword cssTagName a abbr acronym address applet area b base
syn keyword cssTagName basefont bdo big blockquote body br button
syn keyword cssTagName caption center cite code col colgroup dd del
syn keyword cssTagName dfn dir div dl dt em fieldset font form frame
syn keyword cssTagName frameset h1 h2 h3 h4 h5 h6 head hr html i
syn keyword cssTagName iframe img input ins isindex kbd label legend li
syn keyword cssTagName link map meta noframes noscript object ol optgroup
syn keyword cssTagName option p param pre q s samp script select small
syn keyword cssTagName span strike strong style sub sup tbody td
syn keyword cssTagName textarea tfoot th thead title tr tt u ul var
syn match   cssTagName "\<table\>"
syn match   cssTagName "\*"

"  HTML 5 tags
syn keyword cssTagName article aside audio bdi canvas command date
syn keyword cssTagName datalist details dialog embed eventsource
syn keyword cssTagName figcaption figure footer header hgroup keygen
syn keyword cssTagName main mark menu meter nav output progress rp rt ruby
syn keyword cssTagName section source summary time track video wbr

syn match   cssSelectorOp "[+>.]"
"  Included the css3 Attribute selectors: '^=, $=, *='
syn match   cssSelectorOp2 "[~|^$*]\?=" contained
syn region  cssAttributeSelector matchgroup=cssSelectorOp start="\[" end="]" transparent contains=cssUnicodeEscape,cssSelectorOp2,cssStringQ,cssStringQQ

try
syn match   cssIdentifier "#[A-Za-zÀ-ÿ_@][A-Za-zÀ-ÿ0-9_@-]*"
catch /^.*/
syn match   cssIdentifier "#[A-Za-z_@][A-Za-z0-9_@-]*"
endtry

" Values

"  Included the length and resolution and angle units: 'ch, rem, vw, vh, vmin, vmax,
"  dpi, dpcm, dppx, turn'
syn match   cssValueNumber contained "[-+]\=\d\+\%(\.\d\+\)\=\|\.\d\+" display
syn match   cssValuePercentage contained "\%(\d\+\%(\.\d\+\)\=\|\.\d\+\)%" display
syn match   cssValueLength contained "\%([-+]\=\d\+\%(\.\d\+\)\=\|\.\d\+\)\(mm\|ch\|cm\|in\|pt\|pc\|r\=em\|ex\|px\|vh\|vw\|vmin\|vmax\)\>" display
syn match   cssValueAngle contained "\%([-+]\=\d\+\%(\.\d\+\)\=\|\.\d\+\)\(deg\|g\=rad\|turn\)\>" display
syn match   cssValueTime contained "\%([-+]\=\d\+\%(\.\d\+\)\=\|\.\d\+\)\(ms\|s\)\>" display
syn match   cssValueFrequency contained "\%([-+]\=\d\+\%(\.\d\+\)\=\|\.\d\+\)\(Hz\|kHz\)\>" display
syn match   cssValueResolution contained "\%(\d\+\%(\.\d\+\)\=\|\.\d\+\)\(dpi\|dpcm\|dppx\)\>" display

" Colors

"  Standard color names
syn keyword cssColor contained aqua black blue fuchsia gray green lime maroon navy olive orange purple red silver teal white yellow
"  Extended color keywords (That also referred as the X11 colors, the SVG colors)
syn keyword cssColor contained aliceblue antiquewhite aquamarine azure beige bisque blanchedalmond blueviolet brown burlywood
syn keyword cssColor contained cadetblue chartreuse chocolate coral cornflowerblue cornsilk crimson cyan
syn keyword cssColor contained darkblue darkcyan darkgoldenrod darkgray darkgreen darkgrey darkkhaki darkmagenta darkolivegreen darkorange darkorchid darkred darksalmon darkseagreen darkslateblue darkslategray darkslategrey darkturquoise darkviolet deeppink deepskyblue dimgray dimgrey dodgerblue
syn keyword cssColor contained firebrick floralwhite forestgreen gainsboro ghostwhite gold goldenrod greenyellow grey honeydew hotpink indianred indigo ivory khaki
syn keyword cssColor contained lavender lavenderblush lawngreen lemonchiffon lightblue lightcoral lightcyan lightgoldenrodyellow lightgray lightgreen lightgrey lightpink lightsalmon lightseagreen lightskyblue lightslategray lightslategrey lightsteelblue lightyellow limegreen linen
syn keyword cssColor contained magenta mediumaquamarine mediumblue mediumorchid mediumpurple mediumseagreen mediumslateblue mediumspringgreen mediumturquoise mediumvioletred midnightblue mintcream mistyrose moccasin
syn keyword cssColor contained navajowhite oldlace olivedrab orangered orchid palegoldenrod palegreen paleturquoise palevioletred papayawhip peachpuff peru pink plum powderblue
syn keyword cssColor contained rosybrown royalblue saddlebrown salmon sandybrown seagreen seashell sienna skyblue slateblue slategray slategrey snow springgreen steelblue tan thistle tomato turquoise violet wheat whitesmoke yellowgreen

syn case match
syn match   cssColor contained "\<currentColor\>" display
syn case ignore
syn match   cssColor contained "\<transparent\>" display
syn match   cssColor contained "#[0-9A-Fa-f]\{3\}\>" display
syn match   cssColor contained "#[0-9A-Fa-f]\{6\}\>" display

" Functions

syn region  cssURL contained matchgroup=cssFunctionName start="\<url\s*(" end=")" oneline keepend display
syn region  cssFunction contained matchgroup=cssFunctionName start="\<\(counter\|rect\)\s*(" end=")" oneline keepend display
syn region  cssFunction contained matchgroup=cssFunctionName start="\<\(attr\|counters\)\s*(" end=")" oneline keepend display
"  Included 'rgba(), hsl(), hsla()' functional notation
syn region  cssColor contained matchgroup=cssFunctionName start="\<\(rgba\=\|hsla\=\)\s*(" end=")" oneline keepend display
"  Gradients
syn region  cssFunction transparent contained matchgroup=cssFunctionName start="\(-\(webkit\|o\)-\|\(-\(moz\)-\)\@<!\)\(repeating-\)\=\(linear\|radial\)-gradient\s*(" end=")" oneline display
"  Mozilla Extension of the CSS background-image
syn region  cssFunction transparent contained matchgroup=cssFunctionName start="\<-moz-image-rect\s*(" end=")" oneline display
"  'calc()' function
syn region  cssFunction transparent contained matchgroup=cssFunctionName start="\(-\(webkit\)-\|\(-\(moz\)-\)\@<!\)calc\s*(" end=")" contains=cssFunction,cssCalcExpressions,cssValue.* oneline display
syn match   cssCalcExpressions contained "\%(+\|-\|\*\|\/\)" display


syn match   cssImportant contained "!\s*important\>" display

" Properties and Property values

syn keyword cssCommonAttr contained auto none inherit
syn match   cssCommonAttr contained "\<\(top\|bottom\|left\|right\)\>\(:\)\@!" display
syn keyword cssCommonAttr contained medium normal

syn match   cssFontProp contained "\<font\%(-\%(family\|style\|variant\|weight\|size\%(-adjust\)\=\|stretch\)\)\=\>\(\s*:\)\@=" display
syn match   cssFontAttr contained "\<\%(sans-\)\=serif\>" display
syn match   cssFontAttr contained "\<small\%(-\%(caps\|caption\)\)\=\>" display
syn match   cssFontAttr contained "\<x\{1,2\}-\%(large\|small\)\>" display
syn match   cssFontAttr contained "\<message-box\>" display
syn match   cssFontAttr contained "\<status-bar\>" display
syn match   cssFontAttr contained "\<\%(\%(ultra\|extra\|semi\)-\)\=\(condensed\|expanded\)\>" display
syn keyword cssFontAttr contained cursive fantasy monospace italic oblique
syn keyword cssFontAttr contained bold bolder lighter larger smaller
syn keyword cssFontAttr contained icon menu
syn match   cssFontAttr contained "\<caption\>" display
syn keyword cssFontAttr contained large
syn keyword cssFontAttr contained narrower wider

syn match   cssColorProp contained "\<color\>\(\s*:\)\@=" display
syn keyword cssColorAttr contained center scroll fixed
syn match   cssColorAttr contained "\<repeat\%(-[xy]\)\=\>" display
syn match   cssColorAttr contained "\<no-repeat\>" display

syn match   cssTextProp "\<\(\%(word\|letter\)-spacing\|text\%(-\%(decoration\|transform\|align\|index\|shadow\|rendering\)\)\=\|vertical-align\|unicode-bidi\|line-height\)\>\(\s*:\)\@=" display
syn match   cssTextAttr contained "\<line-through\>" display
syn keyword cssTextAttr contained underline overline blink sub super middle
syn keyword cssTextAttr contained capitalize uppercase lowercase full-width
syn keyword cssTextAttr contained center justify baseline text-top text-bottom

syn match   cssBoxProp contained "\<\(margin\|padding\|border\)\%(-\%(top\|right\|bottom\|left\)\)\=\>\(\s*:\)\@=" display
syn match   cssBoxProp contained "\<border-\%(\%(\%(top\|right\|bottom\|left\)-\)\=\%(width\|color\|style\)\)\=\>\(\s*:\)\@=" display
syn match   cssBoxProp contained "\<z-index\>\(\s*:\)\@=" display
syn match   cssBoxProp contained "\<\%(min\|max\)-\%(width\|height\)\>\(\s*:\)\@=" display
syn match   cssBoxProp contained "\<\(width\|height\|float\|clear\|overflow\%(-[xy]\)\=\|clip\|visibility\)\>\(\s*:\)\@=" display
syn keyword cssBoxAttr contained thin thick both
syn keyword cssBoxAttr contained dotted dashed solid double groove ridge inset outset
syn keyword cssBoxAttr contained hidden visible scroll collapse

syn match   cssGeneratedContentProp contained "\<\(content\|quotes\)\>\(\s*:\)\@=" display
syn match   cssGeneratedContentProp contained "\<counter-\%(reset\|increment\)\>\(\s*:\)\@=" display
syn match   cssGeneratedContentProp contained "\<list-style\%(-\%(type\|position\|image\)\)\=\>\(\s*:\)\@=" display
syn match   cssGeneratedContentAttr contained "\<\%(no-\)\=\%(open\|close\)-quote\>" display
syn match   cssGeneratedContentAttr contained "\<\(\%(lower\|upper\)-\%(alpha\|latin\|roman\)\|lower-greek\)\>" display
syn match   cssGeneratedContentAttr contained "\<\(hiragana\|katakana\)\%(-iroha\)\=\>" display
syn match   cssGeneratedContentAttr contained "\<\(decimal\%(-leading-zero\)\=\|cjk-ideographic\)\>" display
syn keyword cssGeneratedContentAttr contained disc circle square hebrew armenian georgian
syn keyword cssGeneratedContentAttr contained inside outside

syn match   cssPagingProp contained "\<page\%(-break-\%(before\|after\|inside\)\)\=\>\(\s*:\)\@=" display
syn match   cssPagingProp contained "\<\(size\|marks\|inside\|orphans\|widows\)\>\(\s*:\)\@=" display
syn keyword cssPagingAttr contained landscape portrait crop cross always avoid

syn match   cssUIProp contained "\<cursor\>\(\s*:\)\@=" display
syn match   cssUIAttr contained "\<\%(col\|row\|nesw\|nwse\|[ns]\=[ew]\=\)-resize\>" display
syn keyword cssUIAttr contained all-scroll alias cell context-menu copy crosshair
syn keyword cssUIAttr contained default move help no-drop not-allowed pointer progress
syn keyword cssUIAttr contained text thin thick wait vertical-text
syn keyword cssUIAttr contained dotted dashed solid double groove ridge inset outset
syn keyword cssUIAttr contained invert

syn match   cssRenderAttr contained "\<marker\>" display
syn match   cssRenderProp contained "\<\(display\|marker-offset\|unicode-bidi\|white-space\)\>\(\s*:\)\@=" display
syn match   cssRenderProp contained "\<\(position\|direction\)\>\(\s*:\)\@=" display
syn match   cssRenderProp contained "\<\(top\|bottom\|left\|right\)\>\(\s*:\)\@=" display
syn keyword cssRenderAttr contained block inline compact
syn match   cssRenderAttr contained "\<table\%(-\%(\%(header\|footer\)-group\|\%(row\|column\)\%(-group\)\=\|cell\|caption\|colgroup\)\)\=\>" display
syn keyword cssRenderAttr contained static relative absolute fixed
syn keyword cssRenderAttr contained ltr rtl embed bidi-override pre nowrap pre-wrap pre-line


syn match   cssAuralProp contained "\<\(pause\|cue\)\%(-\%(before\|after\)\)\=\>\(\s*:\)\@=" display
syn match   cssAuralProp contained "\<\(play-during\|speech-rate\|voice-family\|pitch\%(-range\)\=\|speak\%(-\%(punctuation\|numerals\)\)\=\)\>\(\s*:\)\@=" display
syn match   cssAuralProp contained "\<\(volume\|during\|azimuth\|elevation\|stress\|richness\)\>\(\s*:\)\@=" display
syn match   cssAuralAttr contained "\<\%(x-\)\=\(soft\|loud\)\>" display
syn keyword cssAuralAttr contained silent
syn match   cssAuralAttr contained "\<spell-out\>" display
syn keyword cssAuralAttr contained non mix
syn match   cssAuralAttr contained "\<\%(left\|right\)-side\>" display
syn match   cssAuralAttr contained "\<\%(far\|center\)-\%(left\|center\|right\)\>" display
syn keyword cssAuralAttr contained leftwards rightwards behind
syn keyword cssAuralAttr contained below level above higher
syn match   cssAuralAttr contained "\<\%(x-\)\=\(slow\|fast\)\>" display
syn keyword cssAuralAttr contained faster slower
syn keyword cssAuralAttr contained male female child code digits continuous
syn match   cssAuralAttr contained "\<lower\>" display

syn match   cssTableProp contained "\<\(caption-side\|table-layout\|border-collapse\|border-spacing\|empty-cells\|speak-header\)\>\(\s*:\)\@=" display
syn keyword cssTableAttr contained fixed collapse separate show hide once always

"  CSS3

"   Multi-column layouts
syn match   cssBoxProp contained "\(-\(moz\|webkit\)-\|\)column-\%(width\|rule\%(-\%(color\|width\|style\)\)\=\|gap\|count\|span\)\>\(\s*:\)\@=" display
syn match   cssBoxProp contained "\(-moz-\)\=column-fill\>\(\s*:\)\@=" display
syn match   cssBoxProp contained "\(-\(moz\|webkit\)-\|\)columns\>\(\s*:\)\@=" display

syn match   cssRenderProp contained "\(-\(webkit\)-\|\(-\(moz\|o\)-\)\@<!\)animation\%(-\%(delay\|direction\|duration\|fill-mode\|iteration-count\|name\|play-state\|timing-function\)\)\=\>\(\s*:\)\@=" display
syn match   cssRenderProp contained "\(-\(webkit\)-\|\(-\(moz\|o\)-\)\@<!\)transition\%(-\%(delay\|duration\|property\|timing-function\)\)\=\>\(\s*:\)\@=" display
syn match   cssRenderProp contained "\(-\(webkit\)-\|\(-\(moz\|ms\|o\)-\)\@<!\)transform\%(-\%(origin\|style\)\)\=\>\(\s*:\)\@=" display

syn keyword cssBoxAttr contained border-box content-box padding-box
syn keyword cssBoxAttr contained balance horizontal round space vertical
syn keyword cssBoxAttr contained ignore stretch stretch-to-fit
syn keyword cssTextAttr contained ellipsis clip break-word break-all keep-all
syn keyword cssTextAttr contained manual wavy
syn keyword cssTextAttr contained start end match-parent
syn match   cssRenderAttr contained "\<\(ease\%(-\%(in\|out\|in-out\)\)\=\|linear\|step-\%(start\|end\|stop\)\)\>" display
syn match   cssRenderAttr contained "\<\(alternate\%(-reverse\)\=\|reverse\)\>" display
syn keyword cssRenderAttr contained forwards backwards
syn keyword cssRenderAttr contained infinite paused running
syn keyword cssRenderAttr contained all
syn keyword cssRenderAttr contained flat preserve-3d
syn case match
syn match   cssRenderAttr contained "\<\(optimize\%(Legibility\|Quality\|Speed\)\|geometricPrecision\)\>" display
syn case ignore
syn match   cssRenderAttr contained "\<\(flex\|grid\|inline-\%(block\|flex\|grid\|table\)\|list-item\|run-in\)\>" display
syn match   cssCommonAttr contained "\(-moz-\)\@<!initial\>" display
syn keyword cssGeneratedContentAttr contained bounding-box continuous each-box
syn keyword cssGeneratedContentAttr contained contain cover fill

syn match   cssUIProp contained "\(-\(moz\|webkit\)-\|\)appearance\>\(\s*:\)\@=" display
syn match   cssUIProp contained "\<pointer-events\>\(\s*:\)\@=" display
syn match   cssUIProp contained "\<-moz-outline-radius\%(-\%(bottomleft\|bottomright\|topleft\|topright\)\)\=\>\(\s*:\)\@=" display
syn match   cssUIProp contained "\<outline\%(-\%(width\|style\|offset\|color\)\)\=\>\(\s*:\)\@=" display
syn match   cssUIProp contained "\(-moz-\)\=user-\%(focus\|input\|modify\)\>\(\s*:\)\@=" display
syn match   cssUIProp contained "\<user-select\>\(\s*:\)\@=" display
syn match   cssUIProp contained "\(-\(moz\)-\|\)resize\>\(\s*:\)\@=" display
syn match   cssBoxProp contained "\(-webkit-\)\=\(-moz-\)\@<!perspective\%(-origin\)\=\>\(\s*:\)\@=" display
syn match   cssBoxProp contained "\(-moz-\|\(-webkit-\)\@<!\)box-sizing\>\(\s*:\)\@=" display
syn match   cssBoxProp contained "\<-moz-box-ordinal-group\>\(\s*:\)\@=" display
syn match   cssBoxProp contained "\<box-shadow\>\(\s*:\)\@=" display

syn match   cssBoxProp contained "\<border-radius\>\(\s*:\)\@=" display
syn match   cssBoxProp contained "\<border-\%(bottom\|top\)-\%(left\|right\)-radius\>\(\s*:\)\@=" display
syn match   cssBoxProp contained "\<-moz-border-\%(\%(top\|right\|bottom\|left\)-colors\)\>\(\s*:\)\@=" display
syn match   cssBoxProp contained "\(-\(webkit\|o\)-\|\(-moz-\)\@<!\)border-image\>\(\s*:\)\@=" display
syn match   cssBoxProp contained "\<border-image-\%(source\|width\|repeat\|outset\|slice\)\>\(\s*:\)\@=" display

syn match   cssBoxProp contained "\(-\(moz\|webkit\)-\)\=\%(margin\|padding\|border\)-\%(end\|start\)\>\(\s*:\)\@=" display
syn match   cssBoxProp contained "\<-moz-stack-sizing\>\(\s*:\)\@=" display
syn match   cssBoxProp contained "\(-webkit-\)\=\(-moz-\)\@<!backface-visibility\>\(\s*:\)\@=" display
syn match   cssBoxProp contained "\(-moz-\)\=binding\>\(\s*:\)\@=" display
syn match   cssBoxProp contained "\<-moz-orient\>\(\s*:\)\@=" display
syn match   cssBoxProp contained "\<mask\>\(\s*:\)\@=" display
syn match   cssBoxProp contained "\<clip-path\>\(\s*:\)\@=" display
syn match   cssFontProp contained "\(-\(moz\|webkit\)-\|\)font-feature-settings\>\(\s*:\)\@=" display
syn match   cssTextProp contained "\(-\(moz\|webkit\|ms\)-\|\)hyphens\>\(\s*:\)\@=" display
syn match   cssTextProp contained "\(-moz-\)\=text-\%(align-last\|blink\)\>\(\s*:\)\@=" display
syn match   cssTextProp contained "\(-moz-\)\=text-decoration-\%(line\|color\|style\)\>\(\s*:\)\@=" display
syn match   cssTextProp contained "\<text-\%(justify\|\outline\|overflow\|warp\|indent\)\>\(\s*:\)\@=" display
syn match   cssTextProp contained "\<word-\%(break\|\wrap\)\>\(\s*:\)\@=" display
syn match   cssRenderProp contained "\<opacity\>\(\s*:\)\@=" display
syn match   cssRenderProp contained "\<image-rendering\>\(\s*:\)\@=" display
syn match   cssRenderProp contained "\(-\(webkit\)-\|\(-\(moz\|ms\|o\)-\)\@<!\)filter\>\(\s*:\)\@=" display
syn match   cssGeneratedContentProp contained "\<background\%(-\%(origin\|clip\|repeat\|color\|image\|attachment\|position\|size\)\)\=\>\(\s*:\)\@=" display
syn match   cssGeneratedContentProp contained "\<-moz-background-inline-policy\>\(\s*:\)\@=" display
syn match   cssGeneratedContentProp contained "\<-moz-image-region\>\(\s*:\)\@=" display

syn match   cssTextProp contained "\<ime-mode\>" display
syn keyword cssTextAttr contained active inactive disabled

"   Flexible Box
syn match   cssBoxProp contained "\(-\(webkit\)-\|\(-\(moz\|ms\|o\)-\)\@<!\)align-\%(content\|items\|self\)\>\(\s*:\)\@=" display
syn match   cssBoxProp contained "\(-\(webkit\)-\|\(-\(moz\|ms\|o\)-\)\@<!\)flex\%(-\%(basis\|direction\|flow\|grow\|shrink\|wrap\)\)\=\>\(\s*:\)\@=" display
syn match   cssBoxProp contained "\(-\(webkit\)-\|\(-\(moz\|ms\|o\)-\)\@<!\)justify-content\>\(\s*:\)\@=" display
syn match   cssBoxProp contained "\(-\(webkit\)-\|\(-\(moz\|ms\|o\)-\)\@<!\)order\>\(\s*:\)\@=" display
syn match   cssBoxAttr contained "\<\(flex-\%(start\|end\)\|\(row\|column\|wrap\)\%(-reverse\)\=\|space-\%(between\|around\)\)\>" display

"syn match   cssProperty transparent contained "\<\(-\a\+-\)\=\a\+\(-\a\+\)\{0,3\}\>\(\s*:\)\@=" contains=cssFontDescriptorProp,css.\+Prop nextgroup=cssAttribute skipwhite
"syn region  cssAttribute transparent contained matchgroup=cssPropColon start=":" end="\ze[;}]" contains=cssComment,cssError,cssImportant,cssStringQ\+,cssUnicodeEscape,cssURL,cssFunction,cssColor,cssValue.\+,cssFontDescriptorAttr,css.\+Attr

syn match   cssBraces contained "[{}]"
syn match   cssError contained "{@<>"
"syn region  cssDefinition fold transparent matchgroup=cssBraces start='{' end='}' contains=cssProperty,cssComment,,cssError
syn region  cssDefinition fold transparent matchgroup=cssBraces start='{' end='}' contains=css.*Attr,css.*Prop,cssComment,cssValue.*,cssColor,cssURL,cssImportant,cssError,cssStringQ,cssStringQQ,cssFunction,cssUnicodeEscape
syn match   cssBraceError "}"

" At-rule Group
"   Nested at-rules:
"     Conditional Group Rules:
syn match   cssMedia "@media\>" nextgroup=cssMediaType,cssMediaOperators,cssMediaBrackets skipwhite
syn keyword cssMediaType contained screen print aural braile embosed handheld projection tty tv all nextgroup=cssMediaComma,cssMediaBlock,cssMediaAnd skipwhite
syn match   cssMediaComma contained "," nextgroup=cssMediaType skipwhite
syn region  cssMediaBlock fold transparent contained matchgroup=cssBraces start='{' end='}' contains=cssDocument,cssPage,cssFontDescriptor,cssKeyFrame,cssSupports,cssTagName,cssError,cssComment,cssDefinition,cssUnicodeEscape,cssIdentifier,cssAttributeSelector,@cssPseudo,cssSelectorOp,cssClassName
syn match   cssMediaAnd "\s\zsand\ze\s" contained nextgroup=cssMediaBrackets skipwhite
syn match   cssMediaOperators "\<\(not\|only\)\>" contained nextgroup=cssMediaType skipwhite
syn match   cssMediaFeatures contained "\<\(\(\(min\|max\)-\)\=\(\(\(device-\)\=\(height\|width\|aspect-ratio\)\)\|color\(-index\)\=\|monochrome\|resolution\)\|grid\|scan\|orientation\)\>" display nextgroup=cssMediaColon skipwhite
syn match   cssMediaColon contained ":" display nextgroup=cssMediaFeaturesValueError,css.\+Attr,cssValue.\+ skipwhite
syn region  cssMediaBrackets transparent contained start='(' end=')' contains=cssMediaFeatures nextgroup=cssMediaComma,cssMediaAnd,cssMediaBlock skipwhite
syn match   cssMediaFeaturesValueError contained "\(:\s*\)\@<=-\d\+\(\.\d\+\)\=" display

syn match   cssDocument "@\(-moz-\)\=document\>" nextgroup=cssDUrl,cssURLPrefix,cssDomain,cssRegexp skipwhite
syn region  cssURLPrefix contained matchgroup=cssFunctionName start="\<url-prefix\s*(" end=")" nextgroup=cssDocumentComma,cssDocumentBlock oneline keepend skipwhite
syn region  cssDomain contained matchgroup=cssFunctionName start="\<domain\s*(" end=")" nextgroup=cssDocumentComma,cssDocumentBlock oneline keepend skipwhite
syn region  cssRegexp contained matchgroup=cssFunctionName start="\<regexp\s*(\ze['"]" end="['"]\zs)" contains=cssRegexpError nextgroup=cssDocumentComma,cssDocumentBlock oneline keepend skipwhite
syn match   cssDocumentComma contained "," nextgroup=cssDUrl,cssURLPrefix,cssDomain,cssRegexp skipwhite skipnl
syn region  cssDUrl contained matchgroup=cssFunctionName start="\<url\s*(" end=")" nextgroup=cssDocumentComma,cssDocumentBlock oneline keepend skipwhite
syn region  cssDocumentBlock fold contained transparent matchgroup=cssBraces start='{' end='}' contains=cssError,cssComment,cssPage,cssMedia,cssFontDescriptor,cssKeyFrame,cssSupports,cssNestedSelector
syn match   cssNestedSelector transparent contained "[a-zA-Z*#.:\\][^{]*" contains=@cssPseudo,cssComment,cssError,cssAttributeSelector,cssSelectorOp,cssUnicodeEscape,cssTagName,cssClassName,cssIdentifier nextgroup=cssDefinition skipwhite skipnl skipempty
syn match   cssRegexpError contained +\(\<regexp(\)\@<=[^'"].*\()\%(,\s*\a\+(\|\s*{\(\s*\d\)\@!\)\)\@=\|\(\<regexp(\)\@<=['][^']*\()\%(,\s*\a\+(\|\s*{\(\s*\d\)\@!\)\)\@=\|\(\<regexp(\)\@<=["][^"]*\()\%(,\s*\a\+(\|\s*{\(\s*\d\)\@!\)\)\@=\|\\\@<!\\[^\\]+ display

" Incomplete
syn region  cssSupports transparent matchgroup=cssSupports start="^\s*\zs@supports\>" end="\ze{" contains=cssSupportsOperators,cssSupportsBrackets nextgroup=cssSupportsBlock
syn match   cssSupportsOperators contained "\(\<not\|\s\zs\%(and\|or\)\)\>\ze\%(\s\|$\)"
syn region  cssSupportsBrackets transparent contained start="(" end=")" contains=css.*Prop,css.*Attr,cssValue.*,cssSupportsOperators,cssSupportsBrackets
syn region  cssSupportsBlock fold transparent contained matchgroup=cssBraces start='{' end='}' contains=cssError,cssComment,cssPage,cssMedia,cssFontDescriptor,cssKeyFrame,cssDocument,cssNestedSelector

"     Conditional Group Rules End

syn match   cssPage "@page\>" nextgroup=cssPseudoClassId,cssDefinition

syn match   cssKeyFrame "@\(-webkit-\)\=\(-\(moz\|o\)-\)\@<!keyframes\>" nextgroup=cssKeyFrameID skipwhite skipnl
syn match   cssKeyFrameID contained "\<[a-zA-Z0-9_-]\+\>" nextgroup=cssKeyFrameBlock skipwhite skipnl
syn region  cssKeyFrameBlock fold transparent contained matchgroup=cssBraces start="{" end="}" contains=cssError,cssComment,cssKeyFrameTime
syn match   cssKeyFrameTime contained "\<\(from\|to\)\>\|\d\+%" nextgroup=cssDefinition skipwhite skipnl

syn match   cssFontDescriptor "@font-face\>" nextgroup=cssFontDescriptorBlock skipwhite skipnl
syn region  cssFontDescriptorBlock fold contained transparent matchgroup=cssBraces start="{" end="}" contains=cssComment,cssError,cssUnicodeEscape,cssFontProp,cssFontAttr,cssCommonAttr,cssStringQ,cssStringQQ,cssFontDescriptorProp,cssValue.*,cssFontDescriptorFunction,cssUnicodeRange,cssFontDescriptorAttr,cssImportant
syn match   cssFontDescriptorProp contained "\<\(unicode-range\|unit-per-em\|panose-1\|cap-height\|x-height\|definition-src\)\>\(\s*:\)\@=" display
syn keyword cssFontDescriptorProp contained src stemv stemh slope ascent descent widths bbox baseline centerline mathline topline
syn keyword cssFontDescriptorAttr contained all
syn region  cssFontDescriptorFunction contained matchgroup=cssFunctionName start="\<\(uri\|url\|local\|format\)\s*(" end=")" contains=cssStringQ,cssStringQQ oneline keepend
syn match   cssUnicodeRange contained "U+[0-9A-Fa-f?]\+" display
syn match   cssUnicodeRange contained "U+\x\+-\x\+" display

"   Nested at-rules End

syn region  cssNameSpace transparent matchgroup=cssNameSpace start="@namespace" end=";"he=e-1 contains=cssComment,cssStringQ,cssStringQQ,cssURL,cssNameSpaceName
syn match   cssNameSpaceName contained "\s\zs\<[a-zA-Z]\+\>\ze\s" display

syn region  cssInclude transparent matchgroup=cssInclude start="@import" end=";"he=e-1 contains=cssComment,cssURL,cssUnicodeEscape,cssMediaType,cssStringQ,cssStringQQ

syn region  cssCharset transparent matchgroup=cssCharset start="^@charset\ze\s" end=";"he=e-1 contains=cssComment,cssStringQ,cssStringQQ

" At-rule Group End

" Pseudo-classes and Pseudo-elements

syn match   cssPseudoClassId ":\(link\|visited\|active\|hover\|focus\|first\|left\|right\)\>" display
syn match   cssPseudoElement "\(:\{1,2\}\(before\|after\|first-letter\|first-line\)\|::selection\)\>" display
syn region  cssPseudoClassLang matchgroup=cssPseudoClassId start=":lang(" end=")" oneline
"  PseudoClass expansion list
syn match   cssPseudoClassId ":\(first\|last\|only\)-\(of-type\|child\)\>" display
syn match   cssPseudoClassId ":\(nth\|nth-last\)-\(of-type\|child\)\>\((\( \=\([-+]\=\(\d\+n\=\|n\) \=\([-+] \=\d\+ \=\)\=\|even \=\|odd \=\)\))\)\@=" display nextgroup=cssBracketsElement
syn match   cssPseudoClassId ":\(root\|empty\|target\|enabled\|disabled\|checked\|default\|indeterminate\|invalid\|optional\|required\|valid\)\>" display
syn match   cssPseudoClassId ":\(-\(moz\|webkit\)-\|\)any\>" display
syn region  cssPseudoClassNot matchgroup=cssPseudoClassId start=":not(" end=")" contains=cssAttributeSelector,cssStringQQ oneline
syn match   cssBracketsElement contained "(\( \=\%([-+]\=\%(\d\+n\=\|n\) \=\%([-+] \=\d\+ \=\)\=\|\%(even\|odd\) \=\)\))"hs=s+1,he=e-1 display
syn cluster cssPseudo contains=cssPseudoElement,cssPseudoClassId,cssPseudoClassNot,cssPseudoClassLang

syn region  cssComment start="/\*" end="\*/" contains=@Spell

syn match   cssUnicodeEscape "\\\x\{1,6}\s\?" display
syn match   cssSpecialCharQQ +\\"+ contained display
syn match   cssSpecialCharQ +\\'+ contained display
syn region  cssStringQQ start=+"+ skip=+\\\\\|\\"+ end=+"+ contains=cssUnicodeEscape,cssSpecialCharQQ
syn region  cssStringQ start=+'+ skip=+\\\\\|\\'+ end=+'+ contains=cssUnicodeEscape,cssSpecialCharQ
syn match   cssClassName "\.[A-Za-z][A-Za-z0-9_-]*" display


if main_syntax == 'css'
  " Syntax sync options
  if exists("css_default_sync") && g:css_default_sync == 1
    syn sync maxlines=200
  elseif !exists("css_default_sync") || g:css_default_sync == 0
    syn sync minlines=2000
  endif
  " Define the keyword identifier
  "  Added '-' symbol
  setlocal iskeyword+=-
endif

" Beautify CSS command
command! -buffer CSSBeautify call s:BeautifyTheCSS()
function! s:BeautifyTheCSS()
  execute "normal mz"
  %s/\%(\S\ze\|\s\{2,\}\|\s*\%(\n\s*\)\+\)\({\(\d\+\(,\d*\)\=}\)\@!\)\@=/ /ge|
    \ %s/{\s*\(\s*\n\|\d\+\(,\d*\)\=}\)\@!/{\r/ge|
    \ %s/\(\({\(\d*,\)\=\d*\)\@<![^;{}\t ]\)\@<=\(\s*\(\n\s*\)*}\)\@=/;/ge|
    \ %s/\(}\|;\)\@<=\s*\%(\%(\n\s*\)\+\(\s\)\@<=\)\=}/\r}/ge|
    \ %s/;\([^:;]\+:\)\@=/;\r/ge|
    \ %s/\(\d\)\@<!}\s*\([A-Za-z0-9#*.@:][^{]*{\)\@=/}\r/ge|
    \ %s/\s\+$//e|
    \ %s/\(^\s*[a-zA-Z-]\+\s*:\)\@<=\(\(\s\)\@!\|\s\{2,\}\)\|\(^\s*[a-zA-Z-]\+\s*:.*\S\)\@<=\(\s\{2,\}\)\=\(!\s*important\s*;$\|\(!\s*important\s*\)\@<!;$\)\@=/ /ge
  execute "normal `z"
endfunction

" Define the default highlighting.
" For version 5.7 and earlier: only when not done already
" For version 5.8 and later: only when an item doesn't have highlighting yet
if version >= 508 || !exists("did_css_syn_inits")
  if version < 508
    let did_css_syn_inits = 1
    command -nargs=+ HiLink hi link <args>
  else
    command -nargs=+ HiLink hi def link <args>
  endif

  HiLink cssComment Comment
  HiLink cssTagName Statement
  HiLink cssSelectorOp Special
  HiLink cssSelectorOp2 Special
  HiLink cssFontProp StorageClass
  HiLink cssColorProp StorageClass
  HiLink cssTextProp StorageClass
  HiLink cssBoxProp StorageClass
  HiLink cssAuralProp StorageClass
  HiLink cssRenderProp StorageClass
  HiLink cssGeneratedContentProp StorageClass
  HiLink cssPagingProp StorageClass
  HiLink cssTableProp StorageClass
  HiLink cssUIProp StorageClass
  HiLink cssFontAttr Type
  HiLink cssColorAttr Type
  HiLink cssTextAttr Type
  HiLink cssBoxAttr Type
  HiLink cssRenderAttr Type
  HiLink cssAuralAttr Type
  HiLink cssGeneratedContentAttr Type
  HiLink cssPagingAttr Type
  HiLink cssTableAttr Type
  HiLink cssUIAttr Type
  HiLink cssCommonAttr Type
  HiLink cssPseudoClassId PreProc
  HiLink cssPseudoElement PreProc
  HiLink cssPseudoClassLang Constant
  HiLink cssValueLength Number
  HiLink cssValuePercentage Number
  HiLink cssValueNumber Number
  HiLink cssValueAngle Number
  HiLink cssValueTime Number
  HiLink cssValueFrequency Number
  HiLink cssFunction Constant
  HiLink cssURL String
  HiLink cssFunctionName Function
  HiLink cssColor Constant
  HiLink cssIdentifier Function
  HiLink cssImportant Special
  HiLink cssBraces Function
  HiLink cssBraceError Error
  HiLink cssError Error
  HiLink cssInclude Statement
  HiLink cssUnicodeEscape Special
  HiLink cssStringQQ String
  HiLink cssStringQ String
  HiLink cssMedia Statement
  HiLink cssMediaType Special
  HiLink cssMediaComma Normal
  HiLink cssMediaAnd Operator
  HiLink cssMediaOperators Operator
  HiLink cssMediaFeatures StorageClass
  HiLink cssMediaFeaturesValueError Error
  HiLink cssFontDescriptor Statement
  HiLink cssFontDescriptorFunction Constant
  HiLink cssFontDescriptorProp StorageClass
  HiLink cssFontDescriptorAttr Type
  HiLink cssUnicodeRange Constant
  HiLink cssClassName Function
  HiLink cssBracketsElement Number
  HiLink cssDocument Statement
  HiLink cssDomain String
  HiLink cssDUrl String
  HiLink cssURLPrefix String
  HiLink cssRegexp String
  HiLink cssRegexpError Error
  HiLink cssCharset Statement
  HiLink cssValueResolution Number
  HiLink cssPage Statement
  HiLink cssNameSpace Statement
  HiLink cssKeyFrame Statement
  HiLink cssKeyFrameTime Number

  delcommand HiLink
endif

let b:current_syntax = "css"

if main_syntax == 'css'
  unlet main_syntax
endif

