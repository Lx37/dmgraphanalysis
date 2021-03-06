# -*- coding: utf-8 -*-
"""
Support function for igraph
"""

import numpy as np
import os


import igraph as ig

import cairo as ca

from utils_dtype_coord import where_in_coords,find_index_in_coords
import math

#igraph_colors = ['mediumvioletred',
#'palegoldenrod',
#'cornsilk',
#'lightgoldenrodyellow',
#'lavender',
#'chartreuse1',
#'chartreuse4',
#'blue',
#'maroon1',
#'gold1',
#'dimgray',
#'skyblue1',
#'steelblue',
#'floralwhite',
#'turquoise1',
#'yellow1',
#'violetred1',
#'darkkhaki',
#'firebrick1',
#'aliceblue',
#'lightseagreen',
#'dodgerblue',
#'royalblue',
#'darkslategray',
#'lemonchiffon',
#'navyblue',
#'lemonchiffon',
#'antiquewhite',
#'darkorchid',
#'yellow',
#'deeppink',
#'magenta',
#'palevioletred',
#'mediumaquamarine',
#'darkturquoise',
#'papayawhip',
#'mediumblue',
#'lightslategray',
#'violetred2',
#'khaki1',
#'hotpink',
#'khaki3',
#'salmon1',
#'violetred4',
#'salmon3',
#'salmon2',
#'salmon4',
#'mintcream',
#'green',
#'blueviolet',
#'brown2',
#'brown3',
#'brown1',
#'brown4',
#'cadetblue',
#'oldlace',
#'gray3',
#'skyblue4',
#'slategray',
#'darkgray',
#'maroon4',
#'maroon3',
#'maroon2',
#'chartreuse3',
#'chartreuse2',
#'gold3',
#'gold2',
#'gold4',
#'skyblue3',
#'skyblue2',
#'yellow4',
#'yellow3',
#'yellow2',
#'greenyellow',
#'darkviolet',
#'burlywood4',
#'steelblue',
#'navy',
#'darkred',
#'darkkhaki',
#'violetred',
#'darkgray',
#'royalblue',
#'blue1',
#'skyblue',
#'blue3',
#'blue2',
#'blue4',
#'grey72',
#'aliceblue',
#'lightgrey',
#'burlywood',
#'tomato4',
#'tomato1',
#'tomato3',
#'tomato2',
#'slategray',
#'forestgreen',
#'lightcyan',
#'lightslategrey',
#'darkblue',
#'seagreen4',
#'seagreen3',
#'seagreen2',
#'seagreen1',
#'limegreen',
#'gray40',
#'grey',
#'lightgreen',
#'lightcyan1',
#'lightcyan3',
#'lightcyan2',
#'lightcyan4',
#'rosybrown',
#'lightblue',
#'snow',
#'olivedrab4',
#'olivedrab1',
#'olivedrab2',
#'olivedrab3',
#'thistle3',
#'thistle2',
#'thistle1',
#'salmon',
#'thistle4',
#'oldlace',
#'grey100',
#'gold',
#'green4',
#'violetred',
#'green1',
#'green3',
#'green2',
#'darkslategray1',
#'darkslategray2',
#'darkslategray3',
#'darkslategray4',
#'steelblue1',
#'lightsteelblue',
#'yellowgreen',
#'gray100',
#'bisque4',
#'bisque1',
#'bisque2',
#'bisque3',
#'darkturquoise',
#'deeppink',
#'grey49',
#'grey48',
#'thistle',
#'darkorchid4',
#'darkorchid1',
#'darkorchid2',
#'darkorchid3',
#'palevioletred',
#'lightslateblue',
#'mediumpurple',
#'lightblue2',
#'lightblue3',
#'lightblue1',
#'lightblue4',
#'darkred',
#'mediumturquoise',
#'darkgoldenrod4',
#'lightyellow1',
#'lightyellow2',
#'lightyellow3',
#'lightyellow4',
#'navajowhite4',
#'mediumorchid',
#'olivedrab',
#'navajowhite1',
#'navajowhite2',
#'navajowhite3',
#'darkgoldenrod2',
#'blueviolet',
#'palegreen',
#'seashell',
#'slategrey',
#'darkgoldenrod',
#'tan4',
#'tan3',
#'tan2',
#'tan1',
#'lawngreen',
#'mintcream',
#'saddlebrown',
#'darkgoldenrod1',
#'burlywood1',
#'sandybrown',
#'burlywood3',
#'firebrick3',
#'burlywood2',
#'mediumseagreen',
#'darkorange',
#'steelblue3',
#'saddlebrown',
#'mediumorchid',
#'darkslategray',
#'lightyellow',
#'seagreen',
#'indianred',
#'lightyellow',
#'magenta4',
#'magenta3',
#'magenta2',
#'magenta1',
#'darkgoldenrod3',
#'chartreuse',
#'springgreen',
#'lightsalmon',
#'turquoise',
#'paleturquoise',
#'peachpuff',
#'slateblue2',
#'royalblue4',
#'royalblue1',
#'slateblue1',
#'royalblue3',
#'lightgoldenrod2',
#'orchid',
#'purple',
#'grey27',
#'indianred4',
#'indianred1',
#'indianred2',
#'indianred3',
#'khaki',
#'lightsalmon',
#'lightgrey',
#'plum',
#'azure',
#'honeydew1',
#'honeydew2',
#'honeydew3',
#'honeydew4',
#'antiquewhite',
#'mediumvioletred',
#'snow4',
#'snow2',
#'darksalmon',
#'snow1',
#'sandybrown',
#'mediumspringgreen',
#'mediumseagreen',
#'olivedrab',
#'ghostwhite',
#'lightcoral',
#'lightpink3',
#'forestgreen',
#'lightpink4',
#'cornsilk4',
#'cornsilk2',
#'cornsilk3',
#'lightgoldenrod4',
#'lightgoldenrod1',
#'lightgoldenrod3',
#'royalblue2',
#'springgreen',
#'lightgoldenrod',
#'limegreen',
#'seagreen',
#'mediumslateblue',
#'lavenderblush',
#'paleturquoise',
#'darkorchid',
#'dimgrey',
#'lightgreen',
#'mediumaquamarine',
#'darkgreen',
#'darkseagreen',
#'aquamarine4',
#'aquamarine1',
#'aquamarine3',
#'aquamarine2',
#'mistyrose',
#'brown',
#'cyan',
#'skyblue',
#'deepskyblue4',
#'deepskyblue3',
#'rosybrown2',
#'lightpink',
#'rosybrown1',
#'teal',
#'chocolate1',
#'lemonchiffon3',
#'lemonchiffon2',
#'lemonchiffon1',
#'bisque',
#'chocolate2',
#'lemonchiffon4',
#'grey13',
#'chocolate4',
#'grey16',
#'lightskyblue',
#'dimgrey',
#'midnightblue',
#'palegreen',
#'greenyellow',
#'sienna',
#'lime',
#'peru',
#'red3',
#'red2',
#'red1',
#'springgreen3',
#'red4',
#'chocolate',
#'darkgrey',
#'olive',
#'moccasin',
#'chocolate3',
#'darkslateblue',
#'coral',
#'springgreen1',
#'springgreen2',
#'dodgerblue',
#'springgreen4',
#'seashell2',
#'seashell3',
#'tan',
#'seashell1',
#'seashell4',
#'pink',
#'powderblue',
#'mediumpurple1',
#'mediumpurple2',
#'mediumpurple3',
#'mediumpurple4',
#'lightgray',
#'paleturquoise4',
#'paleturquoise3',
#'paleturquoise2',
#'paleturquoise1',
#'linen',
#'cyan1',
#'peachpuff',
#'orange4',
#'orange1',
#'orange3',
#'orange2',
#'slategrey',
#'mediumspringgreen',
#'darkslategrey',
#'lightskyblue',
#'orange',
#'darkmagenta',
#'snow3',
#'lightslategray',
#'mediumorchid4',
#'mediumorchid1',
#'orangered',
#'mediumorchid3',
#'mediumorchid2',
#'darkviolet',
#'darkslateblue',
#'darkmagenta',
#'darkorange',
#'ghostwhite',
#'khaki2',
#'red',
#'lightslateblue',
#'lightskyblue4',
#'lightskyblue1',
#'lightskyblue2',
#'lightskyblue3',
#'lightslategrey',
#'gainsboro',
#'cornflowerblue',
#'rosybrown',
#'darksalmon',
#'slategray1',
#'slategray2',
#'slategray3',
#'slategray4',
#'lightpink',
#'fuchsia',
#'blanchedalmond',
#'orangered',
#'navajowhite',
#'mistyrose',
#'white',
#'tomato',
#'blanchedalmond',
#'whitesmoke',
#'cadetblue',
#'mediumblue',
#'palegreen1',
#'palegreen3',
#'palegreen2',
#'palegreen4',
#'grey43',
#'mediumturquoise',
#'mistyrose1',
#'turquoise2',
#'mistyrose3',
#'mistyrose2',
#'mistyrose4',
#'turquoise4',
#'whitesmoke',
#'lawngreen',
#'grey46',
#'grey45',
#'purple4',
#'grey44',
#'purple1',
#'purple3',
#'purple2',
#'orangered3',
#'orangered2',
#'orangered1',
#'orangered4',
#'darkgrey',
#'gray19',
#'lightpink2',
#'darkseagreen4',
#'darkseagreen3',
#'darkseagreen2',
#'darkseagreen1',
#'gray14',
#'lightpink1',
#'lightsalmon4',
#'lightsalmon2',
#'lightsalmon3',
#'lightsalmon1',
#'turquoise3',
#'navajowhite',
#'papayawhip',
#'black',
#'indianred',
#'orchid4',
#'orchid1',
#'orchid2',
#'orchid3',
#'antiquewhite3',
#'antiquewhite2',
#'antiquewhite1',
#'antiquewhite4',
#'gray',
#'cornsilk1',
#'plum4',
#'plum3',
#'plum2',
#'plum1',
#'darkcyan',
#'violet',
#'honeydew',
#'gray18',
#'cornflowerblue',
#'darkblue',
#'palevioletred4',
#'palevioletred1',
#'palevioletred2',
#'palevioletred3',
#'floralwhite',
#'lavenderblush1',
#'lavenderblush3',
#'lavenderblush2',
#'lavenderblush4',
#'aqua',
#'lightgoldenrod',
#'aquamarine',
#'slateblue',
#'darkorange4',
#'darkorange1',
#'darkorange3',
#'darkorange2',
#'darkcyan',
#'goldenrod4',
#'hotpink',
#'goldenrod1',
#'goldenrod2',
#'goldenrod3',
#'darkgoldenrod',
#'lightgoldenrodyellow',
#'ivory3',
#'ivory2',
#'ivory1',
#'ivory4',
#'sienna1',
#'palegoldenrod',
#'sienna3',
#'sienna2',
#'mediumpurple',
#'deepskyblue',
#'pink1',
#'pink3',
#'pink2',
#'pink4',
#'darkolivegreen4',
#'lightsteelblue',
#'darkolivegreen1',
#'darkolivegreen3',
#'darkolivegreen2',
#'lavenderblush',
#'lightgray',
#'powderblue',
#'azure1',
#'azure3',
#'azure2',
#'azure4',
#'firebrick',
#'darkolivegreen',
#'darkolivegreen',
#'lightsteelblue1',
#'lightsteelblue2',
#'lightsteelblue3',
#'lightsteelblue4',
#'mediumslateblue',
#'sienna4',
#'silver',
#'darkseagreen',
#'cyan2',
#'cyan3',
#'goldenrod',
#'darkgreen',
#'cyan4',
#'peachpuff4',
#'slateblue4',
#'slateblue3',
#'peachpuff1',
#'peachpuff2',
#'peachpuff3',
#'yellowgreen',
#'wheat4',
#'wheat1',
#'wheat3',
#'wheat2',
#'coral3',
#'coral2',
#'coral1',
#'rosybrown4',
#'rosybrown3',
#'deepskyblue2',
#'deepskyblue1',
#'coral4',
#'wheat',
#'deepskyblue',
#'darkslategrey',
#'beige',
#'dodgerblue1',
#'dodgerblue2',
#'dodgerblue3',
#'dodgerblue4',
#'lightcoral',
#'ivory',
#'midnightblue',
#'lightcyan',
#'maroon',
#'lightseagreen',
#'lightblue',
#'dimgray',
#'cadetblue4',
#'cadetblue3',
#'cadetblue2',
#'cadetblue1',
#'deeppink3',
#'deeppink2',
#'deeppink1',
#'deeppink4',
#'hotpink3',
#'hotpink2',
#'hotpink1',
#'hotpink4',
#'firebrick2',
#'steelblue2',
#'steelblue4',
#'firebrick4',
#'khaki4',
#'violetred3',
#'navyblue',
#'slateblue']

#igraph_colors = ['mediumvioletred',
#'palegoldenrod',
#'yellow',
#'grey61',
#'grey60',
#'grey63',
#'grey62',
#'grey65',
#'grey64',
#'grey67',
#'grey66',
#'grey69',
#'grey68',
#'darkgray',
#'cornsilk',
#'slategray',
#'lightgoldenrodyellow',
#'lavender','chartreuse3','chartreuse2','chartreuse1','chartreuse4','blue','maroon4',
#'maroon3',
#'maroon2',
#'maroon1',
#'gold3',
#'gold2',
#'gold1',
#'gold4',
#'dimgray',
#'skyblue4',
#'skyblue1',
#'skyblue3',
#'skyblue2',
#'steelblue',
#'floralwhite',
#'turquoise1',
#'darkkhaki',
#'firebrick2',
#'firebrick1',
#'steelblue2',
#'steelblue4',
#'firebrick4',
#'aliceblue',
#'lightseagreen',
#'dodgerblue',
#'royalblue',
#'darkslategray',
#'lemonchiffon',
#'navyblue',
#'lemonchiffon',
#'antiquewhite',
#'darkorchid',
#'gray69',
#'gray68',
#'deeppink',
#'gray65',
#'gray64',
#'gray67',
#'gray66',
#'gray61',
#'gray60',
#'gray63',
#'gray62',
#'magenta',
#'palevioletred',
#'mediumaquamarine',
#'darkturquoise',
#'papayawhip',
#'mediumblue',
#'lightslategray',
#'violetred1',
#'violetred2',
#'khaki4',
#'violetred3',
#'khaki1',
#'hotpink',
#'khaki3',
#'salmon1',
#'violetred4',
#'salmon3',
#'salmon2',
#'salmon4',
#'mintcream',
#'green',
#'blueviolet',
#'brown2',
#'brown3',
#'brown1',
#'brown4',
#'cadetblue',
#'oldlace',
#'gray3',
#'yellow4',
#'yellow3',
#'yellow2',
#'yellow1',
#'greenyellow',
#'grey58',
#'grey59',
#'grey54',
#'grey55',
#'grey56',
#'grey57',
#'grey50',
#'grey51',
#'grey52',
#'grey53',
#'darkviolet',
#'burlywood4',
#'steelblue',
#'navy',
#'darkred',
#'darkkhaki',
#'violetred',
#'darkgray',
#'royalblue',
#'blue1',
#'skyblue',
#'blue3',
#'blue2',
#'blue4',
#'grey72',
#'aliceblue',
#'lightgrey',
#'burlywood',
#'tomato4',
#'tomato1',
#'grey74',
#'tomato3',
#'tomato2',
#'grey78',
#'slategray',
#'grey79',
#'forestgreen',
#'lightcyan',
#'lightslategrey',
#'darkblue',
#'seagreen4',
#'seagreen3',
#'seagreen2',
#'seagreen1',
#'limegreen',
#'gray40',
#'grey',
#'lightgreen',
#'lightcyan1',
#'lightcyan3',
#'lightcyan2',
#'lightcyan4',
#'rosybrown',
#'lightblue',
#'snow',
#'gray58',
#'gray59',
#'olivedrab4',
#'gray51',
#'gray52',
#'gray53',
#'gray54',
#'olivedrab1',
#'olivedrab2',
#'olivedrab3',
#'thistle3',
#'thistle2',
#'thistle1',
#'salmon',
#'thistle4',
#'oldlace',
#'grey100',
#'gold',
#'green4',
#'violetred',
#'green1',
#'green3',
#'green2',
#'darkslategray1',
#'darkslategray2',
#'darkslategray3',
#'darkslategray4',
#'steelblue1',
#'lightsteelblue',
#'yellowgreen',
#'gray100',
#'bisque4',
#'bisque1',
#'bisque2',
#'bisque3',
#'darkturquoise',
#'deeppink',
#'grey49',
#'grey48',
#'thistle',
#'darkorchid4',
#'grey42',
#'grey41',
#'grey40',
#'grey47',
#'darkorchid1',
#'darkorchid2',
#'darkorchid3',
#'palevioletred',
#'lightslateblue',
#'mediumpurple',
#'lightblue2',
#'lightblue3',
#'lightblue1',
#'lightblue4',
#'darkred',
#'mediumturquoise',
#'grey38',
#'grey39',
#'grey36',
#'grey37',
#'grey34',
#'grey35',
#'grey32',
#'grey33',
#'grey30',
#'grey31',
#'darkgoldenrod4',
#'lightyellow1',
#'lightyellow2',
#'lightyellow3',
#'lightyellow4',
#'navajowhite4',
#'mediumorchid',
#'olivedrab',
#'navajowhite1',
#'navajowhite2',
#'navajowhite3',
#'darkgoldenrod2',
#'blueviolet',
#'palegreen',
#'seashell',
#'slategrey',
#'darkgoldenrod',
#'tan4',
#'tan3',
#'tan2',
#'tan1',
#'lawngreen',
#'mintcream',
#'saddlebrown',
#'darkgoldenrod1',
#'burlywood1',
#'sandybrown',
#'burlywood3',
#'firebrick3',
#'burlywood2',
#'mediumseagreen',
#'darkorange',
#'steelblue3',
#'saddlebrown',
#'mediumorchid',
#'darkslategray',
#'gray47',
#'gray46',
#'gray45',
#'gray44',
#'gray43',
#'gray42',
#'gray41',
#'lightyellow',
#'gray49',
#'gray48',
#'seagreen',
#'indianred',
#'lightyellow',
#'magenta4',
#'magenta3',
#'magenta2',
#'magenta1',
#'darkgoldenrod3',
#'chartreuse',
#'springgreen',
#'lightsalmon',
#'turquoise',
#'grey8',
#'grey9',
#'grey6',
#'grey7',
#'grey4',
#'grey5',
#'grey2',
#'grey3',
#'grey0',
#'grey1',
#'gray50',
#'gray55',
#'gray56',
#'gray57',
#'paleturquoise',
#'peachpuff',
#'slateblue2',
#'royalblue4',
#'royalblue1',
#'slateblue1',
#'royalblue3',
#'lightgoldenrod2',
#'orchid',
#'purple',
#'grey27',
#'indianred4',
#'indianred1',
#'indianred2',
#'indianred3',
#'khaki',
#'lightsalmon',
#'lightgrey',
#'plum',
#'azure',
#'honeydew1',
#'honeydew2',
#'honeydew3',
#'honeydew4',
#'antiquewhite',
#'mediumvioletred',
#'snow4',
#'snow2',
#'darksalmon',
#'snow1',
#'sandybrown',
#'grey29',
#'grey28',
#'grey25',
#'grey24',
#'mediumspringgreen',
#'grey26',
#'grey21',
#'grey20',
#'grey23',
#'grey22',
#'mediumseagreen',
#'olivedrab',
#'ghostwhite',
#'lightcoral',
#'lightpink3',
#'forestgreen',
#'lightpink4',
#'cornsilk4',
#'cornsilk2',
#'cornsilk3',
#'lightgoldenrod4',
#'grey90',
#'grey91',
#'grey92',
#'grey93',
#'grey94',
#'grey95',
#'grey96',
#'grey97',
#'grey98',
#'lightgoldenrod1',
#'lightgoldenrod3',
#'royalblue2',
#'springgreen',
#'lightgoldenrod',
#'limegreen',
#'seagreen',
#'mediumslateblue',
#'lavenderblush',
#'paleturquoise',
#'darkorchid',
#'dimgrey',
#'lightgreen',
#'mediumaquamarine',
#'darkgreen',
#'darkseagreen',
#'gray32',
#'gray33',
#'gray30',
#'gray31',
#'gray36',
#'gray37',
#'gray34',
#'gray35',
#'aquamarine4',
#'gray38',
#'gray39',
#'aquamarine1',
#'aquamarine3',
#'aquamarine2',
#'mistyrose',
#'brown',
#'gray8',
#'gray9',
#'gray2',
#'cyan',
#'gray0',
#'gray1',
#'gray6',
#'gray7',
#'gray4',
#'gray5',
#'skyblue',
#'deepskyblue4',
#'deepskyblue3',
#'rosybrown2',
#'lightpink',
#'rosybrown1',
#'teal',
#'chocolate1',
#'lemonchiffon3',
#'lemonchiffon2',
#'lemonchiffon1',
#'bisque',
#'chocolate2',
#'lemonchiffon4',
#'grey13',
#'chocolate4',
#'grey16',
#'lightskyblue',
#'dimgrey',
#'midnightblue',
#'palegreen',
#'greenyellow',
#'sienna',
#'lime',
#'peru',
#'red3',
#'red2',
#'red1',
#'springgreen3',
#'red4',
#'chocolate',
#'darkgrey',
#'olive',
#'grey18',
#'grey19',
#'moccasin',
#'grey10',
#'grey11',
#'grey12',
#'chocolate3',
#'grey14',
#'grey15',
#'darkslateblue',
#'grey17',
#'coral',
#'springgreen1',
#'springgreen2',
#'dodgerblue',
#'springgreen4',
#'seashell2',
#'seashell3',
#'tan',
#'seashell1',
#'seashell4',
#'pink',
#'powderblue',
#'grey89',
#'grey88',
#'grey87',
#'grey86',
#'grey85',
#'grey84',
#'grey83',
#'grey82',
#'grey81',
#'grey80',
#'mediumpurple1',
#'mediumpurple2',
#'mediumpurple3',
#'mediumpurple4',
#'lightgray',
#'paleturquoise4',
#'paleturquoise3',
#'paleturquoise2',
#'paleturquoise1',
#'linen',
#'cyan1',
#'peachpuff',
#'orange4',
#'orange1',
#'orange3',
#'orange2',
#'slategrey',
#'mediumspringgreen',
#'darkslategrey',
#'lightskyblue',
#'orange',
#'darkmagenta',
#'snow3',
#'lightslategray',
#'mediumorchid4',
#'mediumorchid1',
#'orangered',
#'mediumorchid3',
#'mediumorchid2',
#'gray21',
#'gray20',
#'gray23',
#'gray22',
#'gray25',
#'gray24',
#'gray27',
#'gray26',
#'gray29',
#'gray28',
#'darkviolet',
#'darkslateblue',
#'darkmagenta',
#'darkorange',
#'ghostwhite',
#'khaki2',
#'gray94',
#'gray95',
#'gray96',
#'gray97',
#'gray90',
#'gray91',
#'gray92',
#'gray93',
#'gray98',
#'gray99',
#'red',
#'lightslateblue',
#'lightskyblue4',
#'lightskyblue1',
#'lightskyblue2',
#'lightskyblue3',
#'lightslategrey',
#'gainsboro',
#'cornflowerblue',
#'rosybrown',
#'darksalmon',
#'slategray1',
#'slategray2',
#'slategray3',
#'slategray4',
#'lightpink',
#'fuchsia',
#'blanchedalmond',
#'orangered',
#'navajowhite',
#'mistyrose',
#'white',
#'tomato',
#'blanchedalmond',
#'whitesmoke',
#'cadetblue',
#'mediumblue',
#'palegreen1',
#'palegreen3',
#'palegreen2',
#'palegreen4',
#'grey43',
#'mediumturquoise',
#'mistyrose1',
#'turquoise2',
#'mistyrose3',
#'mistyrose2',
#'mistyrose4',
#'turquoise4',
#'whitesmoke',
#'lawngreen',
#'grey46',
#'grey45',
#'purple4',
#'grey44',
#'purple1',
#'purple3',
#'purple2',
#'orangered3',
#'orangered2',
#'orangered1',
#'orangered4',
#'darkgrey',
#'gray19',
#'lightpink2',
#'darkseagreen4',
#'darkseagreen3',
#'darkseagreen2',
#'darkseagreen1',
#'gray14',
#'lightpink1',
#'lightsalmon4',
#'lightsalmon2',
#'lightsalmon3',
#'lightsalmon1',
#'turquoise3',
#'navajowhite',
#'papayawhip',
#'black',
#'indianred',
#'orchid4',
#'orchid1',
#'orchid2',
#'orchid3',
#'antiquewhite3',
#'antiquewhite2',
#'antiquewhite1',
#'antiquewhite4',
#'gray',
#'cornsilk1',
#'plum4',
#'plum3',
#'plum2',
#'plum1',
#'darkcyan',
#'violet',
#'honeydew',
#'gray18',
#'cornflowerblue',
#'darkblue',
#'gray15',
#'gray16',
#'gray17',
#'gray10',
#'gray11',
#'gray12',
#'gray13',
#'palevioletred4',
#'palevioletred1',
#'palevioletred2',
#'palevioletred3',
#'floralwhite',
#'lavenderblush1',
#'lavenderblush3',
#'lavenderblush2',
#'lavenderblush4',
#'grey99',
#'aqua',
#'gray83',
#'gray82',
#'gray81',
#'gray80',
#'gray87',
#'gray86',
#'gray85',
#'gray84',
#'gray89',
#'gray88',
#'lightgoldenrod',
#'aquamarine',
#'slateblue',
#'darkorange4',
#'darkorange1',
#'darkorange3',
#'darkorange2',
#'darkcyan',
#'goldenrod4',
#'hotpink',
#'goldenrod1',
#'goldenrod2',
#'goldenrod3',
#'darkgoldenrod',
#'lightgoldenrodyellow',
#'ivory3',
#'ivory2',
#'ivory1',
#'ivory4',
#'sienna1',
#'palegoldenrod',
#'sienna3',
#'sienna2',
#'mediumpurple',
#'grey73',
#'grey70',
#'grey71',
#'grey76',
#'grey77',
#'deepskyblue',
#'grey75',
#'pink1',
#'pink3',
#'pink2',
#'pink4',
#'darkolivegreen4',
#'lightsteelblue',
#'darkolivegreen1',
#'darkolivegreen3',
#'darkolivegreen2',
#'lavenderblush',
#'lightgray',
#'powderblue',
#'azure1',
#'azure3',
#'azure2',
#'azure4',
#'firebrick',
#'darkolivegreen',
#'darkolivegreen',
#'lightsteelblue1',
#'lightsteelblue2',
#'lightsteelblue3',
#'lightsteelblue4',
#'mediumslateblue',
#'sienna4',
#'silver',
#'darkseagreen',
#'cyan2',
#'cyan3',
#'goldenrod',
#'darkgreen',
#'cyan4',
#'peachpuff4',
#'slateblue4',
#'slateblue3',
#'peachpuff1',
#'peachpuff2',
#'peachpuff3',
#'yellowgreen',
#'wheat4',
#'wheat1',
#'wheat3',
#'wheat2',
#'coral3',
#'coral2',
#'coral1',
#'rosybrown4',
#'rosybrown3',
#'deepskyblue2',
#'deepskyblue1',
#'coral4',
#'wheat',
#'deepskyblue',
#'darkslategrey',
#'beige',
#'dodgerblue1',
#'dodgerblue2',
#'dodgerblue3',
#'dodgerblue4',
#'lightcoral',
#'gray78',
#'gray79',
#'gray76',
#'gray77',
#'gray74',
#'gray75',
#'gray72',
#'gray73',
#'gray70',
#'gray71',
#'ivory',
#'midnightblue',
#'lightcyan',
#'maroon',
#'lightseagreen',
#'lightblue',
#'dimgray',
#'cadetblue4',
#'cadetblue3',
#'cadetblue2',
#'cadetblue1',
#'deeppink3',
#'deeppink2',
#'deeppink1',
#'deeppink4',
#'hotpink3',
#'hotpink2',
#'hotpink1',
#'hotpink4',
#'navyblue',
#'slateblue']

#igraph_colors = ['red','blue','green','yellow','brown','purple','lavender','cornsilk','black']

nb_igraph_colors = 100

######################################## generate colors #################################

import matplotlib.cm as cm

def frac_tohex_tuple(val_rgb):
    
    return frac_tohex(val_rgb[0],val_rgb[1],val_rgb[2])
    
def frac_tohex(r,g,b):
    
    return int_tohex(r*255,g*255,b*255)
    
    
def int_tohex(r,g,b):
    
    hexchars = "0123456789ABCDEF"
    return "#" + hexchars[int(r / 16)] + hexchars[int(r % 16)] + hexchars[int(g / 16)] + hexchars[int(g % 16)] + hexchars[int(b / 16)] + hexchars[int(b % 16)]
     
def generate_igraph_colors(nb_colors):

    import colorsys
    import matplotlib.cm as cm
    
    N = 1000
    
    RGB_tuples = cm.get_cmap('rainbow',N)
    
    #print RGB_tuples
    
    #RGB_tuples = my_cmap[:N]
    
    #print RGB_tuples
    
    
    #print RGB_tuples
    
    igraph_colors = []
    
    increment = 1
    val = 0
    
    
    while len(igraph_colors) < nb_colors:
        
        #print val, val*N
        #print RGB_tuples[int(val*N)]
        
        color = frac_tohex_tuple(RGB_tuples(val))
        
        #print color
        
        if not color in igraph_colors:
            igraph_colors.append(color)
            
        val = val+ 1.0/(3.0*float(increment))
        
        if (val >= 1.0):
            
            val = 1.0/(3.0*float(increment))
            
            increment = increment +1
            
        #print len(igraph_colors)
    
    
    return igraph_colors

    # OK marche HSV
#def generate_igraph_colors(nb_colors):

    #import colorsys
    
    #N = 1000
    #HSV_tuples = [(x*1.0/N, 0.5, 0.5) for x in range(N)]
    #RGB_tuples = map(lambda x: colorsys.hsv_to_rgb(*x), HSV_tuples)
    
    ##print RGB_tuples
    
    #igraph_colors = []
    
    #increment = 1
    #val = 0
    
    
    #while len(igraph_colors) < nb_colors:
        
        ##print val, val*N
        ##print RGB_tuples[int(val*N)]
        
        #color = frac_tohex_tuple(RGB_tuples[int(val*N)])
        
        ##print color
        
        #if not color in igraph_colors:
            #igraph_colors.append(color)
            
        #val = val+ 1.0/(3.0*float(increment))
        
        #if (val >= 1.0):
            
            #val = 1.0/(3.0*float(increment))
            
            #increment = increment +1
            
        ##print len(igraph_colors)
    
    
    #return igraph_colors

    ## OK marche
#def generate_igraph_colors(nb_colors):

    #import colorsys
    
    #N = 1000
    #HSV_tuples = [(x*1.0/N, 0.5, 0.5) for x in range(N)]
    #RGB_tuples = map(lambda x: colorsys.hsv_to_rgb(*x), HSV_tuples)
    
    #print RGB_tuples
    
    #igraph_colors = []
    
    #increment = 2
    #val = 0
    
    #for i in range(nb_colors):
    
        ##print val, val*N
        ##print RGB_tuples[int(val*N)]
        
        #print int(i*N/nb_colors)
        
        #print RGB_tuples[int(i*N/nb_colors)]
        
        #color = frac_tohex_tuple(RGB_tuples[int(i*N/nb_colors)])
        
        #print color
        
        ##if not color in igraph_colors:
        #igraph_colors.append(color)
            
        #print len(igraph_colors)
    
    ##print igraph_colors
    
    #return igraph_colors


#def generate_igraph_colors(nb_colors):

    #import colorsys
    
    #N = 10000
    #HSV_tuples = [(x*1.0/N, 0.5, 0.5) for x in range(N)]
    #RGB_tuples = map(lambda x: colorsys.hsv_to_rgb(*x), HSV_tuples)
    
    ##print RGB_tuples
    
    #igraph_colors = []
    
    #increment = 2
    #val = 0
    
    #while len(igraph_colors) < nb_colors:
        
        #val = val+ 1.0/float(increment)
        
        #if (val >= 1.0):
            
            #val = 1.0/float(increment)
            
            #increment = increment +1
            
        ##print val, val*N
        ##print RGB_tuples[int(val*N)]
        
        #color = frac_tohex_tuple(RGB_tuples[int(val*N)])
        
        ##print color
        
        #if not color in igraph_colors:
            #igraph_colors.append(color)
            
        ##print len(igraph_colors)
    
    ##print igraph_colors
    
    #return igraph_colors

igraph_colors = generate_igraph_colors(nb_igraph_colors)

######################################## igraph 2D #######################################

def plot_igraph_2D_adj_mat(signif_adj_matrix,gm_mask_coords_list,plot_nbs_adj_mat_file):
    
    mod_list = signif_adj_matrix.tolist()
    
    g= ig.Graph.Adjacency(mod_list,mode=ig.ADJ_MAX)
    
    #print g.degree()
    
    #g.es['sign'] = np.sign(g)
    
    #
    
    ###print g
    ig.plot(g, plot_nbs_adj_mat_file, layout = gm_mask_coords_list, vertex_size = g.degree())

######################################## igraph 3D #######################################
     
def project2D_np(node_coords):

    node_coords = np.transpose(np.vstack((node_coords[:,1],-node_coords[:,2]*0.5,node_coords[:,0])))
    
    #print node_coords
    
    ##0/0
    
    
    angle_alpha = 0.0
    angle_beta = 0.0

    print node_coords.shape
    
    #layout2D = project2D(node_coords.tolist(),0,0)
    layout2D = project2D(node_coords.tolist(),np.pi/180*angle_alpha,np.pi/180*angle_beta)
    
    
    
    #node_coords = np.transpose(np.vstack((node_coords[:,1],node_coords[:,2],node_coords[:,0])))
    
    #print node_coords.shape
    
    ##layout2D = project2D(node_coords.tolist(),0,0)
    #layout2D = project2D(node_coords.tolist(),0,0)
    
    return layout2D
    
def project2D(layout, alpha, beta):
    '''
    This method will project a set of points in 3D to 2D based on the given
    angles alpha and beta.
    '''
    # Calculate the rotation matrices based on the given angles.
    c = np.matrix([[1, 0, 0], [0, np.cos(alpha), np.sin(alpha)], [0, -np.sin(alpha), np.cos(alpha)]])
    c = c * np.matrix([[np.cos(beta), 0, -np.sin(beta)], [0, 1, 0], [np.sin(beta), 0, np.cos(beta)]])
    b = np.matrix([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
    # Hit the layout, rotate, and kill a dimension
    layout = np.matrix(layout)
    #x,y,z = (b * (c * layout.transpose())).transpose()
    
    X = (b * (c * layout.transpose())).transpose()
    
    #print X.shape
    
    proj = [[X[i,0],X[i,1],X[i,2]] for i in range(X.shape[0])]
     
    #print proj
    
    x,y,z = zip(*proj)
    
    #graph.vs['x2'], graph.vs['y2'], graph.vs['z2'] = zip(*layout2D)
    minX, maxX = min(x), max(x)
    minY, maxY = min(y), max(y)
    minZ, maxZ = min(z), max(z)
    
    
    
    layout2D_x = (x - minX) / (maxX - minX)
    layout2D_y = (y - minY) / (maxY - minY)
    
    #print layout2D_x
    #print layout2D_y
        
    layout2D = np.transpose(np.vstack((layout2D_x,layout2D_y)))
    
    #print layout2D.shape
    
    return layout2D

    
    
    
    
    
    
def plot_igraph_3D_int_mat_labels(int_matrix,coords,plot_nbs_adj_mat_file,labels = []):
    
    layout2D = project2D_np(coords)
     
    #print layout2D
        
    mod_list = int_matrix.tolist()
    
    #print mod_list
    
    g= ig.Graph.Weighted_Adjacency(mod_list,mode=ig.ADJ_MAX)
    
    
    if len(labels) == len(g.vs):
    
        g.vs['label'] = labels
        
        g.vs['label_size'] = 5
    
    
    vertex_degree = np.array(g.degree())*0.2
    
    
    
    #print vertex_degree
    
    #g.es['sign'] = np.sign(g)
    
    #
    ###print g
    #ig.plot(g, plot_nbs_adj_mat_file, layout = layout2D.tolist() , vertex_size = vertex_degree,    edge_width = np.array(g.es['weight']), edge_curved = True)
    #ig.plot(g, plot_nbs_adj_mat_file, layout = layout2D.tolist() , vertex_size = vertex_degree,    edge_width = 0.01, edge_curved = True)
    ig.plot(g, plot_nbs_adj_mat_file, layout = layout2D.tolist() , vertex_size = vertex_degree,    edge_width = 0.01, edge_curved = False)
    
    
def plot_igraph_3D_int_mat(int_matrix,coords,plot_nbs_adj_mat_file):
    
    layout2D = project2D_np(coords)
     
    #print layout2D
        
    mod_list = int_matrix.tolist()
    
    #print mod_list
    
    g= ig.Graph.Weighted_Adjacency(mod_list,mode=ig.ADJ_MAX)
    
    vertex_degree = np.array(g.degree())*0.2
    
    
    
    #print vertex_degree
    
    #g.es['sign'] = np.sign(g)
    
    #
    ###print g
    #ig.plot(g, plot_nbs_adj_mat_file, layout = layout2D.tolist() , vertex_size = vertex_degree,    edge_width = np.array(g.es['weight']), edge_curved = True)
    ig.plot(g, plot_nbs_adj_mat_file, layout = layout2D.tolist() , vertex_size = vertex_degree,    edge_width = 0.01, edge_curved = True)
    
    
    
def plot_igraph_3D_int_mat(int_matrix,coords,plot_nbs_adj_mat_file):
    
    layout2D = project2D_np(coords)
     
    #print layout2D
        
    mod_list = int_matrix.tolist()
    
    #print mod_list
    
    g= ig.Graph.Weighted_Adjacency(mod_list,mode=ig.ADJ_MAX)
    
    vertex_degree = np.array(g.degree())*0.2
    
    
    
    #print vertex_degree
    
    #g.es['sign'] = np.sign(g)
    
    #
    ###print g
    #ig.plot(g, plot_nbs_adj_mat_file, layout = layout2D.tolist() , vertex_size = vertex_degree,    edge_width = np.array(g.es['weight']), edge_curved = True)
    ig.plot(g, plot_nbs_adj_mat_file, layout = layout2D.tolist() , vertex_size = vertex_degree,    edge_width = 0.01, edge_curved = True)
    
    
    
    
def plot_igraph_3D_signed_bin_label_mat(int_matrix,coords,plot_nbs_adj_mat_file,labels = []):
    
    layout2D = project2D_np(coords)
     
    #print layout2D
        
    mod_list = int_matrix.tolist()
    
    #print mod_list
    
    g= ig.Graph.Weighted_Adjacency(mod_list,mode=ig.ADJ_MAX)
    
    print len(labels),len(g.vs)
    
    if len(labels) == len(g.vs):
    
        g.vs['label'] = labels
        
        g.vs['label_size'] = 5
    
    print len(g.es)
    
    if len(g.es) > 0 :
        
        #print g.es['weight']
        
        edge_col = []
        
        for w in g.es['weight']:
            
            #(e0,e1) = e.tuple
            
            #print int(e.weight)
            
            #comp_index = int(e.weight)
            
            if int(w) == -1:
                edge_col.append('green')
            elif int(w) == -2:
                edge_col.append('cyan')
            elif int(w) == -4:
                edge_col.append('darkblue')
            elif int(w) == 1:
                edge_col.append('yellow')
            elif int(w) == 2:
                edge_col.append('orange')
            elif int(w) == 4:
                edge_col.append('red')
                
        
        #g_all.es['names'] = edge_list_names
        #g_all.vs['names'] = node_list_names
        
        g.es['color'] = edge_col
        
        ig.plot(g, plot_nbs_adj_mat_file, layout = layout2D.tolist() , vertex_size = 0.2,    edge_width =  np.array(np.absolute(g.es['weight']))*0.1)
        
    else:
        ig.plot(g, plot_nbs_adj_mat_file, layout = layout2D.tolist() , vertex_size = 0.2,    edge_width =  0.01)
    #print vertex_degree
    
    #g.es['sign'] = np.sign(g)
    
    #
    ###print g
    #ig.plot(g, plot_nbs_adj_mat_file, layout = layout2D.tolist() , vertex_size = vertex_degree,    edge_width = np.array(g.es['weight']), edge_curved = True)
    #ig.plot(g, plot_nbs_adj_mat_file, layout = layout2D.tolist() , vertex_size = vertex_degree,    edge_width = 0.01, edge_curved = True)
    
    
    
def plot_igraph_3D_int_label_mat(int_matrix,coords,plot_nbs_adj_mat_file):
    
    layout2D = project2D_np(coords)
     
    #print layout2D
        
    mod_list = int_matrix.tolist()
    
    #print mod_list
    
    g= ig.Graph.Weighted_Adjacency(mod_list,mode=ig.ADJ_MAX)
    
    
    #print g.es['weight']
    
    edge_col = []
    
    for w in g.es['weight']:
        
        #(e0,e1) = e.tuple
        
        #print int(e.weight)
        
        #comp_index = int(e.weight)
        
        if int(w) < nb_igraph_colors:
            edge_col.append(igraph_colors[int(w)])
            
        else:
            edge_col.append("lightgrey")
            
    
    #g_all.es['names'] = edge_list_names
    #g_all.vs['names'] = node_list_names
    
    g.es['color'] = edge_col
    
    
    
    vertex_degree = np.array(g.degree())*0.2
    
    #print vertex_degree
    
    #g.es['sign'] = np.sign(g)
    
    #
    ###print g
    #ig.plot(g, plot_nbs_adj_mat_file, layout = layout2D.tolist() , vertex_size = vertex_degree,    edge_width = np.array(g.es['weight']), edge_curved = True)
    #ig.plot(g, plot_nbs_adj_mat_file, layout = layout2D.tolist() , vertex_size = vertex_degree,    edge_width = 0.01, edge_curved = True)
    ig.plot(g, plot_nbs_adj_mat_file, layout = layout2D.tolist() , vertex_size = vertex_degree,    edge_width = 0.01)
    
    
    
    
    
    
    
    
    
    
def plot_igraph_3D_adj_mat(adj_matrix,coords,plot_nbs_adj_mat_file):
    
    layout2D = project2D_np(coords_list)
     
    #print layout2D
        
    mod_list = adj_matrix.tolist()
    
    g= ig.Graph.Adjacency(mod_list,mode=ig.ADJ_MAX)
    
    vertex_degree = np.array(g.degree())*0.2
    
    #print vertex_degree
    
    #g.es['sign'] = np.sign(g)
    
    #
    ###print g
    ig.plot(g, plot_nbs_adj_mat_file, layout = layout2D.tolist() , vertex_size = vertex_degree,    edge_width = 0.01, edge_curved = True)
    
def plot_igraph_3D_avg_cor_mat(avg_cor_mat,coords):
    
    #layout2D = project2D(node_coords.tolist(),0,0)
    layout2D = project2D_np(coords)
    
    #print mod_cor_mat
    
    wei_sig_list = avg_cor_mat.tolist()
    
    #print mod_list
    
    g= ig.Graph.Weighted_Adjacency(wei_sig_list,mode=ig.ADJ_MAX)
    
    #print g
    
    #g.es['sign'] = np.sign(g)
    
    
    
    pos_list = g.es.select(weight_gt = 0)
    
    #print pos_list
    
    neg_list = g.es.select(weight_lt = 0)
    
    #pos_list["color"] = 'red'
    neg_list["color"] = 'blue'
    
    
    #pos_list["edge_width"] = 0.01
    neg_list["edge_width"] = 0.01
    
    g.delete_edges(pos_list)
    
    i_graph_file = os.path.abspath('plot_igraph-neg_correl.eps')
    
    
    #g.vs['color'] = igraph_colors[:node_coords.shape[0]]
    
    #vertex_degree = np.array(g.degree())*0.2
    
    
    ###print g
    #ig.plot(g,i_graph_file,layout = layout2D.tolist(),vertex_size = vertex_degree,  edge_width = 0.01, edge_curved = True)
    ig.plot(g,i_graph_file,layout = layout2D.tolist(),vertex_size = 0.1)
    
    
    
    
    return i_graph_file
    
    
    
    
def plot_3D_igraph_weighted_signed_matrix(wei_sig_mat,node_coords):
    
    #layout2D = project2D(node_coords.tolist(),0,0)
    layout2D = project2D_np(node_coords)
    
    #print mod_cor_mat
    
    wei_sig_list = wei_sig_mat.tolist()
    
    #print mod_list
    
    g= ig.Graph.Weighted_Adjacency(wei_sig_list,mode=ig.ADJ_MAX)
    
    #print g
    
    #g.es['sign'] = np.sign(g)
    
    
    
    pos_list = g.es.select(weight_gt = 0)
    
    #print pos_list
    
    neg_list = g.es.select(weight_lt = 0)
    
    pos_list["color"] = 'red'
    neg_list["color"] = 'blue'
    
    
    
    g.vs['color'] = igraph_colors[:node_coords.shape[0]]
    
    i_graph_file = os.path.abspath('plot_weighted_signed_graph.eps')
    
    ###print g
    ig.plot(g,i_graph_file,layout = layout2D.tolist())
    
    return i_graph_file
    
def plot_3D_igraph_modules_net_list(community_vect,node_coords,net_list,gm_mask_coords,labels = []):

    if (community_vect.shape[0] != node_coords.shape[0]):
        print "Warning, community_vect {} != node_coords {}".format(community_vect.shape[0], node_coords.shape[0])
        
    find_in_corres = find_index_in_coords(gm_mask_coords,node_coords)
    
    find_in_gm = find_index_in_coords(node_coords,gm_mask_coords)
    
    
    print np.min(find_in_gm),np.max(find_in_gm),find_in_gm.shape
    
    np_labels = np.array(labels, dtype = 'string')
    
    cur_labels = np_labels[find_in_gm]
    
    print cur_labels
    
    print np.min(find_in_corres),np.max(find_in_corres),find_in_corres.shape
    
    ########### extract edge list (with coords belonging to )
    
    edge_list = []
    
    edge_weights = []
    
    for u,v,w in net_list:
        #print u,v
        if find_in_corres[u-1] != -1 and find_in_corres[v-1] != -1:
        #and u > v:
            
            edge_list.append((find_in_corres[u-1],find_in_corres[v-1]))
            edge_weights.append(w)
            
    node_list_names = map(str,range(len(community_vect)))
    
    layout2D = project2D_np(node_coords)
    
    ###################################################### All modules 
    
    net_list_all_modules_file = os.path.abspath("net_list_all_modules.eps")

    g= ig.Graph(edge_list)
    
    g.es["weight"] = edge_weights
    
    #print g
    
    ######### colors
    
    community_vect[community_vect > len(igraph_colors)-1] = len(igraph_colors)-1
    
    edge_col = []
    
    for e in g.es:
        
        (e0,e1) = e.tuple
        
        if (community_vect[e0] == community_vect[e1]):
            edge_col.append(igraph_colors[community_vect[e0]])
            
        else:
            edge_col.append("lightgrey")
            
    
    vertex_col = []
    
    for i,v in enumerate(g.vs):
        mod_index = community_vect[i]
        if (mod_index != len(igraph_colors)-1):
            vertex_col.append(igraph_colors[mod_index])
        else:
            vertex_col.append("lightgrey")
    
    g.vs['color'] = vertex_col
    
    g.es['color'] = edge_col
    
    g['layout'] = layout2D.tolist()
    
    
    
    if len(cur_labels) == len(g.vs):
    
        print "$$$$$$$$$$$$$$$$ Labels $$$$$$$$$$$$$$$$$$$$$$$$"
        
        g.vs['label'] = cur_labels
        
        g.vs['label_size'] = 5
    
    
    
    ig.plot(g, net_list_all_modules_file, vertex_size = 5, edge_width = 0.01, edge_curved = False)
    #ig.plot(g_all, net_list_all_modules_file, vertex_size = np.array(g_all.degree())*0.2,    edge_width = np.array(edge_weights)*0.1, edge_curved = False)
    
    return net_list_all_modules_file
    
    
def plot_3D_igraph_modules_Z_list(community_vect,node_coords,Z_list,gm_mask_coords):

    if (community_vect.shape[0] != node_coords.shape[0]):
        print "Warning, community_vect {} != node_coords {}".format(community_vect.shape[0], node_coords.shape[0])
        
    find_in_corres = find_index_in_coords(gm_mask_coords,node_coords)
    
    ########### threshoding the number of dictictly displayed modules with the number of igraph colors
    
    community_vect[community_vect > len(igraph_colors)-1] = len(igraph_colors)-1
    
    ########### extract edge list (with coords belonging to )
    
    edge_col_inter = []
    edge_list_inter = []
    edge_weights_inter = []
    
    edge_col_intra = []
    edge_list_intra = []
    edge_weights_intra = []
    
    for u,v,w in Z_list:
        #print u,v
        if find_in_corres[u-1] != -1 and find_in_corres[v-1] != -1:
        #and u > v:
            
            e0 = find_in_corres[u-1]
            e1 = find_in_corres[v-1]
            
            if (community_vect[e0] == community_vect[e1]):
                
                edge_list_intra.append((e0,e1))
                edge_weights_intra.append(w)
                edge_col_intra.append(igraph_colors[community_vect[e0]])
            else:
                
                edge_list_inter.append((e0,e1))
                edge_weights_inter.append(w)
                edge_col_inter.append("lightgrey")
                
            
    layout2D = project2D_np(node_coords)
    
    ###################################################### All modules 
    
    Z_list_all_modules_file = os.path.abspath("Z_list_all_modules.eps")

    edge_list = edge_list_inter + edge_list_intra
    
    edge_weights = edge_weights_inter + edge_weights_intra 
    
    edge_col = edge_col_inter + edge_col_intra
    
    
    g_all= ig.Graph(edge_list)
    
    g_all.es["weight"] = edge_weights
    
    g_all.es['color'] = edge_col
    #print g_all
    
    ######### colors
    
    vertex_col = []
    
    for i,v in enumerate(g_all.vs):
        mod_index = community_vect[i]
        if (mod_index != len(igraph_colors)-1):
            vertex_col.append(igraph_colors[mod_index])
        else:
            vertex_col.append("lightgrey")
    
    g_all.vs['color'] = vertex_col
    
    g_all['layout'] = layout2D.tolist()
    
    ig.plot(g_all, Z_list_all_modules_file, vertex_size = np.array(g_all.degree())*0.5,    edge_width = np.array(edge_weights)*0.001, edge_curved = False)
    
    return Z_list_all_modules_file
    
    
    
#def plot_3D_igraph_modules_Z_list(community_vect,node_coords,Z_list,gm_mask_coords):

    #if (community_vect.shape[0] != node_coords.shape[0]):
        #print "Warning, community_vect {} != node_coords {}".format(community_vect.shape[0], node_coords.shape[0])
        
    #find_in_corres = find_index_in_coords(gm_mask_coords,node_coords)
    
    ############ extract edge list (with coords belonging to )
    
    #edge_list = []
    
    #edge_weights = []
    
    #for u,v,w in Z_list:
        ##print u,v
        #if find_in_corres[u-1] != -1 and find_in_corres[v-1] != -1:
        ##and u > v:
            
            #edge_list.append((find_in_corres[u-1],find_in_corres[v-1]))
            #edge_weights.append(w)
            
    #layout2D = project2D_np(node_coords)
    
    ####################################################### All modules 
    
    #Z_list_all_modules_file = os.path.abspath("Z_list_all_modules.eps")

    #g_all= ig.Graph(edge_list)
    
    #g_all.es["weight"] = edge_weights
    
    ##print g_all
    
    ########## colors
    
    #community_vect[community_vect > len(igraph_colors)-1] = len(igraph_colors)-1
    
    #edge_col = []
    
    #edge_col
    
    #for e in g_all.es:
        
        #(e0,e1) = e.tuple
        
        #if (community_vect[e0] == community_vect[e1]):
            #edge_col.append(igraph_colors[community_vect[e0]])
            
        #else:
            #edge_col.append("lightgrey")
            
    
    #vertex_col = []
    
    #for i,v in enumerate(g_all.vs):
        #mod_index = community_vect[i]
        #if (mod_index != len(igraph_colors)-1):
            #vertex_col.append(igraph_colors[mod_index])
        #else:
            #vertex_col.append("lightgrey")
    
    #g_all.vs['color'] = vertex_col
    
    #g_all.es['color'] = edge_col
    
    #g_all['layout'] = layout2D.tolist()
    
    #ig.plot(g_all, Z_list_all_modules_file, vertex_size = np.array(g_all.degree())*0.5,    edge_width = np.array(edge_weights)*0.001, edge_curved = False)
    
    #return Z_list_all_modules_file
    
     ######################################## igraph + cairo #######################################

def project2D_cairo(layout, alpha, beta):
    '''
    This method will project a set of points in 3D to 2D based on the given
    angles alpha and beta.
    '''
    # Calculate the rotation matrices based on the given angles.
    c = numpy.matrix([[1, 0, 0], [0, numpy.cos(alpha), numpy.sin(alpha)], [0, -numpy.sin(alpha), numpy.cos(alpha)]])
    c = c * numpy.matrix([[numpy.cos(beta), 0, -numpy.sin(beta)], [0, 1, 0], [numpy.sin(beta), 0, numpy.cos(beta)]])
    b = numpy.matrix([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
    # Hit the layout, rotate, and kill a dimension
    layout = numpy.matrix(layout)
    X = (b * (c * layout.transpose())).transpose()
    return [[X[i,0],X[i,1],X[i,2]] for i in range(X.shape[0])]
    
def drawGraph3D(graph, layout, angle, fileName):
    '''
    Draw a graph in 3D with the given layout, angle, and filename.
    '''
    # Setup some vertex attributes and calculate the projection
    graph.vs['degree'] = graph.degree()
    vertexRadius = (0.9 * 0.9) / np.sqrt(graph.vcount())
    
    print zip(*layout)
    
    graph.vs['x3'], graph.vs['y3'], graph.vs['z3'] = zip(*layout)
    layout2D = project2D_cairo(layout, angle[0], angle[1])
    graph.vs['x2'], graph.vs['y2'], graph.vs['z2'] = zip(*layout2D)
    minX, maxX = min(graph.vs['x2']), max(graph.vs['x2'])
    minY, maxY = min(graph.vs['y2']), max(graph.vs['y2'])
    minZ, maxZ = min(graph.vs['z2']), max(graph.vs['z2'])
    # Calculate the draw order. This is important if we want this to look
    # realistically 3D.
    zVal, zOrder = zip(*sorted(zip(graph.vs['z3'], range(graph.vcount()))))
    # Setup the ca surface
    surf = ca.ImageSurface(ca.FORMAT_ARGB32, 1280, 800)
    con = ca.Context(surf)
    con.scale(1280.0, 800.0)
    # Draw the background
    #con.set_source_rgba(0.0, 0.0, 0.0, 1.0)
    con.set_source_rgb(1.0, 1.0, 1.0)
    
    con.rectangle(0.0, 0.0, 1.0, 1.0)
    con.fill()
    # Draw the edges without respect to z-order but set their alpha along
    # a linear gradient to represent depth.
    for e in graph.get_edgelist():
    # Get the first vertex info
        v0 = graph.vs[e[0]]
        x0 = (v0['x2'] - minX) / (maxX - minX)
        y0 = (v0['y2'] - minY) / (maxY - minY)
        alpha0 = (v0['z2'] - minZ) / (maxZ - minZ)
        alpha0 = max(0.1, alpha0)
        # Get the second vertex info
        v1 = graph.vs[e[1]]
        x1 = (v1['x2'] - minX) / (maxX - minX)
        y1 = (v1['y2'] - minY) / (maxY - minY)
        alpha1 = (v1['z2'] - minZ) / (maxZ - minZ)  
        alpha1 = max(0.1, alpha1)
        
        # Setup the pattern info
        pat = ca.LinearGradient(x0, y0, x1, y1)
        
        pat.add_color_stop_rgba(0, 1, 0.0, 0.0, alpha0 / 6.0)
        pat.add_color_stop_rgba(1, 1, 1.0, 1.0, alpha1 / 6.0)
        #pat.add_color_stop_rgba(0, 1, 1.0, 1.0, alpha0 / 6.0)
        #pat.add_color_stop_rgba(1, 1, 1.0, 1.0, alpha1 / 6.0)
        
        con.set_source(pat)
        # Draw the line
        con.set_line_width(vertexRadius / 4.0)
        con.move_to(x0, y0) 
        con.line_to(x1, y1)
        con.stroke()
    # Draw vertices in z-order
    vert_degree = graph.degree()
    max_deg = np.max(vert_degree)
    
    for i in zOrder:
        v = graph.vs[i]
        alpha = (v['z2'] - minZ) / (maxZ - minZ)
        alpha = max(0.1, alpha)
        radius = vert_degree[i]/max_deg * vertexRadius
        #vertexRadius
        x = (v['x2'] - minX) / (maxX - minX)
        y = (v['y2'] - minY) / (maxY - minY)
        # Setup the radial pattern for 3D lighting effect
        pat = ca.RadialGradient(x, y, radius / 4.0, x, y, radius)
        pat.add_color_stop_rgba(0, alpha, 0, 0, 1)
        pat.add_color_stop_rgba(1, 0, 0, 0, 1)
        con.set_source(pat)
        # Draw the vertex sphere
        con.move_to(x, y)
        con.arc(x, y, radius, 0, 2 * np.pi)  
        con.fill()
    # Output the surface
    surf.write_to_png(fileName)
    
         
def plot_cairo_3D_adj_mat(signif_adj_matrix,gm_mask_coords_list,plot_nbs_adj_mat_file):
    
    mod_list = signif_adj_matrix.tolist()
    
    g= ig.Graph.Adjacency(mod_list,mode=ig.ADJ_MAX)
    
    #print g.degree()
    
    #g.es['sign'] = np.sign(g)
    
    #
    
    drawGraph3D(g, gm_mask_coords_list, (30, 60), plot_nbs_adj_mat_file)
    ###print g
    
    #ig.plot(g, plot_nbs_adj_mat_file, layout = gm_mask_coords_list, vertex_size = g.degree())
    