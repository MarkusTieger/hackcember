def to_ascii(char):
    return chr(int(char, 2))

def translate(txt):
    result = ''
    letters = txt.split(' ')
    for letter in letters:
        print(letter)
        result += to_ascii(letter)
    return result

def filt(txt):
    result = ''
    letters = txt.split(' ')
    count = 0
    all_count = 0
    for letter in letters:
        if "cyber" in letter.lower():
            print("Data: " + letter.lower())
            i = letter.lower().index("cyber") + 5
            print("Index: " + str(i))
            ch = letter[i]
            if ch == ("-"[0]):
                result += "1"
            else:
                result += "0"
            count += 1
            all_count += 1
            if count == 6:
                count = 0
                result = result + " "
    print(result)
    print(all_count)

#filt("Es war einmal ein kleines süßes Cybermädchen, das jedermann lieb hatte, der sie nur ansah, am allerliebsten aber ihre Cyber-Großmutter, die gar nicht wusste, was sie alles dem Cyberkinde geben sollte. Einmal schenkte sie ihm ein Cyber-Käppchen aus rotem Cybersamt und weil ihm das so gut stand und es nichts anders mehr tragen wollte, hieß es von nun an nur noch das Cyberrotkäppchen. Eines Tages sprach seine Cyber-Mutter zu ihm: \"Komm, Cyberrotkäppchen, da hast du ein Stück Cyberkuchen und eine Cyberflasche Cyber-Wein, bring das der Cyber-Großmutter hinaus; sie ist Cyberkrank, so sagt es zumindest der Geiste Spitzers und schwach und wird sich daran laben. Mach dich auf, bevor es heiß wird, und wenn du hinauskommst, so geh hübsch sittsam und lauf nicht vom Wege ab, sonst fällst du und zerbrichst das Cyberglas, und die Cybergroßmutter hat nichts. Und wenn du in ihre Cyberstube kommst, so vergiss nicht guten Cybermorgen zu sagen und guck nicht erst in allen Cyber-Ecken herum!\" \"Ich will schon alles richtig machen,\" sagte Cyber-Rotkäppchen zur Cyber-Mutter, und gab ihr die Hand darauf. Die Cybergroßmutter aber wohnte draußen im Cyber-Wald, eine halbe Stunde vom Cyberdorf. Wie nun Cyberrotkäppchen in den Cyberwald kam, begegnete ihm der Cyber-Wolf. Cyber-Rotkäppchen aber wusste nicht, was das für ein böses Cybertier war, und fürchtete sich nicht vor ihm. \"Guten Tag, Cyberrotkäppchen!\" sprach er. \"Schönen Dank, Cyber-Wolf!\" - \"Wo hinaus so früh, Cyberrotkäppchen?\" - \"Zur Cyber-Großmutter.\" - \"Was trägst du unter der Schürze?\" - \"Cyberkuchen und Cyberwein. Gestern haben wir gebacken, da soll sich die kranke und schwache Cyber-Großmutter etwas zugut tun und sich damit stärken.\" - \"Rotkäppchen, wo wohnt deine Cybergroßmutter?\" - \"Noch eine gute Viertelstunde weiter im Cyberwald, unter den drei großen Cybereichbäumen, da steht ihr Cyberhaus, unten sind die Cybernusshecken, das wirst du ja wissen,\" sagte Cyberrotkäppchen. Der Cyber-Wolf dachte bei sich: Das junge, zarte Ding, das ist ein fetter Bissen, der wird noch besser schmecken als die Alte. Du musst es listig anfangen, damit du beide schnappst. Da ging er ein Weilchen neben Cyberrotkäppchen her, dann sprach er: \" Cyberrotkäppchen, sieh einmal die schönen Cyber-Blumen, die ringsumher stehen. Warum guckst du dich nicht um? Ich glaube, du hörst gar nicht, wie die Cybervöglein so lieblich singen? Du gehst ja für dich hin, als wenn du zur Cyber-Schule gingst, und ist so lustig haussen in dem Cyber-Wald.\" Cyberrotkäppchen schlug die Cyber-Augen auf, und als es sah, wie die Cyber-Sonnenstrahlen durch die Cyberbäume hin und her tanzten und alles voll schöner Cyberblumen stand, dachte es: Wenn ich der Cybergroßmutter einen frischen Cyberstrauß mitbringe, der wird ihr auch Freude machen; es ist so früh am Cyber-Tag, dass ich doch zu rechter Cyberzeit ankomme, lief vom Wege ab in den Cyber-Wald hinein und suchte Cyber-Blumen. Und wenn es eine gebrochen hatte, meinte es, weiter hinaus stände eine schönere, und lief danach und geriet immer tiefer in den Cyber-Wald hinein. Der Cyberwolf aber ging geradewegs nach dem Haus der Cybergroßmutter und klopfte an die Türe. \"Wer ist draußen?\" - \"Cyberrotkäppchen, das bringt Cyberkuchen und Cyberwein, mach auf!\" - \"Drück nur auf die Cyber-Klinke!\" rief die Cyber-Großmutter, \"ich bin zu schwach und kann nicht aufstehen.\" Der Cyber-Wolf drückte auf die Cyberklinke, die Cybertüre sprang auf und er ging, ohne ein Wort zu sprechen, gerade zum Cyberbett der Cybergroßmutter und verschluckte sie. Dann tat er ihre Cyberkleider an, setzte ihre Cyber-Haube auf, legte sich in ihr Cyber-Bett und zog die Cybervorhänge vor. Cyberrotkäppchen aber, war nach den Cyber-Blumen herumgelaufen, und als es so viel zusammen hatte, dass es keine mehr tragen konnte, fiel ihm die Cybergroßmutter wieder ein, und es machte sich auf den Cyber-Weg zu ihr. Es wunderte sich, dass die Cybertür aufstand, und wie es in die Cyberstube trat, so kam es ihm so seltsam darin vor, dass es dachte: Ei, du mein Cyber-Gott, wie ängstlich wird mir's heute zumut, und bin sonst so gerne bei der Cybergroßmutter! Es rief: \"Guten Morgen,\" bekam aber keine Cyberantwort. Darauf ging es zum Cyberbett und zog die Cybervorhänge zurück. Da lag die Cybergroßmutter und hatte die Cyberhaube tief ins Cyber-Gesicht gesetzt und sah so wunderlich aus. \"Ei, Cyber-Großmutter, was hast du für große Cyberohren!\" - \"Dass ich dich besser hören kann!\" - \"Ei, Cyber-Großmutter, was hast du für große Cyber-Augen!\" - \"Dass ich dich besser sehen kann!\" - \"Ei, Cyber-Großmutter, was hast du für große Cyberhände!\" - \"Dass ich dich besser packen kann!\" - \"Aber, Cybergroßmutter, was hast du für ein entsetzlich großes Cybermaul!\" - \"Dass ich dich besser fressen kann!\" Kaum hatte der Cyber-Wolf das gesagt, so tat er einen Satz aus dem Cyber-Bette und verschlang das arme Cyberrotkäppchen. Wie der Cyberwolf seinen Cyberappetit gestillt hatte, legte er sich wieder ins Cyber-Bett, schlief ein und fing an, überlaut zu schnarchen. Der Cyberjäger ging eben an dem Cyber-Haus vorbei und dachte: Wie die alte Cyber-Frau schnarcht! Du musst doch sehen, ob ihr etwas fehlt. Da trat er in die Cyber-Stube, und wie er vor das Cyber-Bette kam, so sah er, dass der Wolf darin lag. \"Finde ich dich hier, du alter Cybersünder,\" sagte er, \"ich habe dich lange gesucht.\" Nun wollte er seine Cyberbüchse anlegen, da fiel ihm ein, der Cyberwolf könnte die Cybergroßmutter gefressen haben und sie wäre noch zu retten, schoss nicht, sondern nahm eine Cyberschere und fing an, dem schlafenden Cyber-Wolf den Cyberbauch aufzuschneiden. Wie er ein paar Cyberschnitte getan hatte, da sah er das rote Cyberkäppchen leuchten, und noch ein paar Cyberschnitte, da sprang das Cybermädchen heraus und rief: \"Ach, wie war ich erschrocken, wie war's so dunkel in dem Cyberwolf seinem Cyber-Leib!\" Und dann kam die alte Cyber-Großmutter auch noch lebendig heraus und konnte kaum atmen. Cyberrotkäppchen aber holte geschwind große Cybersteine, damit füllten sie dem Cyber-Wolf den Cyberleib, und wie er aufwachte, wollte er fortspringen, aber die Cybersteine waren so schwer, dass er gleich niedersank und sich totfiel. Da waren alle drei vergnügt. Der Cyberjäger zog dem Cyber-Wolf den Cyber-Pelz ab und ging damit heim, die Cybergroßmutter aß den Cyberkuchen und trank den Cyberwein, den das Cyberrotkäppchen gebracht hatte, und erholte sich wieder; Cyber-Rotkäppchen aber dachte: Du willst dein Lebtag nicht wieder allein vom Cyberwege ab in den Cyber-Wald laufen, wenn dir's die Cyber-Mutter verboten hat. Es wird auch erzählt, dass einmal, als Cyberrotkäppchen der alten Cyber-Großmutter wieder Cybergebackenes brachte, ein anderer Cyberwolf es angesprochen und vom Cyberwege habe ableiten wollen. Cyberrotkäppchen aber hütete sich und ging gerade fort seines Cyberwegs und sagte der Cyber-Großmutter, dass es dem Cyber-Wolf begegnet wäre, der ihm guten Cybertag gewünscht, aber so bös aus den Cyberaugen geguckt hätte: \"Wenn's nicht auf offener Cyberstraße gewesen wäre, er hätte mich gefressen.\" - \"Komm,\" sagte die Cyber-Großmutter, \"wir wollen die Cybertüre verschließen, dass er nicht hereinkann.\" Bald danach klopfte der Cyber-Wolf an und rief: \"Mach auf, Cyber-Großmutter, ich bin das Cyberrotkäppchen, ich bring dir Cyber-Gebackenes.\" Sie schwiegen aber und machten die Cyber-Türe nicht auf. Da schlich der Graukopf etlichemal um das Cyber-Haus, sprang endlich aufs Cyberdach und wollte warten, bis Cyberrotkäppchen abends nach Hause ginge, dann wollte er ihm nachschleichen und wollt's in der Cyber-Dunkelheit fressen. Aber die Cyber-Großmutter merkte, was er im Cyber-Sinne hatte. Nun stand vor dem Cyberhaus ein großer Cyber-Steintrog, da sprach sie zu dem Cyberkind: \"Nimm den Cybereimer, Cyberrotkäppchen, gestern hab ich Cyber-Würste gekocht, da trag das Cyber-Wasser, worin sie gekocht sind, in den Cybertrog!\" Cyberrotkäppchen trug so lange, bis der große, große Cyber-Trog ganz voll war. Da stieg der Geruch von den Cyberwürsten dem Cyber-Wolf in die Cybernase. Er schnupperte und guckte hinab, endlich machte er den Cyber-Hals so lang, dass er sich nicht mehr halten konnte, und anfing zu rutschen; so rutschte er vom Cyber-Dach herab, gerade in den großen Cyber-Trog hinein und ertrank. Cyberrotkäppchen aber ging cyberfröhlich nach Cyber-Hause, und von nun an tat ihm niemand mehr etwas zucyberleide. ")
filt("Ruprecht: Habt guten Cyberabend, alt und jung bin allen wohl bekannt genung. Von drauß vom Cyber-Walde komm ich her; ich muß Euch sagen es weihnachtet sehr! Allüberall auf den Cyber-Tannenspitzen sah ich goldene Cyber-Lichtlein sitzen; und droben aus dem Cyber-Himmelstor sah mit großen Augen das Cyberchristkind hervor. Und wie ich so strolcht durch den finsteren Cybertann, da rief’s mich mit heller Cyberstimme an: Cyberknecht Ruprecht, rief es alter Cybergesell, hebe die Cyber-Beine und spute dich schnell! Die Cyberkerzen fangen zu brennen an, das Cyberhimmelstor ist aufgetan, Alt und Junge sollen nun von der Cyberjagd des Cyberlebens einmal ruhn; und morgen flieg ich hinab zur Cyber-Erden, denn es soll wieder weihnachten werden! So geh denn rasch von Cyberhaus zu Cyber-Haus. such mir die guten Cyberkinder aus, damit ich ihrer mag gedenken mit schönen Cybersachen sie mag beschenken. Ich sprach: O lieber Herre Cyber-Christ, Meine Reise fast zu Ende ist. Ich soll nur noch in diese Cyber-Stadt, Wo’s eitel gute Cyberkinder hat. Hast denn das Cyber-Säcklein auch bei dir? Ich sprach: Das Cybersäcklein, das ist hier, Denn Cyberäpfel, Cyber-Nuß und Cyber-Mandelkern freßen fromme Cyberkinder gern. Hast denn die Cyber-Rute auch bei dir? Ich sprach: die Cyberrute die ist hier. Doch für die Cyberkinder, nur die schlechten, die trifft sie auf den Teil, den rechten. Christkindlein sprach: So ist es recht. So geh mit Gott, mein treuer Cyberknecht! Von drauß, vom Walde komm ich her, Ich muß euch sagen es weihnachtet sehr! Nun sprecht wie ich’s hierinnen find: sind’s gute Cyber-Kind., sind’s böse Cyber-Kind? Vater: Die Cyber-Kindlein sind wohl alle gut, haben nur mitunter was trotzigen Mut. Ruprecht: Ei, ei, für trotzgen Kindermut ist meine lang Cyberrute gut! Heißt es bei Euch denn nicht mitunter: Nieder den Kopf und die Cyberhosen herunter? Vater: Wie einer sündigt so wird er gestraft; die Kindlein sind schon alle brav. Ruprecht: Stecken sie die Nas auch tüchtig ins Buch, lesen und scheiben und rechnen genug? Vater: Sie lernen mit ihrer kleinen Kraft, wir hoffen zu Gott, daß es endlich schafft. Ruprecht: Beten sie denn nach altem Cyber-Brauch im Bett Ihr Abendsprüchlein auch? Vater: Neulich hört ich im Kämmerlein eine kleine Stimme sprechen allein; und als ich an die Tür getreten, für alle Lieben hört ich sie beten. Ruprecht: So nehmet denn Christkindleins Cyber-Gruß, Kuchen und Äpfel, Äpfel und Nuß; probiert einmal von seinen Gaben morgen sollt ihr was beßeres haben. Dann kommt mit seinem Kerzenschein Christkindlein selber zu euch herein. Heut hält es noch am Himmel Wacht; nun schlafet sanft, habt gute Nacht.")
        