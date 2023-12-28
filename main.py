import PIL.Image
import pilgram


print("Hello! Would you prefer to enhance your images with Instagram-style filters (Type 1) or edit them manually (Type 2)?")
user = int(input())


if user == 1:
    print("Here are the options:")
    print("_1977, aden, brannan, brooklyn, clarendon, earlybird, gingham, hudson, inkwell, kelvin, lark, lofi, maven, "
          "mayfair, moon, nashville, perpetua, reyes, rise, slumber, stinson, toaster, valencia, walden, willow, xpro2")
    filter_choice = str(input("What filter would you like to use? "))
    img = PIL.Image.open("Mountains.jpg")

    filter_choice = filter_choice.lower()

    if filter_choice == '_1977':
        pilgram._1977(img).save("IGFilter_1977.jpg")
        print("Success!")
    elif filter_choice == 'aden':
        pilgram.aden(img).save("IGFilter_aden.jpg")
        print("Success!")
    elif filter_choice == 'brannan':
        pilgram.brannan(img).save("IGFilter_brannan.jpg")
        print("Success!")
    elif filter_choice == 'brooklyn':
        pilgram.brooklyn(img).save("IGFilter_brooklyn.jpg")
        print("Success!")
    elif filter_choice == 'clarendon':
        pilgram.clarendon(img).save("IGFilter_clarendon.jpg")
        print("Success!")
    elif filter_choice == 'earlybird':
        pilgram.earlybird(img).save("IGFilter_earlybird.jpg")
        print("Success!")
    elif filter_choice == 'gingham':
        pilgram.gingham(img).save("IGFilter_gingham.jpg")
        print("Success!")
    elif filter_choice == 'hudson':
        pilgram.hudson(img).save("IGFilter_hudson.jpg")
        print("Success!")
    elif filter_choice == 'inkwell':
        pilgram.inkwell(img).save("IGFilter_inkwell.jpg")
        print("Success!")
    elif filter_choice == 'kelvin':
        pilgram.kelvin(img).save("IGFilter_kelvin.jpg")
        print("Success!")
    elif filter_choice == 'lark':
        pilgram.lark(img).save("IGFilter_lark.jpg")
        print("Success!")
    elif filter_choice == 'lofi':
        pilgram.lofi(img).save("IGFilter_lofi.jpg")
        print("Success!")
    elif filter_choice == 'maven':
        pilgram.maven(img).save("IGFilter_maven.jpg")
        print("Success!")
    elif filter_choice == 'mayfair':
        pilgram.mayfair(img).save("IGFilter_mayfair.jpg")
        print("Success!")
    elif filter_choice == 'moon':
        pilgram.moon(img).save("IGFilter_moon.jpg")
        print("Success!")
    elif filter_choice == 'nashville':
        pilgram.nashville(img).save("IGFilter_nashville.jpg")
        print("Success!")
    elif filter_choice == 'perpetua':
        pilgram.perpetua(img).save("IGFilter_perpetua.jpg")
        print("Success!")
    elif filter_choice == 'reyes':
        pilgram.reyes(img).save("IGFilter_reyes.jpg")
        print("Success!")
    elif filter_choice == 'rise':
        pilgram.rise(img).save("IGFilter_rise.jpg")
        print("Success!")
    elif filter_choice == 'slumber':
        pilgram.slumber(img).save("IGFilter_slumber.jpg")
        print("Success!")
    elif filter_choice == 'stinson':
        pilgram.stinson(img).save("IGFilter_stinson.jpg")
        print("Success!")
    elif filter_choice == 'toaster':
        pilgram.toaster(img).save("IGFilter_toaster.jpg")
        print("Success!")
    elif filter_choice == 'valencia':
        pilgram.valencia(img).save("IGFilter_valencia.jpg")
        print("Success!")
    elif filter_choice == 'walden':
        pilgram.walden(img).save("IGFilter_walden.jpg")
        print("Success!")
    elif filter_choice == 'willow':
        pilgram.willow(img).save("IGFilter_willow.jpg")
        print("Success!")
    elif filter_choice == 'xpro2':
        pilgram.xpro2(img).save("IGFilter_xpro2.jpg")
        print("Success!")
    else:
        print("Invalid filter choice. Make sure you spell the filters right.")


elif user == 2:

    img = PIL.Image.open("Mountains.jpg")

    print("Would you like to add:")
    user_choice = str(input("contrast, grayscale, hue_rotate, saturate, sepia? "))
    if user_choice == 'contrast':
        user_input = int(input("How much would you like to add? "))
        pilgram.css.contrast(img, user_input).save('contrast.jpg')
    elif user_choice == 'grayscale':
        user_input = int(input("How much would you like to add? "))
        pilgram.css.grayscale(img, user_input).save('grayscale.jpg')
    elif user_choice == 'hue_rotate':
        user_input = int(input("How much would you like to add? "))
        pilgram.css.hue_rotate(img, user_input).save('hue_rotate.jpg')
    elif user_choice == 'saturate':
        user_input = int(input("How much would you like to add? "))
        pilgram.css.saturate(img, user_input).save('saturate.jpg')
    elif user_choice == 'sepia':
        user_input = int(input("How much would you like to add? "))
        pilgram.css.sepia(img, user_input).save('sepia.jpg')
    else:
        print("Invalid choice. Make sure you spell the filters right.")