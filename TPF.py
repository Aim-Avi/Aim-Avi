from easygui import *
text = "Are the planes departing(1) or arriving(2). 1 for Departing and 2 for Arrival"
title = "TPF"
d_int =0
lower = 0
upper = 99999
ardp = integerbox(text, title, d_int, lower, upper)

if ardp == 1:
        text = "Enter Weight for Plane1 in Tons(Except dry weight)"
        title = "TPF"
        d_int = 10
        lower = 0
        upper = 99999
        mscwd1 = integerbox(text, title, d_int, lower, upper)

        text = "Enter dry weight for Plane1 in tons"
        title = "TPF"
        d_int = 10
        lower = 0
        upper = 99999
        weightd1 = integerbox(text, title, d_int, lower, upper)

        text = "Enter Gate of Plane "
        title = "TPF"
        d_int = 1
        lower = 0
        upper = 99999
        gpd1 = integerbox(text, title, d_int, lower, upper)

        categoryd1 = 0

        if weightd1 > 102:
            categoryd1 = 3
        elif 102 > weightd1 > 7:
            categoryd1 = 2
        elif weightd1 < 7:
            categoryd1 = 1
        else:
            categoryd1 = 0

        if categoryd1 == 1:
            if gpd1 == 1 :
                message = "Use Runway 09l via C1-B2-A2"
                title = "TPF"
                ok_btn_txt = "Confirm"
                output = msgbox(message, title, ok_btn_txt)
            elif  gpd1 == 2 :
                message = "Use Runway 09l via C2-B2-A2"
                title = "TPF"
                ok_btn_txt = "Confirm"
                output = msgbox(message, title, ok_btn_txt)
            elif gpd1 == 3 :
                message = "Use Runway 09l via C2-B2-A2"
                title = "TPF"
                ok_btn_txt = "Confirm"
                output = msgbox(message, title, ok_btn_txt)
            elif gpd1 == 4 :
                message = "Use Runway 09l via C3-C2--B2-A2"
                title = "TPF"
                ok_btn_txt = "Confirm"
                output = msgbox(message, title, ok_btn_txt)
            else :
                message = "Wrong value"
                title = "TPF"
                ok_btn_txt = "Confirm"
                output = msgbox(message, title, ok_btn_txt)
        elif categoryd1 == 2:
            if gpd1 == 1 :
                message = "Use Runway 09R via C1-C2-C3-B4"
                title = "TPF"
                ok_btn_txt = "Confirm"
                output = msgbox(message, title, ok_btn_txt)
            elif  gpd1 == 2 :
                message = "Use Runway 09R via C2-C3-B4"
                title = "TPF"
                ok_btn_txt = "Confirm"
                output = msgbox(message, title, ok_btn_txt)
            elif gpd1 == 3 :
                message = "Use Runway 09R via C3-B4"
                title = "TPF"
                ok_btn_txt = "Confirm"
                output = msgbox(message, title, ok_btn_txt)
            elif gpd1 == 4 :
                message = "Use Runway 09R via C3-B4"
                title = "TPF"
                ok_btn_txt = "Confirm"
                output = msgbox(message, title, ok_btn_txt)
            else :
                message = "Wrong value"
                title = "TPF"
                ok_btn_txt = "Confirm"
                output = msgbox(message, title, ok_btn_txt)
        elif categoryd1 == 3:
            if gpd1 == 1 :
                message = "Use Runway 09R via C1-C2-C3-B4"
                title = "TPF"
                ok_btn_txt = "Confirm"
                output = msgbox(message, title, ok_btn_txt)
            elif  gpd1 == 2 :
                message = "Use Runway 09R via C2-C3-B4"
                title = "TPF"
                ok_btn_txt = "Confirm"
                output = msgbox(message, title, ok_btn_txt)
            elif gpd1 == 3 :
                message = "Use Runway 09R via C3-B4"
                title = "TPF"
                ok_btn_txt = "Confirm"
                output = msgbox(message, title, ok_btn_txt)
            elif gpd1 == 4 :
                message = "Use Runway 09R via C3-B4"
                title = "TPF"
                ok_btn_txt = "Confirm"
                output = msgbox(message, title, ok_btn_txt)
            else :
                message = "Wrong value"
                title = "TPF"
                ok_btn_txt = "Confirm"
                output = msgbox(message, title, ok_btn_txt)

        else:
            message = "Wrong value"
            title = "TPF"
            ok_btn_txt = "Confirm"
            output = msgbox(message, title, ok_btn_txt)

elif ardp == 2:
    text = "How many planes are on Final Approach"
    title = "TPF"
    d_int = 1
    lower = 0
    upper = 99999
    plnos = integerbox(text, title, d_int, lower, upper)

    if plnos == 1:
        text = "Enter Weight for Plane1 in Tons(Except dry weight)"
        title = "TPF"
        d_int = 10
        lower = 0
        upper = 99999
        mscw = integerbox(text, title, d_int, lower, upper)

        text = "Enter dry weight for Plane1 in tons"
        title = "TPF"
        d_int = 10
        lower = 0
        upper = 99999
        weight = integerbox(text, title, d_int, lower, upper)

        text = "Enter vertical speed for Plane1 (feet/second)"
        title = "TPF"
        d_int = 10
        lower = 0
        upper = 99999
        vs = integerbox(text, title, d_int, lower, upper)

        text = "Enter altitude for Plane1 (feet)"
        title = "TPF"
        d_int = 10
        lower = 0
        upper = 99999
        alt = integerbox(text, title, d_int, lower, upper)

        ttouchd = alt/vs

        category = 0

        if weight > 102:
            category = 3
        elif 102 > weight > 7:
            category = 2
        elif weight < 7:
            category = 1
        else:
            category = 0

        if category == 1:
            message = "Use Runway 09l with taxiway A1-B1-C1"
            title = "TPF"
            ok_btn_txt = "Confirm"
            output = msgbox(message, title, ok_btn_txt)
        elif category == 2:
            message = "Runway 09r with taxiway B2-C2"
            title = "TPF"
            ok_btn_txt = "Confirm"
            output = msgbox(message, title, ok_btn_txt)
        elif category == 3:
            message = "Use Runway 09r with taxiway B1-C1"
            title = "TPF"
            ok_btn_txt = "Confirm"
            output = msgbox(message, title, ok_btn_txt)

        else:
            message = "Wrong value"
            title = "TPF"
            ok_btn_txt = "Confirm"
            output = msgbox(message, title, ok_btn_txt)

    elif plnos == 2 :
        text = "Enter Weight for Plane1 (Except dry weight)"
        title = "TPF"
        d_int = 10
        lower = 0
        upper = 99999
        mscw1 = integerbox(text, title, d_int, lower, upper)

        text = "Enter dry weight for Plane1 (in tons)"
        title = "TPF"
        d_int = 10
        lower = 0
        upper = 99999
        weight1 = integerbox(text, title, d_int, lower, upper)

        text = "Enter vertical speed for Plane1 (feet/second)"
        title = "TPF"
        d_int = 10
        lower = 0
        upper = 99999
        vs1 = integerbox(text, title, d_int, lower, upper)

        text = "Enter altitude for Plane1 (feet)"
        title = "TPF"
        d_int = 10
        lower = 0
        upper = 99999
        alt1 = integerbox(text, title, d_int, lower, upper)

        ttouchd1 = alt1 / vs1

        category1 = 0

        if weight1 > 102:
            category1 = 3
        elif 102 > weight1 > 7:
            category1 = 2
        elif weight1 < 7:
            category1 = 1
        else:
            category1 = 0

        text = "Enter Weight for Plane2 (Except dry weight)"
        title = "TPF"
        d_int = 10
        lower = 0
        upper = 99999
        mscw2 = integerbox(text, title, d_int, lower, upper)

        text = "Enter dry weight for Plane2 (in tons)"
        title = "TPF"
        d_int = 10
        lower = 0
        upper = 99999
        weight2 = integerbox(text, title, d_int, lower, upper)

        text = "Enter vertical speed for Plane2 (feet/second)"
        title = "TPF"
        d_int = 10
        lower = 0
        upper = 99999
        vs2 = integerbox(text, title, d_int, lower, upper)

        text = "Enter altitude for Plane2 (feet)"
        title = "TPF"
        d_int = 10
        lower = 0
        upper = 99999
        alt2 = integerbox(text, title, d_int, lower, upper)

        ttouchd2 = alt2 / vs2

        category2 = 0

        if weight2 > 102:
            category2 = 3
        elif 102 > weight2 > 7:
            category2 = 2
        elif weight2 < 7:
            category2 = 1
        else:
            category2 = 0

        if weight1 == weight2 :
            if weight1 < 7:
                message = "Use Runway 09L for Plane1 via A1-B1-C1 and 09r for Plane2 via B2-C2"
                title = "TPF"
                ok_btn_txt = "Confirm"
                output = msgbox(message, title, ok_btn_txt)
            elif 102 > weight1 > 7:
                if vs1 == vs2:
                    message = "First, Let Plane1 land on 09R via  B2-C2.Than, Let Plane2 land on 09R after 5 minutes via B2-C2 "
                    title = "TPF"
                    ok_btn_txt = "Confirm"
                    output = msgbox(message, title, ok_btn_txt)
                elif vs1 > vs2 :
                    message = "First, Let Plane1 land on 09R via  B2-C2.Than, Let Plane2 land on 09R after 5 minutes via B2-C2"
                    title = "TPF"
                    ok_btn_txt = "Confirm"
                    output = msgbox(message, title, ok_btn_txt)
                elif vs1 < vs2 :
                     message = "First, Let Plane2 land on 09R via  B2-C2.Than, Let Plane1 land on 09R after 5 minutes via B2-C2"
                     title = "TPF"
                     ok_btn_txt = "Confirm"
                     output = msgbox(message, title, ok_btn_txt)
                else:
                    message = "Wrong value"
                    title = "TPF"
                    ok_btn_txt = "Confirm"
                    output = msgbox(message, title, ok_btn_txt)
            elif  weight1 > 102:
                if vs1 == vs2:
                    message = "First, Let Plane1 land on 09R via  B1-C1.Than, Let Plane2 land on 09R after 5 minutes via B1-C1 "
                    title = "TPF"
                    ok_btn_txt = "Confirm"
                    output = msgbox(message, title, ok_btn_txt)
                elif vs1>vs2 :
                    message = "First, Let Plane1 land on 09R via  B1-C1.Than, Let Plane2 land on 09R after 5 minutes via B1-C1"
                    title = "TPF"
                    ok_btn_txt = "Confirm"
                    output = msgbox(message, title, ok_btn_txt)
                elif vs1<vs2 :
                     message = "First, Let Plane2 land on 09R via  B1-C1.Than, Let Plane1 land on 09R after 5 minutes via B1-C1"
                     title = "TPF"
                     ok_btn_txt = "Confirm"
                     output = msgbox(message, title, ok_btn_txt)
                else:
                    message = "Wrong value"
                    title = "TPF"
                    ok_btn_txt = "Confirm"
                    output = msgbox(message, title, ok_btn_txt)
            else:
                message = "Wrong value"
                title = "TPF"
                ok_btn_txt = "Confirm"
                output = msgbox(message, title, ok_btn_txt)
        elif weight1 > weight2 :
                if 102 > weight1 > 7:
                    message = "Use 09R for Plane1 via B2-C2 and Runway 09L for Plane2 via A1-B1-C1 and"
                    title = "TPF"
                    ok_btn_txt = "Confirm"
                    output = msgbox(message, title, ok_btn_txt)
                elif weight1 > 102:
                    message = "Use Runway 09R for Plane1 via B1-C1 after 5 minutes, let Plane2 land on 09R via B2-B2 "
                    title = "TPF"
                    ok_btn_txt = "Confirm"
                    output = msgbox(message, title, ok_btn_txt)
                else :
                    message = "Wrong value"
                    title = "TPF"
                    ok_btn_txt = "Confirm"
                    output = msgbox(message, title, ok_btn_txt)
        elif weight2 > weight1 :
                if 102 > weight2 > 7:
                    message = "Use Runway 09L for Plane1 via A1-B1-C1 and 09R for Plane2 via B2-C2 "
                    title = "TPF"
                    ok_btn_txt = "Confirm"
                    output = msgbox(message, title, ok_btn_txt)
                elif weight2 > 102:
                    message = "Use Runway 09R for Plane2 via B1-C1 after 5 minutes, let Plane1 land on 09R via B2-B2 "
                    title = "TPF"
                    ok_btn_txt = "Confirm"
                    output = msgbox(message, title, ok_btn_txt)
                else :
                    message = "Wrong value"
                    title = "TPF"
                    ok_btn_txt = "Confirm"
                    output = msgbox(message, title, ok_btn_txt)
        else :
                message = "Wrong value"
                title = "TPF"
                ok_btn_txt = "Confirm"
                output = msgbox(message, title, ok_btn_txt)
    else :
        message = "Wrong value"
        title = "TPF"
        ok_btn_txt = "Confirm"
        output = msgbox(message, title, ok_btn_txt)
else:
    message = "Wrong value"
    title = "TPF"
    ok_btn_txt = "Confirm"
    output = msgbox(message, title, ok_btn_txt)

















