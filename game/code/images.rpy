# ANIMATION
init:
    image button_circle_green:
        "content/gfx/interface/icons/move15.png"
        yoffset 6

    image no_image = "content/gfx/interface/images/no_image.png"

    image bg_main = "content/gfx/bg/main.jpg"

    image eyes:
        zoom .7
        additive 1.0
        alpha .7
        "content/gfx/animations/main_menu/eyes/eyes1.webp"
        pause 1
        "content/gfx/animations/main_menu/eyes/eyes2.webp"
        pause 2
        "content/gfx/animations/main_menu/eyes/eyes3.webp"
        pause .2
        "content/gfx/animations/main_menu/eyes/eyes4.webp"
        pause .2
        "content/gfx/animations/main_menu/eyes/eyes5.webp"
        pause .2
        "content/gfx/animations/main_menu/eyes/eyes6.webp"
        pause .2
        "content/gfx/animations/main_menu/eyes/eyes7.webp"
        pause 1
        "content/gfx/animations/main_menu/eyes/eyes8.webp"
        pause 2
        "content/gfx/animations/main_menu/eyes/eyes9.webp"
        pause 2
        "content/gfx/animations/main_menu/eyes/eyes10.webp"
        pause 2
        "content/gfx/animations/main_menu/eyes/eyes11.webp"
        pause .2
        "content/gfx/animations/main_menu/eyes/eyes12.webp"
        pause .2
        "content/gfx/animations/main_menu/eyes/eyes13.webp"
        pause .2
        "content/gfx/animations/main_menu/eyes/eyes14.webp"
        pause .2
        "content/gfx/animations/main_menu/eyes/eyes15.webp"
        pause .2
        "content/gfx/animations/main_menu/eyes/eyes16.webp"
        pause .2
        "content/gfx/animations/main_menu/eyes/eyes17.webp"
        pause .2
        "content/gfx/animations/main_menu/eyes/eyes18.webp"
        pause .2
        "content/gfx/animations/main_menu/eyes/eyes19.webp"
        pause .2
        "content/gfx/animations/main_menu/eyes/eyes20.webp"
        pause .2
        "content/gfx/animations/main_menu/eyes/eyes21.webp"
        pause 1
        "content/gfx/animations/main_menu/eyes/eyes22.webp"
        pause 2
        "content/gfx/animations/main_menu/eyes/eyes23.webp"
        pause 1
        "content/gfx/animations/main_menu/eyes/eyes24.webp"
        pause .2
        "content/gfx/animations/main_menu/eyes/eyes25.webp"
        pause .2
        "content/gfx/animations/main_menu/eyes/eyes26.webp"
        pause .2
        "content/gfx/animations/main_menu/eyes/eyes27.webp"
        pause .2
        "content/gfx/animations/main_menu/eyes/eyes28.webp"
        pause .2
        "content/gfx/animations/main_menu/eyes/eyes29.webp"
        pause 1
        "content/gfx/animations/main_menu/eyes/eyes30.webp"
        pause 1
        "content/gfx/animations/main_menu/eyes/eyes31.webp"
        pause .5
        "content/gfx/animations/main_menu/eyes/eyes32.webp"
        pause 1
        "content/gfx/animations/main_menu/eyes/eyes33.webp"
        pause .5
        "content/gfx/animations/main_menu/eyes/eyes34.webp"
        pause 1
        "content/gfx/animations/main_menu/eyes/eyes35.webp"
        pause .5
        "content/gfx/animations/main_menu/eyes/eyes36.webp"
        pause .5
        "content/gfx/animations/main_menu/eyes/eyes37.webp"
        pause .5
        "content/gfx/animations/main_menu/eyes/eyes38.webp"
        pause 1
        "content/gfx/animations/main_menu/eyes/eyes39.webp"
        pause .4
        "content/gfx/animations/main_menu/eyes/eyes40.webp"
        pause .4
        repeat

    image anim_logo:
        subpixel True
        additive .1
        alpha .95
        "content/gfx/animations/main_menu/anim_logo/logo1.webp"
        pause .2
        "content/gfx/animations/main_menu/anim_logo/logo2.webp"
        pause .2
        "content/gfx/animations/main_menu/anim_logo/logo3.webp"
        pause .3
        "content/gfx/animations/main_menu/anim_logo/logo2.webp"
        pause .2
        "content/gfx/animations/main_menu/anim_logo/logo1.webp"
        pause .2
        "content/gfx/animations/main_menu/anim_logo/logo5.webp"
        pause .2
        "content/gfx/animations/main_menu/anim_logo/logo6.webp"
        pause .3
        "content/gfx/animations/main_menu/anim_logo/logo5.webp"
        pause .2
        repeat

    image fog:
        "content/gfx/animations/main_menu/fog1.webp"
        pos (15, 20)

    image mm_fire = "content/gfx/animations/main_menu/fire1.webp"

    image mm_clouds = "content/gfx/animations/main_menu/cloud1.webp"
    image mm_cloudstest = im.Scale("content/gfx/animations/main_menu/cloud1.webp", 287, 263)

    image save:
        zoom .4
        additive 1.0
        alpha .7
        "content/gfx/animations/main_menu/settings/save1.png"
        pause .2
        "content/gfx/animations/main_menu/settings/save2.png"
        pause .2
        "content/gfx/animations/main_menu/settings/save3.png"
        pause .2
        "content/gfx/animations/main_menu/settings/save4.png"
        pause .2
        "content/gfx/animations/main_menu/settings/save5.png"
        pause .2
        "content/gfx/animations/main_menu/settings/save6.png"
        pause .2
        "content/gfx/animations/main_menu/settings/save7.png"
        pause .2
        "content/gfx/animations/main_menu/settings/save8.png"
        pause .2
        "content/gfx/animations/main_menu/settings/save9.png"
        pause .2
        "content/gfx/animations/main_menu/settings/save10.png"
        pause .2
        "content/gfx/animations/main_menu/settings/save11.png"
        pause .2
        "content/gfx/animations/main_menu/settings/save12.png"
        pause .2
        repeat

    image slo:
        zoom .9
        additive 1.0
        #alpha .7
        "content/gfx/animations/main_menu/settings/slo1.png"
        pause .2
        "content/gfx/animations/main_menu/settings/slo2.png"
        pause .2
        "content/gfx/animations/main_menu/settings/slo3.png"
        pause .2
        "content/gfx/animations/main_menu/settings/slo4.png"
        pause .2
        "content/gfx/animations/main_menu/settings/slo5.png"
        pause .2
        "content/gfx/animations/main_menu/settings/slo6.png"
        pause .2
        "content/gfx/animations/main_menu/settings/slo7.png"
        pause .2
        "content/gfx/animations/main_menu/settings/slo8.png"
        pause .2
        repeat

    # Interactions module:
    # Portrait overlays (for enhancing emotions):
    image angry_pulse = "content/gfx/animations/interactions/angry.webp"
    image sweat_drop = "content/gfx/animations/interactions/uncertain.webp"
    image scared_lines = "content/gfx/animations/interactions/scared.webp"
    image question_mark = "content/gfx/animations/interactions/puzzled.webp"
    image exclamation_mark = "content/gfx/animations/interactions/exclamation.webp"
    image music_note = "content/gfx/animations/interactions/note.webp"
    image shy_blush = "content/gfx/animations/interactions/blush.webp"
    image hearts_rise = FilmStrip('content/gfx/animations/interactions/hearts.webp', (168, 157), (10, 3), .07, loop=True)

    image hearts_flow:
        subpixel True
        anchor (.5, 1.0)
        alpha .8
        additive .9
        "content/gfx/animations/interactions/hearts/heart1.webp"
        pause .07
        "content/gfx/animations/interactions/hearts/heart2.webp"
        pause .07
        "content/gfx/animations/interactions/hearts/heart3.webp"
        pause .07
        "content/gfx/animations/interactions/hearts/heart4.webp"
        pause .07
        "content/gfx/animations/interactions/hearts/heart5.webp"
        pause .07
        "content/gfx/animations/interactions/hearts/heart6.webp"
        pause .07
        "content/gfx/animations/interactions/hearts/heart7.webp"
        pause .07
        "content/gfx/animations/interactions/hearts/heart8.webp"
        pause .07
        "content/gfx/animations/interactions/hearts/heart9.webp"
        pause .07
        "content/gfx/animations/interactions/hearts/heart10.webp"
        pause .07
        "content/gfx/animations/interactions/hearts/heart11.webp"
        pause .07
        "content/gfx/animations/interactions/hearts/heart12.webp"
        pause .07
        "content/gfx/animations/interactions/hearts/heart13.webp"
        pause .07
        "content/gfx/animations/interactions/hearts/heart14.webp"
        pause .07
        "content/gfx/animations/interactions/hearts/heart15.webp"
        pause .07
        repeat

    image fire_element_be_viewport = ProportionalScale("content/gfx/interface/images/elements/small_fire.png", 15, 15)
    image water_element_be_viewport = ProportionalScale("content/gfx/interface/images/elements/small_water.png", 15, 15)
    image earth_element_be_viewport = ProportionalScale("content/gfx/interface/images/elements/small_earth.png", 15, 15)
    image darkness_element_be_viewport = ProportionalScale("content/gfx/interface/images/elements/small_darkness.png", 15, 15)
    image ice_element_be_viewport = ProportionalScale("content/gfx/interface/images/elements/small_ice.png", 15, 15)
    image air_element_be_viewport = ProportionalScale("content/gfx/interface/images/elements/small_air.png", 15, 15)
    image ele_element_be_viewport = ProportionalScale("content/gfx/interface/images/elements/small_electricity.png", 15, 15)
    image light_element_be_viewport = ProportionalScale("content/gfx/interface/images/elements/small_light.png", 15, 15)
    image healing_be_viewport = ProportionalScale("content/gfx/interface/images/elements/healing.png", 13, 13)
    image poison_be_viewport = ProportionalScale("content/gfx/interface/images/elements/poison.png", 15, 15)
    image physical_be_viewport = ProportionalScale("content/gfx/interface/images/elements/physical.png", 15, 15)

    image fire_element_be_size20 = ProportionalScale("content/gfx/interface/images/elements/small_fire.png", 20, 20)
    image water_element_be_size20 = ProportionalScale("content/gfx/interface/images/elements/small_water.png", 20, 20)
    image earth_element_be_size20 = ProportionalScale("content/gfx/interface/images/elements/small_earth.png", 20, 20)
    image darkness_element_be_size20 = ProportionalScale("content/gfx/interface/images/elements/small_darkness.png", 20, 20)
    image ice_element_be_size20 = ProportionalScale("content/gfx/interface/images/elements/small_ice.png", 20, 20)
    image air_element_be_size20 = ProportionalScale("content/gfx/interface/images/elements/small_air.png", 20, 20)
    image ele_element_be_size20 = ProportionalScale("content/gfx/interface/images/elements/small_electricity.png", 20, 20)
    image light_element_be_size20 = ProportionalScale("content/gfx/interface/images/elements/small_light.png", 20, 20)
    image healing_be_size20 = ProportionalScale("content/gfx/interface/images/elements/healing.png", 18, 18)
    image poison_be_size20 = ProportionalScale("content/gfx/interface/images/elements/poison.png", 20, 20)
    image physical_be_size20 = ProportionalScale("content/gfx/interface/images/elements/physical.png", 20, 20)
