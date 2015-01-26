#-*- coding:utf-8 -*-
from pyquery import PyQuery as pq

s = """
<div class="row">
    <div class="image-item column one">
        <div class="wr">
            <a class="img" href="/wallpapers/view/id/42441" title="Обои&nbsp;Зеленое поле для гольфа">
                <img src="http://img.mota.ru/upload/wallpapers/2014/12/25/20/01/42441/074-preview-thumb.jpg?v=1" width="300" height="225" alt="Обои&nbsp;Зеленое поле для гольфа">
            </a>
            <div class="inf-pad" style="display: none;">
                <p class="fll">
                    <a href="/wallpapers/view/id/42441">
                        1920x1080                    </a>
                </p>
                <p class="flr">
                    <a href="/categories/view/name/nature">
                        Природа                    </a>
                </p>
            </div>
        </div>
    </div>
    <div class="image-item column one">
        <div class="wr">
            <a class="img" href="/wallpapers/view/id/42426" title="Обои&nbsp;Пещера на морском берегу">
                <img src="http://img.mota.ru/upload/wallpapers/2014/12/25/20/01/42426/059-preview-thumb.jpg?v=1" width="300" height="225" alt="Обои&nbsp;Пещера на морском берегу">
            </a>
            <div class="inf-pad" style="display: none;">
                <p class="fll">
                    <a href="/wallpapers/view/id/42426">
                        1920x1080                    </a>
                </p>
                <p class="flr">
                    <a href="/categories/view/name/nature">
                        Природа                    </a>
                </p>
            </div>
        </div>
    </div>
    <div class="image-item column one">
        <div class="wr">
            <a class="img" href="/wallpapers/view/id/42427" title="Обои&nbsp;Звездное небо над скалами">
                <img src="http://img.mota.ru/upload/wallpapers/2014/12/25/20/01/42427/060-preview-thumb.jpg?v=1" width="300" height="225" alt="Обои&nbsp;Звездное небо над скалами">
            </a>
            <div class="inf-pad" style="display: none;">
                <p class="fll">
                    <a href="/wallpapers/view/id/42427">
                        1920x1080                    </a>
                </p>
                <p class="flr">
                    <a href="/categories/view/name/nature">
                        Природа                    </a>
                </p>
            </div>
        </div>
    </div>
    <div class="image-item column one">
        <div class="wr">
            <a class="img" href="/wallpapers/view/id/42428" title="Обои&nbsp;Белый песок и голубое небо">
                <img src="http://img.mota.ru/upload/wallpapers/2014/12/25/20/01/42428/061-preview-thumb.jpg?v=1" width="300" height="225" alt="Обои&nbsp;Белый песок и голубое небо">
            </a>
            <div class="inf-pad" style="display: none;">
                <p class="fll">
                    <a href="/wallpapers/view/id/42428">
                        1920x1080                    </a>
                </p>
                <p class="flr">
                    <a href="/categories/view/name/nature">
                        Природа                    </a>
                </p>
            </div>
        </div>
    </div>
    <div class="image-item column one">
        <div class="wr">
            <a class="img" href="/wallpapers/view/id/42431" title="Обои&nbsp;Sky Lanterns: Amy">
                <img src="http://img.mota.ru/upload/wallpapers/2014/12/25/20/01/42431/064-preview-thumb.jpg?v=1" width="300" height="225" alt="Обои&nbsp;Sky Lanterns: Amy">
            </a>
            <div class="inf-pad" style="display: none;">
                <p class="fll">
                    <a href="/wallpapers/view/id/42431">
                        1920x1080                    </a>
                </p>
                <p class="flr">
                    <a href="/categories/view/name/anime">
                        Аниме                    </a>
                </p>
            </div>
        </div>
    </div>
    <div class="image-item column one">
        <div class="wr">
            <a class="img" href="/wallpapers/view/id/42433" title="Обои&nbsp;Замок на закате">
                <img src="http://img.mota.ru/upload/wallpapers/2014/12/25/20/01/42433/066-preview-thumb.jpg?v=1" width="300" height="225" alt="Обои&nbsp;Замок на закате">
            </a>
            <div class="inf-pad" style="display: none;">
                <p class="fll">
                    <a href="/wallpapers/view/id/42433">
                        1920x1080                    </a>
                </p>
                <p class="flr">
                    <a href="/categories/view/name/nature">
                        Природа                    </a>
                </p>
            </div>
        </div>
    </div>
    <div class="image-item column one">
        <div class="wr">
            <a class="img" href="/wallpapers/view/id/42439" title="Обои&nbsp;Дорога к горам">
                <img src="http://img.mota.ru/upload/wallpapers/2014/12/25/20/01/42439/072-preview-thumb.jpg?v=1" width="300" height="225" alt="Обои&nbsp;Дорога к горам">
            </a>
            <div class="inf-pad">
                <p class="fll">
                    <a href="/wallpapers/view/id/42439">
                        1920x1080                    </a>
                </p>
                <p class="flr">
                    <a href="/categories/view/name/nature">
                        Природа                    </a>
                </p>
            </div>
        </div>
    </div>
    <div class="image-item column one">
        <div class="wr">
            <a class="img" href="/wallpapers/view/id/42416" title="Обои&nbsp;Бутик-отель Island Hideaway, Мальдивы">
                <img src="http://img.mota.ru/upload/wallpapers/2014/12/25/20/01/42416/049-preview-thumb.jpg?v=1" width="300" height="225" alt="Обои&nbsp;Бутик-отель Island Hideaway, Мальдивы">
            </a>
            <div class="inf-pad" style="display: none;">
                <p class="fll">
                    <a href="/wallpapers/view/id/42416">
                        1920x1080                    </a>
                </p>
                <p class="flr">
                    <a href="/categories/view/name/nature">
                        Природа                    </a>
                </p>
            </div>
        </div>
    </div>
    <div class="image-item column one">
        <div class="wr">
            <a class="img" href="/wallpapers/view/id/42417" title="Обои&nbsp;Морской пейзаж Чинкве-Терре, Италия">
                <img src="http://img.mota.ru/upload/wallpapers/2014/12/25/20/01/42417/050-preview-thumb.jpg?v=1" width="300" height="225" alt="Обои&nbsp;Морской пейзаж Чинкве-Терре, Италия">
            </a>
            <div class="inf-pad">
                <p class="fll">
                    <a href="/wallpapers/view/id/42417">
                        1920x1080                    </a>
                </p>
                <p class="flr">
                    <a href="/categories/view/name/italy">
                        Италия                    </a>
                </p>
            </div>
        </div>
    </div>
    <div class="image-item column one">
        <div class="wr">
            <a class="img" href="/wallpapers/view/id/42418" title="Обои&nbsp;Горы в сумерках">
                <img src="http://img.mota.ru/upload/wallpapers/2014/12/25/20/01/42418/051-preview-thumb.jpg?v=1" width="300" height="225" alt="Обои&nbsp;Горы в сумерках">
            </a>
            <div class="inf-pad" style="display: none;">
                <p class="fll">
                    <a href="/wallpapers/view/id/42418">
                        1920x1080                    </a>
                </p>
                <p class="flr">
                    <a href="/categories/view/name/nature">
                        Природа                    </a>
                </p>
            </div>
        </div>
    </div>
    <div class="image-item column one">
        <div class="wr">
            <a class="img" href="/wallpapers/view/id/42422" title="Обои&nbsp;Луна над Амстердамом, Нидерланды">
                <img src="http://img.mota.ru/upload/wallpapers/2014/12/25/20/01/42422/055-preview-thumb.jpg?v=1" width="300" height="225" alt="Обои&nbsp;Луна над Амстердамом, Нидерланды">
            </a>
            <div class="inf-pad" style="display: none;">
                <p class="fll">
                    <a href="/wallpapers/view/id/42422">
                        1920x1080                    </a>
                </p>
                <p class="flr">
                    <a href="/categories/view/name/netherlands">
                        Нидерланды                    </a>
                </p>
            </div>
        </div>
    </div>
    <div class="image-item column one">
        <div class="wr">
            <a class="img" href="/wallpapers/view/id/42425" title="Обои&nbsp;Ледники Аляски">
                <img src="http://img.mota.ru/upload/wallpapers/2014/12/25/20/01/42425/058-preview-thumb.jpg?v=1" width="300" height="225" alt="Обои&nbsp;Ледники Аляски">
            </a>
            <div class="inf-pad">
                <p class="fll">
                    <a href="/wallpapers/view/id/42425">
                        1920x1080                    </a>
                </p>
                <p class="flr">
                    <a href="/categories/view/name/nature">
                        Природа                    </a>
                </p>
            </div>
        </div>
    </div>
    <div class="image-item column one">
        <div class="wr">
            <a class="img" href="/wallpapers/view/id/42396" title="Обои&nbsp;Новогодняя елка на пирсе">
                <img src="http://img.mota.ru/upload/wallpapers/2014/12/25/20/01/42396/029-preview-thumb.jpg?v=1" width="300" height="225" alt="Обои&nbsp;Новогодняя елка на пирсе">
            </a>
            <div class="inf-pad" style="display: none;">
                <p class="fll">
                    <a href="/wallpapers/view/id/42396">
                        1920x1080                    </a>
                </p>
                <p class="flr">
                    <a href="/categories/view/name/ny">
                        Новый год и Рождество                    </a>
                </p>
            </div>
        </div>
    </div>
    <div class="image-item column one">
        <div class="wr">
            <a class="img" href="/wallpapers/view/id/42400" title="Обои&nbsp;Пляжная сумка и шляпа на берегу">
                <img src="http://img.mota.ru/upload/wallpapers/2014/12/25/20/01/42400/033-preview-thumb.jpg?v=1" width="300" height="225" alt="Обои&nbsp;Пляжная сумка и шляпа на берегу">
            </a>
            <div class="inf-pad" style="display: none;">
                <p class="fll">
                    <a href="/wallpapers/view/id/42400">
                        1920x1080                    </a>
                </p>
                <p class="flr">
                    <a href="/categories/view/name/nature">
                        Природа                    </a>
                </p>
            </div>
        </div>
    </div>
    <div class="image-item column one">
        <div class="wr">
            <a class="img" href="/wallpapers/view/id/42404" title="Обои&nbsp;Мечеть в Абу-Даби, ОАЭ">
                <img src="http://img.mota.ru/upload/wallpapers/2014/12/25/20/01/42404/037-preview-thumb.jpg?v=1" width="300" height="225" alt="Обои&nbsp;Мечеть в Абу-Даби, ОАЭ">
            </a>
            <div class="inf-pad">
                <p class="fll">
                    <a href="/wallpapers/view/id/42404">
                        1920x1080                    </a>
                </p>
                <p class="flr">
                    <a href="/categories/view/name/UAE">
                        Объединённые Арабские Эмираты                    </a>
                </p>
            </div>
        </div>
    </div>
</div>

"""

d = pq(s)
for i in d("div.image-item").items():
    print i("a.img").attr("href")


