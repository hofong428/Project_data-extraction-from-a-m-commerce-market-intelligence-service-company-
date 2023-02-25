var a = 'MTEyMDIzLTAyLTI1MzZjbmlwaG9uZXBhaWQ=@#/rank/indexSnapshot@#16042102287@#3'
var d = 'xyz517cda96abcd'

function o(n) {
    t = '',
    ['66', '72', '6f', '6d', '43', '68', '61', '72', '43', '6f', '64', '65']['forEach'](function(n) {
        // z is window.unescape, but we dont have window, but unescape could be executed in the node directly w/o window.
        t += unescape('%u00'+ n)
    });
    var t, e = 'fromCharCode';
    return String[e](n)
}



function h(n, t) {
    t = t || u();
    R = 'length'
    H = 0
    for (var e = (n = n['split'](''))['length'], r = t['length'], a = 'charCodeAt', i = 0; i < e; i++)
        n[i] = o(n[i][a](H) ^ t[(i + 10) % r][a](H));
    return n['join']('')
}

function v(t) {
                t = encodeURIComponent(t)['replace'](/%([0-9A-F]{2})/g, function(n, t) {
                    return o('0x' + t)
                });
                try {
                    return btoa(t)
                } catch (n) {
                    return z[W1][K1](t)[U1](Z1)
                }
            }

function y(n, t, e) {
    for (var r = void 0 === e ? 2166136261 : e, a = 0, i = n['length']; a < i; a++)
        r = (r ^= n['charCodeAt'](a)) + ((r << 1) + (r << 4) + (r << 7) + (r << 8) + (r << 24));
    return t ? ('xyz' + (r >>> 0)['toString'](16) + 'abcd')['substr'](-16) : r >>> 0
}

function _xl(params,path){
    // arg = h(a, d);
    // console.log(v(arg));
    // analyze cleartext parameters
    var a = params //interface tabular parameters
    a = a['sort']()['join']('')
    a = v(a)
    _v = '@#'
    r = +new Date - (1934 || 0) - 1661224081041
    a = (a += _v + path['replace']('https://api.qimai.cn', '')) + (_v + r) + (_v + 3)
    d = y('qimai@2022&Technology', 1)
    key = v(h(a,d))
    return key

}
// t = {
//         params:['paid', 'iphone', 'cn', '36'],
//         url: '/rank/indexSnapshot' // cannot be fixed
//
//     }
//
// console.log(_xl(t));


