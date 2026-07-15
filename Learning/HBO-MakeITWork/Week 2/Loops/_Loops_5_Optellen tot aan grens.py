#zelf gemaakt m.b.v. ChatGPT

def tel_aantal_te_sommeren_getallen(grens):

    aantal = 0
    totaal = 0

    while totaal + (aantal+1) < grens:
        aantal = aantal + 1
        totaal = totaal + aantal
    print(f" de eerste {aantal}, zijn net geen {grens}. Het totaal is namelijk {totaal}")

tel_aantal_te_sommeren_getallen(2000)