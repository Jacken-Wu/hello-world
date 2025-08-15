// ==UserScript==
// @name         BarrageAutoBlock
// @namespace    http://tampermonkey.net/
// @version      1.0
// @description  按照视频的 tag 自动控制弹幕开关
// @author       -墓场-

// @match        https://www.bilibili.com/video/*

// @icon         https://raw.githubusercontent.com/Jacken-Wu/hello-world/main/biliBackground/icon48.png
// @grant        none
// ==/UserScript==

const banTags = ['初音', '初音未来', 'miku', '初音ミク', 'VOCALOID', 'Vocaloid', 'teto', '重音', '镜音リン', '镜音レン', '鏡音リン・レン', '魔术', '重音テト', '重音'];

const observer = new MutationObserver(mutations => {
    const disableButtom = document.querySelector('.bui-danmaku-switch-input');
    if (disableButtom) {
        const tagList = document.querySelectorAll('.tag.not-btn-tag');
        let isNeedBan = false;
        tagList.forEach(tag => {
            const tagName = tag.querySelector('.tag-link').textContent;
            if (banTags.includes(tagName)) {
                isNeedBan = true;
            }
        });
        const disabledInputBox = document.querySelector('.bpx-player-dm-setting.disabled');
        if (isNeedBan) {
            if (disabledInputBox == null) {
                disableButtom.click();
                console.log('关闭弹幕');
            }
        } else {
            if (disabledInputBox) {
                disableButtom.click();
                console.log('开启弹幕');
            }
        }
        // 执行操作后断开监听
        observer.disconnect();
    }
});
observer.observe(document.body, { childList: true, subtree: true });

const observerComment = new MutationObserver(mutations => {
    const tagList = document.querySelectorAll('.tag.not-btn-tag');
    let isNeedBan = false;
    tagList.forEach(tag => {
        const tagName = tag.querySelector('.tag-link').textContent;
        if (banTags.includes(tagName)) {
            isNeedBan = true;
        }
    });
    if (isNeedBan) {
        commentDiv.remove();
        console.log('屏蔽评论区');
    }
    // 执行操作后断开监听
    observerComment.disconnect();
});
const commentDiv = document.querySelector('#commentapp');
observerComment.observe(commentDiv, { childList: true, subtree: true });
