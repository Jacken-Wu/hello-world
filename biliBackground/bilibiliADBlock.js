// ==UserScript==
// @name         bilibiliADBlock
// @namespace    http://tampermonkey.net/
// @version      1.0
// @description  删除bilibili首页广告
// @author       -墓场-

// @match        https://www.bilibili.com
// @match        https://www.bilibili.com/?spm_id_from=*
// @match        https://www.bilibili.com/v/popular/*

// @icon         https://raw.githubusercontent.com/Jacken-Wu/hello-world/main/biliBackground/icon48.png
// @grant        none
// ==/UserScript==

(() => {
    const checkAndRemove = () => {
        document.querySelectorAll('div.feed-card').forEach(a => {
            const b = a.querySelector('div.bili-video-card.is-rcmd');
            if (b && !b.classList.contains('enable-no-interest')) {
                console.log(a, 'removed');
                a.style.display = "none";
            }
        });
        document.querySelectorAll('div.bili-feed-card').forEach(a => {
            const b = a.querySelector('div.bili-video-card.is-rcmd');
            if (b && !b.classList.contains('enable-no-interest')) {
                console.log(a, 'removed');
                a.style.display = "none";
            }
        });
    };

    checkAndRemove();

    const observer = new MutationObserver(checkAndRemove);
    observer.observe(document.body, { childList: true, subtree: true });
})();
