// ==UserScript==
// @name         bilibilibackground
// @namespace    http://tampermonkey.net/
// @version      3.0
// @description  更换bilibili的背景图片
// @author       -墓场-

// @match        https://www.bilibili.com
// @match        https://www.bilibili.com/?spm_id_from=*
// @match        https://www.bilibili.com/v/popular/*

// @icon         https://raw.githubusercontent.com/Jacken-Wu/hello-world/main/biliBackground/icon48.png
// @grant        none
// ==/UserScript==

var css = `
.bili-header__banner{
background-image: url(https://raw.githubusercontent.com/Jacken-Wu/hello-world/main/biliBackground/bilibiliHead.jpg) !important;
max-height: 380px !important;
height: 380px !important;
}
.bili-header__bar{background: linear-gradient(rgb(100, 200, 255, 1), rgb(100, 200, 255, 0)) !important}
.bili-header__channel{
height: 20px !important;
top: -55px;
background-color: rgb(255, 255, 255, 0) !important;
}
a.channel-link{background-color: rgb(255, 162, 162, 0.65) !important;}
#channel-entry-more{background-color: rgb(255, 162, 162, 0.65) !important;}
div.channel-icons{
background-color: rgb(162, 210, 255, 0.35);
border-radius: 7px;
padding: 7px;
}
div.channel-items__right{
background-color: rgb(162, 210, 255, 0.35);
border-radius: 7px;
padding: 7px;
}
`;

(() => {
    var style = document.createElement("style");
    style.innerText = css;
    document.head.appendChild(style);

    setTimeout(() => {
        document.getElementsByClassName('bili-header__banner')[0].innerHTML = "";

        var ad = document.getElementsByClassName("recommended-swipe")[0];
        ad.remove();
    }, 1000);


    const checkMarginTop = () => {

        document.querySelectorAll('.recommended-container_floor-aside .container.is-version8>*:nth-of-type(n + 8)').forEach(a => {
            a.style.marginTop = "0";
        });
        document.querySelectorAll('.recommended-container_floor-aside .container.is-version8>*:nth-of-type(n + 13)').forEach(a => {
            a.style.marginTop = "0";
        });
    };

    checkMarginTop();

    const observer = new MutationObserver(checkMarginTop);
    observer.observe(document.body, { childList: true, subtree: true });
})();

