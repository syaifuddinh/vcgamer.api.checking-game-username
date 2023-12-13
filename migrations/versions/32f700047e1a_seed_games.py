"""seed_games

Revision ID: 32f700047e1a
Revises: 3e9959a0f4cb
Create Date: 2023-12-07 11:42:59.417361

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '32f700047e1a'
down_revision: Union[str, None] = '3e9959a0f4cb'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
	op.execute('''
		INSERT INTO public."MTGame" (name, "thumbnailUrl", slug) VALUES('Mobile Legends', 'https://cdn1.codashop.com/S/content/mobile/images/product-tiles/MLBB-Next-tile_sept23.jpg', 'mobile-legends');
		INSERT INTO public."MTGame" (name, "thumbnailUrl", slug) VALUES('PUBG Mobile', 'https://cdn1.codashop.com/S/content/mobile/images/product-tiles/pubgm_rps_tile.jpg', 'pubg-mobile');
		INSERT INTO public."MTGame" (name, "thumbnailUrl", slug) VALUES('Valorant', 'https://cdn1.codashop.com/S/content/common/images/mno/VALORANT_Coda_640x241.jpg', 'valorant');
		INSERT INTO public."MTGame" (name, "thumbnailUrl", slug) VALUES('Ragnarok Eternal Love', 'https://cdn1.codashop.com/S/content/common/images/mno/ragnarok_640.jpg', 'ragnarok-eternal-love');
		INSERT INTO public."MTGame" (name, "thumbnailUrl", slug) VALUES('Point Blank Beyonds Limit', 'https://cdn1.codashop.com/S/content/common/images/mno/PBID_Coda_Asset_Product_640X241.jpg', 'point-blank-beyonds-limit');
		INSERT INTO public."MTGame" (name, "thumbnailUrl", slug) VALUES('Genshin Impact', 'https://cdn1.codashop.com/S/content/common/images/mno/Genshin%20Impact%20V4.1%20Update%20.png', 'genshin-impact');
		INSERT INTO public."MTGame" (name, "thumbnailUrl", slug) VALUES('Dragon Raja', 'https://cdn1.codashop.com/S/content/common/images/mno/DragonRaja_640x241.png', 'dragon-raja');
		INSERT INTO public."MTGame" (name, "thumbnailUrl", slug) VALUES('Arena of Valor', 'https://cdn1.codashop.com/S/content/common/images/mno/aov_640x241.png', 'arena-of-valor');
		INSERT INTO public."MTGame" (name, "thumbnailUrl", slug) VALUES('Clash of Clans', 'https://cdn1.codashop.com/S/content/common/images/mno/logo_clashofclans_evergreen_640x241.png', 'clash-of-clans');
		INSERT INTO public."MTGame" (name, "thumbnailUrl", slug) VALUES('Call of Duty Mobile', 'https://cdn1.codashop.com/S/content/common/images/mno/codmobile2_640x241.jpg', 'call-of-duty-mobile');
		INSERT INTO public."MTGame" (name, "thumbnailUrl", slug) VALUES('Hay Day', 'https://cdn1.codashop.com/S/content/common/images/mno/HayDay_BG_640x241_2023.png', 'hay-day');
		INSERT INTO public."MTGame" (name, "thumbnailUrl", slug) VALUES('Honkai Impact 3', 'https://cdn1.codashop.com/S/content/common/images/mno/honkaiimpact3_640x241.png', 'honkai-impact-3');
		INSERT INTO public."MTGame" (name, "thumbnailUrl", slug) VALUES('Life After', 'https://cdn1.codashop.com/S/content/common/images/mno/LifeAfter-New-Product-Page-Banner-Optimization.jpg', 'life-after');
		INSERT INTO public."MTGame" (name, "thumbnailUrl", slug) VALUES('Light of Thel', 'https://cdn.unipin.com/images/icon_product_pages/1684142367-icon-200+%C2%A6+%C2%A6.jpg', 'light-of-thel');
		INSERT INTO public."MTGame" (name, "thumbnailUrl", slug) VALUES('League of Legends: Wild Rift', 'https://cdn1.codashop.com/S/content/common/images/mno/LoL_banner_640x241.png', 'league-of-legends-wild-rift');
		INSERT INTO public."MTGame" (name, "thumbnailUrl", slug) VALUES('Lords Mobile', 'https://img-cdn.shareitpay.in/shoplay365/prod/upload/app-logo/img_220210820075932120.png', 'lords-mobile');
		INSERT INTO public."MTGame" (name, "thumbnailUrl", slug) VALUES('Omega Legends', 'https://cdn.unipin.com/images/icon_product_pages/1612923604-icon-Omega-Legends-2-200x200.jpg', 'omega-legends');
		INSERT INTO public."MTGame" (name, "thumbnailUrl", slug) VALUES('One punch Man The Strongest', 'https://cdn1.codashop.com/S/content/common/images/mno/omp_new.jpg', 'one-punch-man-the-strongest');
		INSERT INTO public."MTGame" (name, "thumbnailUrl", slug) VALUES('Zepeto', 'https://cdn1.codashop.com/S/content/common/images/mno/Zepeto-newBanner_640x241.png', 'zepeto');
		INSERT INTO public."MTGame" (name, "thumbnailUrl", slug) VALUES('Free Fire', 'https://cdn1.codashop.com/S/content/common/images/mno/freefire_new_640x241.jpg', 'free-fire');
		INSERT INTO public."MTGame" (name, "thumbnailUrl", slug) VALUES('Ragnarok X Generation', 'https://cdn1.codashop.com/S/content/common/images/mno/ragnarok_x_640x241.jpg', 'ragnarok-x-generation');
		INSERT INTO public."MTGame" (name, "thumbnailUrl", slug) VALUES('Sausage Man', 'https://cdn1.codashop.com/S/content/common/images/mno/sausage-man-banner.jpg', 'sausage-man');
		INSERT INTO public."MTGame" (name, "thumbnailUrl", slug) VALUES('Super Sus', 'https://cdn1.codashop.com/S/content/common/images/mno/Super%20Sus_Banner.png', 'super-sus');
		INSERT INTO public."MTGame" (name, "thumbnailUrl", slug) VALUES('Tower of Fantasy', 'https://cdn.unipin.com/images/icon_product_pages/1663645620-icon-1662619195-icon-1662082730-icon-Tower%20of%20Fantasy%20logo%20-%201%20jpg.jpg', 'tower-of-fantasy');
		INSERT INTO public."MTGame" (name, "thumbnailUrl", slug) VALUES('Ludo Club', 'https://cdn1.codashop.com/S/content/common/images/mno/ludoclub_banner640x241.png', 'ludo-club');
		INSERT INTO public."MTGame" (name, "thumbnailUrl", slug) VALUES('Era of Celestials', 'https://cdn1.codashop.com/S/content/common/images/mno/eraofcelestials_640x241.jpg’', 'era-of-celestials');
		INSERT INTO public."MTGame" (name, "thumbnailUrl", slug) VALUES('Revelation Infinite Journey', 'https://cdn1.codashop.com/S/content/common/images/mno/Revelation_PH_ID.png', 'revelation-infinite-journey');
		INSERT INTO public."MTGame" (name, "thumbnailUrl", slug) VALUES('Marvel Snap', 'https://cdn1.codashop.com/S/content/common/images/mno/Marvel-Product-Page-Banner.png', 'marvel-snap');
		INSERT INTO public."MTGame" (name, "thumbnailUrl", slug) VALUES('Ace Racer', 'https://cdn.unipin.com/images/icon_product_pages/1678934346-icon-20kb-.jpg', 'ace-racer');
		INSERT INTO public."MTGame" (name, "thumbnailUrl", slug) VALUES('Stumble Guys', 'https://cdn1.codashop.com/S/content/common/images/mno/Stumble_Guys_Page_Banner.png', 'stumble-guys');
		INSERT INTO public."MTGame" (name, "thumbnailUrl", slug) VALUES('Goddess of Victory: Nikke', 'https://cdn.unipin.com/images/icon_product_pages/1667549693-icon-nikke.jpg', 'goddess-of-victory-nikke');
		INSERT INTO public."MTGame" (name, "thumbnailUrl", slug) VALUES('Clash Royale', 'https://cdn1.codashop.com/S/content/common/images/mno/ClashRoyale_Banner_640x241.png', 'clash-royale');
		INSERT INTO public."MTGame" (name, "thumbnailUrl", slug) VALUES('Brawl Stars', 'https://cdn1.codashop.com/S/content/common/images/mno/Brawl_Banner640x241.png', 'brawl-stars');
		INSERT INTO public."MTGame" (name, "thumbnailUrl", slug) VALUES('Undawn', 'https://cdn1.codashop.com/S/content/common/images/mno/Garena-Undawn_product-page-banner.jpg', 'undawn');
		INSERT INTO public."MTGame" (name, "thumbnailUrl", slug) VALUES('Honkai Star Rail', 'https://cdn1.codashop.com/S/content/common/images/mno/Garena-Undawn_product-page-banner.jpg', 'honkai-star-rail');
		INSERT INTO public."MTGame" (name, "thumbnailUrl", slug) VALUES('Metal Slug Awakening', 'https://cdn1.codashop.com/S/content/common/images/mno/metal_slug_pp-banner.png', 'metal-slug-awakening');
		INSERT INTO public."MTGame" (name, "thumbnailUrl", slug) VALUES('Eggy Party', 'https://cdn1.codashop.com/S/content/common/images/mno/eggyparty_banner640x241.png', 'eggy-party');
		INSERT INTO public."MTGame" (name, "thumbnailUrl", slug) VALUES('EA SPORTS FC', 'https://cdn1.codashop.com/S/content/common/images/mno/640X241_product-banner.jpeg', 'ea-sports-fc');
		INSERT INTO public."MTGame" (name, "thumbnailUrl", slug) VALUES('Farlight 84', 'https://cdn1.codashop.com/S/content/common/images/mno/farlight84_640x241.jpeg', 'farlight-84');
		INSERT INTO public."MTGame" (name, "thumbnailUrl", slug) VALUES('Kings Choice', 'https://cdn1.codashop.com/S/content/common/images/mno/kings_choicebanner.png', 'kings-choice');
		INSERT INTO public."MTGame" (name, "thumbnailUrl", slug) VALUES('Among Heroes: Fantasy Samkok', 'https://cdn1.codashop.com/S/content/common/images/mno/among-heroes-banner.png', 'among-heroes-fantasy-samkok');
		INSERT INTO public."MTGame" (name, "thumbnailUrl", slug) VALUES('Dynasty Warriors: Overlords', 'https://cdn1.codashop.com/S/content/common/images/mno/DWO_640x241.jpg', 'dynasty-warriors-overlords');
		INSERT INTO public."MTGame" (name, "thumbnailUrl", slug) VALUES('Jade Legends', 'https://cdn1.codashop.com/S/content/common/images/mno/jadelegend.jpeg', 'jade-legends');
		INSERT INTO public."MTGame" (name, "thumbnailUrl", slug) VALUES('Scroll of Onymyoji', 'https://cdn1.codashop.com/S/content/common/images/mno/SOO_640*241.jpg', 'scroll-of-onymyoji');
		INSERT INTO public."MTGame" (name, "thumbnailUrl", slug) VALUES('Madtale Idle RPG', 'https://cdn1.codashop.com/S/content/common/images/mno/madtale_idle_rpg_banner.jpeg', 'madtale-idle-rpg');
		INSERT INTO public."MTGame" (name, "thumbnailUrl", slug) VALUES('Ensemble Stars Music', 'https://cdn.unipin.com/images/icon_product_pages/1668508038-icon-icon-200.jpg', 'ensemble-stars-music');
		INSERT INTO public."MTGame" (name, "thumbnailUrl", slug) VALUES('Idle Legends GOD SAGA', 'https://cdn1.codashop.com/S/content/common/images/mno/Idle-Legends-banner.jpg', 'idle-legends-god-saga');
INSERT INTO public."MTGame" (name, "thumbnailUrl", slug) VALUES('Miko Era Twelve Myths', 'https://cdn1.codashop.com/S/content/common/images/mno/MikoEra_Banner.jpeg', 'miko-era-twelve-myths');

	''')


def downgrade() -> None:
    op.execute('DELETE FROM public."MTGame"')
