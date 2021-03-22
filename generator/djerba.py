#!/usr/bin/python
# -*- coding: utf-8 -*-
import transitfeed


schedule = transitfeed.Schedule()
schedule.AddAgency("Société régionale de transport de Medenine", "http://www.srtm.tn/", "Africa/Tunis", 'FR')

service_period = schedule.GetDefaultServicePeriod()
service_period.SetStartDate("20170101")
service_period.SetEndDate("20200101")
service_period.SetWeekdayService(True)
#service_period.SetDateHasService('20070704', False)

stop1 = schedule.AddStop(lng=10.7988301, lat=33.86370184, name="Mellita 2")
stop2 = schedule.AddStop(lng=10.81067653, lat=33.86268142, name="Mellita 1")
stop3 = schedule.AddStop(lng=10.82517735, lat=33.86370184, name="Mosquet Kébir")
stop4 = schedule.AddStop(lng=10.79042455, lat=33.86606919, name="Essouissi")
stop5 = schedule.AddStop(lng=10.77720177, lat=33.86957927, name="L'aéroport")
stop6 = schedule.AddStop(lng=10.79199752, lat=33.85802811, name="Margane 1")
stop7 = schedule.AddStop(lng=10.78541071, lat=33.855783, name="Margane 2")
stop8 = schedule.AddStop(lng=10.83900515, lat=33.87007028, name="Elhimaya")
stop9 = schedule.AddStop(lng=10.84298569, lat=33.87288926, name="Bir mgalas")
stop10 = schedule.AddStop(lng=10.858049, lat=33.872285, name="Houmet Souk")
stop11 = schedule.AddStop(lng=10.86589335, lat=33.86673275, name="L'hôpital")
stop12 = schedule.AddStop(lng=10.88622537, lat=33.87055632, name="Fatou1")
stop13 = schedule.AddStop(lng=10.86076157, lat=33.88199359, name="Station Elmarsa")
stop14 = schedule.AddStop(lng=10.87047879, lat=33.87927211, name="Elwilayia")
stop15 = schedule.AddStop(lng=10.88015698, lat=33.87745775, name="Sidi Zayed")
stop16 = schedule.AddStop(lng=10.8908108, lat=33.87535174, name="Lobirette")
stop17 = schedule.AddStop(lng=10.89916215, lat=33.87376409, name="Fatou2")
stop18 = schedule.AddStop(lng=10.90396222, lat=33.87470372, name="Sidi Ismail")
stop19 = schedule.AddStop(lng=10.91008914, lat=33.87314847, name="Arouay")
stop20 = schedule.AddStop(lng=10.9290943, lat=33.87344008, name="Croisement Guisen")
stop21 = schedule.AddStop(lng=10.94542625, lat=33.86887138, name="Elmagtaa")
stop22 = schedule.AddStop(lng=10.93742613, lat=33.87010268, name="Ras ettabia")
stop23 = schedule.AddStop(lng=10.9533093, lat=33.86926021, name="Athene")
stop24 = schedule.AddStop(lng=10.95959232, lat=33.86731602, name="Ulysse")
stop25 = schedule.AddStop(lng=10.96767049, lat=33.86605226, name="Eljazira")
stop26 = schedule.AddStop(lng=10.96798269, lat=33.86109429, name="Dalli")
stop27 = schedule.AddStop(lng=10.97395351, lat=33.85914991, name="Holiday")
stop28 = schedule.AddStop(lng=10.97840236, lat=33.85516379, name="Elmadina")
stop29 = schedule.AddStop(lng=10.9831634, lat=33.85571473, name="Abou Nawess")
stop30 = schedule.AddStop(lng=10.98687078, lat=33.85169604, name="Palm Beach")
stop31 = schedule.AddStop(lng=10.98730005, lat=33.84699653, name="Toumana")
stop32 = schedule.AddStop(lng=10.9889391, lat=33.84320432, name="Yasmina")
stop33 = schedule.AddStop(lng=10.99565139, lat=33.84362568, name="Dar Midoun")
stop34 = schedule.AddStop(lng=10.99295867, lat=33.8390878, name="R.D.V")
stop35 = schedule.AddStop(lng=10.99900754, lat=33.84006022, name="Hasdrubal")
stop36 = schedule.AddStop(lng=11.00080269, lat=33.83665669, name="Minenx")
stop37 = schedule.AddStop(lng=11.00513446, lat=33.83195635, name="Elhana")
stop38 = schedule.AddStop(lng=11.00954429, lat=33.82884426, name="Plazza")
stop39 = schedule.AddStop(lng=11.01317361, lat=33.82732059, name="Golf")
stop40 = schedule.AddStop(lng=11.01645171, lat=33.82618592, name="Yadis")
stop41 = schedule.AddStop(lng=11.01953468, lat=33.82550511, name="Elmahari")
stop42 = schedule.AddStop(lng=11.02312498, lat=33.82527818, name="Elmanara")
stop43 = schedule.AddStop(lng=11.02710552, lat=33.82638044, name="Abou Nawess Golf")
stop44 = schedule.AddStop(lng=11.0301885, lat=33.82702882, name="Dar Jeba")
stop45 = schedule.AddStop(lng=11.04095939, lat=33.82456494, name="Phare Ennadhour")
stop46 = schedule.AddStop(lng=10.99082, lat=33.805388, name="Midoun")
stop47 = schedule.AddStop(lng=10.98511465, lat=33.80368402, name="Hadher bach")
stop48 = schedule.AddStop(lng=10.97777796, lat=33.81649202, name="Fadhloun")
stop49 = schedule.AddStop(lng=10.97231446, lat=33.81808073, name="Mosquet Elgayed 1")
stop50 = schedule.AddStop(lng=10.97311447, lat=33.79878729, name="Boufaden")
stop51 = schedule.AddStop(lng=10.96616803, lat=33.79697121, name="Mahboubine")
stop52 = schedule.AddStop(lng=10.99383673, lat=33.79846299, name="Mosquet Ben Ammar")
stop53 = schedule.AddStop(lng=10.99504651, lat=33.79252815, name="Essaegh")
stop54 = schedule.AddStop(lng=10.99879291, lat=33.78464681, name="Elazmouni")
stop55 = schedule.AddStop(lng=11.0044125, lat=33.78260339, name="Mosquet Arko")
stop56 = schedule.AddStop(lng=11.01135895, lat=33.78224659, name="Arko")
stop57 = schedule.AddStop(lng=11.02013957, lat=33.7811762, name="Elwachnia")
stop58 = schedule.AddStop(lng=11.02665674, lat=33.78438733, name="Elmoustaoussef")
stop59 = schedule.AddStop(lng=11.03555443, lat=33.77708913, name="Elmaamoura")
stop60 = schedule.AddStop(lng=11.03922278, lat=33.7786137, name="Carthago")
stop61 = schedule.AddStop(lng=11.04343748, lat=33.7808194, name="Calipso")
stop62 = schedule.AddStop(lng=11.0494083, lat=33.78163031, name="Jerba La douce")
stop63 = schedule.AddStop(lng=11.05498887, lat=33.78263582, name="Jerba Menzel")
stop64 = schedule.AddStop(lng=11.05483277, lat=33.78536038, name="Jerba La fidèle")
stop65 = schedule.AddStop(lng=11.0497205, lat=33.78714427, name="Ejmel")
stop66 = schedule.AddStop(lng=11.03906668, lat=33.79123086, name="Elmadrassa")
stop67 = schedule.AddStop(lng=11.03079338, lat=33.79440918, name="Ben Nacr")
stop68 = schedule.AddStop(lng=11.00074415, lat=33.80465685, name="Mosquet Ben Achour")
stop69 = schedule.AddStop(lng=11.01007112, lat=33.7990143, name="Hanout Bouzguin")
stop70 = schedule.AddStop(lng=11.02934946, lat=33.80858047, name="Tazdin")
stop71 = schedule.AddStop(lng=11.0501888, lat=33.7941173, name="Dar Hamouda")
stop72 = schedule.AddStop(lng=11.04386675, lat=33.81243907, name="Dar Edhaou")
stop73 = schedule.AddStop(lng=11.04277405, lat=33.81889129, name="Djerba Explorer (Ettmassi7)")
stop74 = schedule.AddStop(lng=11.05522302, lat=33.80407315, name="Tanit")
stop75 = schedule.AddStop(lng=11.03574956, lat=33.81944246, name="Maamar")
stop76 = schedule.AddStop(lng=11.02981776, lat=33.81924793, name="Elfitouri")
stop77 = schedule.AddStop(lng=11.02279326, lat=33.81720533, name="Yati")
stop78 = schedule.AddStop(lng=11.01307605, lat=33.81438451, name="Elmgarsa")
stop79 = schedule.AddStop(lng=11.00343688, lat=33.81347664, name="Elmhiri")
stop80 = schedule.AddStop(lng=10.97920237, lat=33.8079968, name="Khazroun")
stop81 = schedule.AddStop(lng=10.97014857, lat=33.80916414, name="Mosquet Elgayed 2")
stop82 = schedule.AddStop(lng=10.95504591, lat=33.80089519, name="Elweryemmi")
stop83 = schedule.AddStop(lng=10.94864581, lat=33.79992232, name="Ettouta")
stop84 = schedule.AddStop(lng=10.93931884, lat=33.79450648, name="elmehrab")
stop85 = schedule.AddStop(lng=10.93182605, lat=33.79230112, name="Elhajra elbidha")
stop86 = schedule.AddStop(lng=10.9228503, lat=33.79226869, name="Elhazem")
stop87 = schedule.AddStop(lng=10.91590386, lat=33.79531725, name="Ben Hamouda")
stop88 = schedule.AddStop(lng=10.908841, lat=33.796581, name="Hadj Dahmane")
stop89 = schedule.AddStop(lng=10.9020821, lat=33.7968814, name="ElKabou")
stop90 = schedule.AddStop(lng=10.884753, lat=33.801815, name="Elmay")
stop91 = schedule.AddStop(lng=10.88827418, lat=33.78840919, name="Elmaabri")
stop92 = schedule.AddStop(lng=10.86509334, lat=33.79356596, name="Oued amgar")
stop93 = schedule.AddStop(lng=10.84671258, lat=33.78607394, name="Allamet Esrandi")
stop94 = schedule.AddStop(lng=10.84359058, lat=33.79100383, name="Ben Arbi")
stop95 = schedule.AddStop(lng=10.84952238, lat=33.77588893, name="Ben Aissa")
stop96 = schedule.AddStop(lng=10.84178313, lat=33.78367698, name="Mosquet Ellil")
stop97 = schedule.AddStop(lng=10.83304015, lat=33.77948192, name="Ben Terdayet")
stop98 = schedule.AddStop(lng=10.82010427, lat=33.7734996, name="Srendi")
stop99 = schedule.AddStop(lng=10.81239456, lat=33.76755689, name="Elassayda")
stop100 = schedule.AddStop(lng=10.80833384, lat=33.78139014, name="Oued Ezbib")
stop101 = schedule.AddStop(lng=10.80612983, lat=33.78659348, name="Barbouch")
stop102 = schedule.AddStop(lng=10.74497447, lat=33.72092086, name="Ajim")
stop103 = schedule.AddStop(lng=10.76608698, lat=33.7285484, name="Hwanet Fadhel")
stop104 = schedule.AddStop(lng=10.77494565, lat=33.72929489, name="La methania")
stop105 = schedule.AddStop(lng=10.78341407, lat=33.72968436, name="Ben Azoun")
stop106 = schedule.AddStop(lng=10.84046858, lat=33.73179396, name="Elkhaway 1")
stop107 = schedule.AddStop(lng=10.84573695, lat=33.73189133, name="Elkhaway 2")
stop108 = schedule.AddStop(lng=10.85291755, lat=33.73039839, name="Gallala")
stop109 = schedule.AddStop(lng=10.85073215, lat=33.73834962, name="Tilouin")
stop110 = schedule.AddStop(lng=10.85900545, lat=33.72010938, name="Almakha")
stop111 = schedule.AddStop(lng=10.86193232, lat=33.71517541, name="Ben Ammar")
stop112 = schedule.AddStop(lng=10.86673239, lat=33.72910016, name="Elmat'haf")
stop113 = schedule.AddStop(lng=10.88644, lat=33.72955454, name="Oursighen 2")
stop114 = schedule.AddStop(lng=10.88819613, lat=33.73292988, name="Ben Mchichi")
stop115 = schedule.AddStop(lng=10.89326937, lat=33.73464995, name="Oursighen 1")
stop116 = schedule.AddStop(lng=10.91258674, lat=33.74260079, name="Tafertast")
stop117 = schedule.AddStop(lng=10.91172819, lat=33.74704644, name="Elhouch")
stop118 = schedule.AddStop(lng=10.91980636, lat=33.74341205, name="Sedwikech")
stop119 = schedule.AddStop(lng=10.92039173, lat=33.74701399, name="Dar Echabeb")
stop120 = schedule.AddStop(lng=10.92726013, lat=33.74097823, name="Zaatout")
stop121 = schedule.AddStop(lng=10.9328407, lat=33.74334715, name="Erraes")
stop122 = schedule.AddStop(lng=10.93943592, lat=33.75009661, name="Bounouh")
stop123 = schedule.AddStop(lng=10.94208962, lat=33.75437965, name="Edhira")
stop124 = schedule.AddStop(lng=10.94454819, lat=33.75853269, name="Ballagha")
stop125 = schedule.AddStop(lng=10.95469468, lat=33.7493503, name="Ben Thayer")
stop126 = schedule.AddStop(lng=10.96257773, lat=33.74737093, name="Bni Maaguel")
stop127 = schedule.AddStop(lng=10.96210943, lat=33.75197858, name="La poste")
stop128 = schedule.AddStop(lng=10.95348491, lat=33.76404814, name="Bir Bouaziz")
stop129 = schedule.AddStop(lng=10.95032389, lat=33.77173673, name="Elhajjam")
stop130 = schedule.AddStop(lng=10.94271402, lat=33.77669988, name="Bedouin")
stop131 = schedule.AddStop(lng=10.95059706, lat=33.78539281, name="Latrech")
stop132 = schedule.AddStop(lng=10.95789473, lat=33.79012815, name="Elkoucha")
stop133 = schedule.AddStop(lng=11.01354435, lat=33.75817579, name="Aguir")
stop134 = schedule.AddStop(lng=11.01147602, lat=33.76116068, name="Cap Jerba")
stop135 = schedule.AddStop(lng=11.0058174, lat=33.76943346, name="Elgassala")
stop136 = schedule.AddStop(lng=11.03130071, lat=33.77313163, name="Hari Club")
stop137 = schedule.AddStop(lng=11.02743724, lat=33.7701796, name="Sidi Slim")
stop138 = schedule.AddStop(lng=11.02310546, lat=33.76661108, name="Palmasur")
stop139 = schedule.AddStop(lng=11.02021762, lat=33.76437256, name="Diva")
stop140 = schedule.AddStop(lng=11.01658829, lat=33.76226376, name="Palmariva")
stop141 = schedule.AddStop(lng=10.91637216, lat=33.68069464, name="Elkantara")
stop142 = schedule.AddStop(lng=10.91250869, lat=33.71225385, name="Elmhamid")
stop143 = schedule.AddStop(lng=10.91340626, lat=33.71994708, name="Oued Ajmi")
stop144 = schedule.AddStop(lng=10.84620525, lat=33.74960989, name="Etlat")
stop145 = schedule.AddStop(lng=10.84636135, lat=33.75570994, name="Ezitouna")
stop146 = schedule.AddStop(lng=10.84487841, lat=33.76038202, name="Echaouchia")
stop147 = schedule.AddStop(lng=10.866682, lat=33.85203, name="Essouani")
stop148 = schedule.AddStop(lng=10.87982527, lat=33.85931195, name="Souk Ejoumla")
stop149 = schedule.AddStop(lng=10.88696684, lat=33.85658974, name="Houassa")
stop150 = schedule.AddStop(lng=10.89172789, lat=33.85539065, name="Echahben")
stop151 = schedule.AddStop(lng=10.89765968, lat=33.85467767, name="Elassas")
stop152 = schedule.AddStop(lng=10.90702568, lat=33.85276555, name="Hanout Salah")
stop153 = schedule.AddStop(lng=10.91725022, lat=33.847191, name="Elmajen")
stop154 = schedule.AddStop(lng=10.92497717, lat=33.84330156, name="Croisement Ibn Sina")
stop155 = schedule.AddStop(lng=10.93001139, lat=33.85837215, name="Guisen")
stop156 = schedule.AddStop(lng=10.92848941, lat=33.8628442, name="Ben Madi")
stop157 = schedule.AddStop(lng=10.92848941, lat=33.86673275, name="Elmestiri")
stop158 = schedule.AddStop(lng=10.95010925, lat=33.85458044, name="Mezraya")
stop159 = schedule.AddStop(lng=10.868151, lat=33.842877, name="Omajen 3")
stop160 = schedule.AddStop(lng=10.86944463, lat=33.83150251, name="Bir Ben Amor")
stop161 = schedule.AddStop(lng=10.870431, lat=33.823002, name="Allamet")
stop162 = schedule.AddStop(lng=10.8745569, lat=33.82566721, name="Walagh 1")
stop163 = schedule.AddStop(lng=10.87748377, lat=33.82625076, name="Walagh 2")
stop164 = schedule.AddStop(lng=10.88247897, lat=33.82725575, name="Elbkalti")
stop165 = schedule.AddStop(lng=10.88786441, lat=33.82887667, name="Bakir")
stop166 = schedule.AddStop(lng=10.89625478, lat=33.83137284, name="Denguir")
stop167 = schedule.AddStop(lng=10.90843058, lat=33.82164711, name="Tinisset")
stop168 = schedule.AddStop(lng=10.9084696, lat=33.82939536, name="Gachayin")
stop169 = schedule.AddStop(lng=10.90683055, lat=33.83396618, name="Mosquet Elyounsi")
stop170 = schedule.AddStop(lng=10.92478204, lat=33.82180921, name="Erramla")
stop171 = schedule.AddStop(lng=10.92138687, lat=33.82673705, name="Sadguyène 2")
stop172 = schedule.AddStop(lng=10.92290884, lat=33.83672152, name="Sadguyène 1")
stop173 = schedule.AddStop(lng=10.94974827, lat=33.82962229, name="Mosquet Boulaymane")
stop174 = schedule.AddStop(lng=10.876903, lat=33.812803, name="Ben Moussa")
stop175 = schedule.AddStop(lng=10.879975, lat=33.809331, name="Mosbah")
stop176 = schedule.AddStop(lng=10.85877585, lat=33.81477767, name="Elghriba")
stop177 = schedule.AddStop(lng=10.85862449, lat=33.81205302, name="Dyguet")
stop178 = schedule.AddStop(lng=10.8500982, lat=33.80865755, name="Zenkri")
stop179 = schedule.AddStop(lng=10.855069, lat=33.819634, name="Erriadh")
stop180 = schedule.AddStop(lng=10.85317574, lat=33.84989699, name="Elbassatin")
stop181 = schedule.AddStop(lng=10.85125859, lat=33.84072042, name="Errahba")
stop182 = schedule.AddStop(lng=10.85161175, lat=33.82990841, name="Ejadoui")
stop183 = schedule.AddStop(lng=10.8551938, lat=33.82324451, name="Elmakbara")
stop184 = schedule.AddStop(lng=10.8446999, lat=33.82102309, name="Eroua")
stop185 = schedule.AddStop(lng=10.83723309, lat=33.81892736, name="Elahouach")
stop186 = schedule.AddStop(lng=10.83360059, lat=33.81708308, name="Majin")
stop187 = schedule.AddStop(lng=10.85050181, lat=33.80433968, name="Eljenni")
stop188 = schedule.AddStop(lng=10.84545667, lat=33.79712875, name="Ezayat")
stop189 = schedule.AddStop(lng=10.7829726, lat=33.79870095, name="Elgroo")
stop190 = schedule.AddStop(lng=10.84956846, lat=33.86726272, name="Hnini")
stop191 = schedule.AddStop(lng=10.84755041, lat=33.86424649, name="Elbarkaoui")
stop192 = schedule.AddStop(lng=10.84533054, lat=33.86173288, name="Elhachen")
stop193 = schedule.AddStop(lng=10.84210165, lat=33.85779475, name="Sidi Hassen")
stop194 = schedule.AddStop(lng=10.83967999, lat=33.85469439, name="Saoud")
stop195 = schedule.AddStop(lng=10.83695561, lat=33.85276708, name="Jaballah 1")
stop196 = schedule.AddStop(lng=10.83443304, lat=33.85083973, name="Jaballah 2")
stop197 = schedule.AddStop(lng=10.83059873, lat=33.8469849, name="Slim")
stop198 = schedule.AddStop(lng=10.82293012, lat=33.83868803, name="Bazim")
stop199 = schedule.AddStop(lng=10.80375858, lat=33.75986962, name="Ben Yakhlef")
stop200 = schedule.AddStop(lng=10.79074212, lat=33.7516482, name="Elkhnansa")
stop201 = schedule.AddStop(lng=10.7795419, lat=33.7470338, name="Ben Marzoug")
stop202 = schedule.AddStop(lng=10.74624397, lat=33.73352475, name="Elkharouba")
stop203 = schedule.AddStop(lng=10.75038098, lat=33.74543967, name="Fekih Amor")
stop204 = schedule.AddStop(lng=10.75189453, lat=33.75030586, name="Bousmael")
stop205 = schedule.AddStop(lng=10.75401349, lat=33.75542344, name="Fekih Massaoud")
stop206 = schedule.AddStop(lng=10.75613245, lat=33.75903074, name="Bel Haj Yahyia")
stop207 = schedule.AddStop(lng=10.75996675, lat=33.76356061, name="26-26")
stop208 = schedule.AddStop(lng=10.76269113, lat=33.77010334, name="Mezran")
stop209 = schedule.AddStop(lng=10.76733266, lat=33.7785746, name="Ben Hafsia")
stop210 = schedule.AddStop(lng=10.77510218, lat=33.78813521, name="Eddaoula")
stop211 = schedule.AddStop(lng=10.79911705, lat=33.7893931, name="Elmaassra")
stop212 = schedule.AddStop(lng=10.79679628, lat=33.79140569, name="Karouia")
stop213 = schedule.AddStop(lng=10.79518184, lat=33.79316668, name="Elkhlifi")
stop214 = schedule.AddStop(lng=10.79205385, lat=33.79601771, name="Eljaabira")
stop215 = schedule.AddStop(lng=10.89069073, lat=33.78025017, name="Echhoud")
stop216 = schedule.AddStop(lng=10.89583677, lat=33.77437921, name="Robana")
stop217 = schedule.AddStop(lng=10.90421171, lat=33.76548813, name="Chnib")
stop218 = schedule.AddStop(lng=10.90915595, lat=33.76045503, name="Krouna")
stop219 = schedule.AddStop(lng=10.91510921, lat=33.75508607, name="Angar Hmida")
stop220 = schedule.AddStop(lng=10.86405238, lat=33.71103112, name="Elfahmin")
stop221 = schedule.AddStop(lng=10.862598, lat=33.868835, name="Lycée Technique")
stop222 = schedule.AddStop(lng=10.86498, lat=33.865279, name="Errahma")
stop223 = schedule.AddStop(lng=10.8896973, lat=33.799251, name="Le Collège")


route = schedule.AddRoute(short_name="SU410", long_name="Houmet Souk, ElMay, Mahboubine, Midoun, Aguir, Djerba La Fidele",
                          route_type="Bus")

trip = route.AddTrip(schedule, headsign="Houmet Souk vers Djerba La Fidele")
trip.AddStopTime(stop10, stop_time='06:30:00') # Houmet Souk - 0
trip.AddStopTime(stop221, stop_time='06:32:00') # Lycée Technique - 123
trip.AddStopTime(stop222, stop_time='06:33:00') # Errahma - 79
trip.AddStopTime(stop147, stop_time='06:35:00') # Essouani - 118
trip.AddStopTime(stop159, stop_time='06:36:00') # Omajen 3 - 83
trip.AddStopTime(stop160, stop_time='06:38:00') # Bir Ben Amor - 94
trip.AddStopTime(stop161, stop_time='06:39:00') # Allamet - 63
trip.AddStopTime(stop174, stop_time='06:40:00') # Ben Moussa - 72
trip.AddStopTime(stop175, stop_time='06:40:00') # Mosbah - 26
trip.AddStopTime(stop90, stop_time='06:42:00') # Elmay - 145
trip.AddStopTime(stop223, stop_time='06:43:00') # Le Collège - 61
trip.AddStopTime(stop89, stop_time='06:45:00') # ElKabou - 96
trip.AddStopTime(stop88, stop_time='06:46:00') # Hadj Dahmane - 38
trip.AddStopTime(stop87, stop_time='06:47:00') # Ben Hamouda - 39
trip.AddStopTime(stop86, stop_time='06:48:00') # Elhazem - 38
trip.AddStopTime(stop85, stop_time='06:49:00') # Elhajra elbidha - 77
trip.AddStopTime(stop84, stop_time='06:50:00') # elmehrab - 39
trip.AddStopTime(stop83, stop_time='06:51:00') # Ettouta - 83
trip.AddStopTime(stop82, stop_time='06:52:00') # Elweryemmi - 47
trip.AddStopTime(stop51, stop_time='06:54:00') # Mahboubine - 97
trip.AddStopTime(stop50, stop_time='06:55:00') # Boufaden - 53
trip.AddStopTime(stop47, stop_time='06:57:00') # Hadher bach - 115
trip.AddStopTime(stop46, stop_time='06:58:00') # Midoun - 85
trip.AddStopTime(stop52, stop_time='07:01:00') # Mosquet Ben Ammar - 180
trip.AddStopTime(stop53, stop_time='07:04:00') # Essaegh - 209
trip.AddStopTime(stop54, stop_time='07:06:00') # Elazmouni - 124
trip.AddStopTime(stop55, stop_time='07:07:00') # Mosquet Arko - 77
trip.AddStopTime(stop56, stop_time='07:09:00') # Arko - 126
trip.AddStopTime(stop57, stop_time='07:10:00') # Elwachnia - 73
trip.AddStopTime(stop58, stop_time='07:12:00') # Elmoustaoussef - 92
trip.AddStopTime(stop135, stop_time='07:18:00') # Elgassala - 369
trip.AddStopTime(stop134, stop_time='07:20:00') # Cap Jerba - 139
trip.AddStopTime(stop133, stop_time='07:22:00') # Aguir - 92
trip.AddStopTime(stop140, stop_time='07:23:00') # Palmariva - 44
trip.AddStopTime(stop139, stop_time='07:23:00') # Diva - 29
trip.AddStopTime(stop138, stop_time='07:23:00') # Palmasur - 25
trip.AddStopTime(stop137, stop_time='07:24:00') # Sidi Slim - 37
trip.AddStopTime(stop136, stop_time='07:25:00') # Hari Club - 39
trip.AddStopTime(stop59, stop_time='07:26:00') # Elmaamoura - 78
trip.AddStopTime(stop60, stop_time='07:27:00') # Carthago - 63
trip.AddStopTime(stop61, stop_time='07:28:00') # Calipso - 33
trip.AddStopTime(stop62, stop_time='07:30:00') # Jerba La douce - 112
trip.AddStopTime(stop63, stop_time='07:31:00') # Jerba Menzel - 32
trip.AddStopTime(stop64, stop_time='07:31:00') # Jerba La fidèle - 19

trip = route.AddTrip(schedule, headsign="Djerba La Fidele Vers Houmet Souk")
trip.AddStopTime(stop64, stop_time='06:35:00') # Jerba La fidèle - 0
trip.AddStopTime(stop63, stop_time='06:35:00') # Jerba Menzel - 19
trip.AddStopTime(stop62, stop_time='06:36:00') # Jerba La douce - 33
trip.AddStopTime(stop61, stop_time='06:37:00') # Calipso - 44
trip.AddStopTime(stop60, stop_time='06:38:00') # Carthago - 89
trip.AddStopTime(stop59, stop_time='06:38:00') # Elmaamoura - 29
trip.AddStopTime(stop136, stop_time='06:39:00') # Hari Club - 74
trip.AddStopTime(stop137, stop_time='06:40:00') # Sidi Slim - 66
trip.AddStopTime(stop138, stop_time='06:41:00') # Palmasur - 37
trip.AddStopTime(stop139, stop_time='06:41:00') # Diva - 25
trip.AddStopTime(stop140, stop_time='06:41:00') # Palmariva - 29
trip.AddStopTime(stop133, stop_time='06:42:00') # Aguir - 44
trip.AddStopTime(stop134, stop_time='06:43:00') # Cap Jerba - 75
trip.AddStopTime(stop135, stop_time='06:44:00') # Elgassala - 55
trip.AddStopTime(stop58, stop_time='06:50:00') # Elmoustaoussef - 349
trip.AddStopTime(stop57, stop_time='06:52:00') # Elwachnia - 92
trip.AddStopTime(stop56, stop_time='06:53:00') # Arko - 73
trip.AddStopTime(stop55, stop_time='06:55:00') # Mosquet Arko - 120
trip.AddStopTime(stop54, stop_time='06:57:00') # Elazmouni - 110
trip.AddStopTime(stop53, stop_time='06:58:00') # Essaegh - 66
trip.AddStopTime(stop52, stop_time='06:59:00') # Mosquet Ben Ammar - 34
trip.AddStopTime(stop46, stop_time='07:01:00') # Midoun - 114
trip.AddStopTime(stop47, stop_time='07:03:00') # Hadher bach - 146
trip.AddStopTime(stop50, stop_time='07:05:00') # Boufaden - 116
trip.AddStopTime(stop51, stop_time='07:06:00') # Mahboubine - 53
trip.AddStopTime(stop82, stop_time='07:08:00') # Elweryemmi - 101
trip.AddStopTime(stop83, stop_time='07:09:00') # Ettouta - 47
trip.AddStopTime(stop84, stop_time='07:10:00') # elmehrab - 83
trip.AddStopTime(stop85, stop_time='07:11:00') # Elhajra elbidha - 42
trip.AddStopTime(stop86, stop_time='07:12:00') # Elhazem - 67
trip.AddStopTime(stop87, stop_time='07:13:00') # Ben Hamouda - 39
trip.AddStopTime(stop88, stop_time='07:14:00') # Hadj Dahmane - 41
trip.AddStopTime(stop89, stop_time='07:15:00') # ElKabou - 38
trip.AddStopTime(stop223, stop_time='07:17:00') # Le Collège - 92
trip.AddStopTime(stop90, stop_time='07:18:00') # Elmay - 58
trip.AddStopTime(stop175, stop_time='07:20:00') # Mosbah - 121
trip.AddStopTime(stop174, stop_time='07:20:00') # Ben Moussa - 26
trip.AddStopTime(stop161, stop_time='07:21:00') # Allamet - 72
trip.AddStopTime(stop160, stop_time='07:22:00') # Bir Ben Amor - 61
trip.AddStopTime(stop159, stop_time='07:24:00') # Omajen 3 - 92
trip.AddStopTime(stop147, stop_time='07:25:00') # Essouani - 83
trip.AddStopTime(stop222, stop_time='07:27:00') # Errahma - 118
trip.AddStopTime(stop221, stop_time='07:28:00') # Lycée Technique - 75
trip.AddStopTime(stop10, stop_time='07:31:00') # Houmet Souk - 159

trip = route.AddTrip(schedule, headsign="Houmet Souk vers Djerba La Fidele")
trip.AddStopTime(stop10, stop_time='07:00:00') # Houmet Souk - 0
trip.AddStopTime(stop221, stop_time='07:02:00') # Lycée Technique - 123
trip.AddStopTime(stop222, stop_time='07:03:00') # Errahma - 79
trip.AddStopTime(stop147, stop_time='07:05:00') # Essouani - 118
trip.AddStopTime(stop159, stop_time='07:06:00') # Omajen 3 - 83
trip.AddStopTime(stop160, stop_time='07:08:00') # Bir Ben Amor - 94
trip.AddStopTime(stop161, stop_time='07:09:00') # Allamet - 63
trip.AddStopTime(stop174, stop_time='07:10:00') # Ben Moussa - 72
trip.AddStopTime(stop175, stop_time='07:10:00') # Mosbah - 26
trip.AddStopTime(stop90, stop_time='07:12:00') # Elmay - 145
trip.AddStopTime(stop223, stop_time='07:13:00') # Le Collège - 61
trip.AddStopTime(stop89, stop_time='07:15:00') # ElKabou - 96
trip.AddStopTime(stop88, stop_time='07:16:00') # Hadj Dahmane - 38
trip.AddStopTime(stop87, stop_time='07:17:00') # Ben Hamouda - 39
trip.AddStopTime(stop86, stop_time='07:18:00') # Elhazem - 38
trip.AddStopTime(stop85, stop_time='07:19:00') # Elhajra elbidha - 77
trip.AddStopTime(stop84, stop_time='07:20:00') # elmehrab - 39
trip.AddStopTime(stop83, stop_time='07:21:00') # Ettouta - 83
trip.AddStopTime(stop82, stop_time='07:22:00') # Elweryemmi - 47
trip.AddStopTime(stop51, stop_time='07:24:00') # Mahboubine - 97
trip.AddStopTime(stop50, stop_time='07:25:00') # Boufaden - 53
trip.AddStopTime(stop47, stop_time='07:27:00') # Hadher bach - 115
trip.AddStopTime(stop46, stop_time='07:28:00') # Midoun - 85
trip.AddStopTime(stop52, stop_time='07:31:00') # Mosquet Ben Ammar - 180
trip.AddStopTime(stop53, stop_time='07:34:00') # Essaegh - 209
trip.AddStopTime(stop54, stop_time='07:36:00') # Elazmouni - 124
trip.AddStopTime(stop55, stop_time='07:37:00') # Mosquet Arko - 77
trip.AddStopTime(stop56, stop_time='07:39:00') # Arko - 126
trip.AddStopTime(stop57, stop_time='07:40:00') # Elwachnia - 73
trip.AddStopTime(stop58, stop_time='07:42:00') # Elmoustaoussef - 92
trip.AddStopTime(stop135, stop_time='07:48:00') # Elgassala - 369
trip.AddStopTime(stop134, stop_time='07:50:00') # Cap Jerba - 139
trip.AddStopTime(stop133, stop_time='07:52:00') # Aguir - 92
trip.AddStopTime(stop140, stop_time='07:53:00') # Palmariva - 44
trip.AddStopTime(stop139, stop_time='07:53:00') # Diva - 29
trip.AddStopTime(stop138, stop_time='07:53:00') # Palmasur - 25
trip.AddStopTime(stop137, stop_time='07:54:00') # Sidi Slim - 37
trip.AddStopTime(stop136, stop_time='07:55:00') # Hari Club - 39
trip.AddStopTime(stop59, stop_time='07:56:00') # Elmaamoura - 78
trip.AddStopTime(stop60, stop_time='07:57:00') # Carthago - 63
trip.AddStopTime(stop61, stop_time='07:58:00') # Calipso - 33
trip.AddStopTime(stop62, stop_time='08:00:00') # Jerba La douce - 112
trip.AddStopTime(stop63, stop_time='08:01:00') # Jerba Menzel - 32
trip.AddStopTime(stop64, stop_time='08:01:00') # Jerba La fidèle - 19

trip = route.AddTrip(schedule, headsign="Djerba La Fidele Vers Houmet Souk")
trip.AddStopTime(stop64, stop_time='07:50:00') # Jerba La fidèle - 0
trip.AddStopTime(stop63, stop_time='07:50:00') # Jerba Menzel - 19
trip.AddStopTime(stop62, stop_time='07:51:00') # Jerba La douce - 33
trip.AddStopTime(stop61, stop_time='07:52:00') # Calipso - 44
trip.AddStopTime(stop60, stop_time='07:53:00') # Carthago - 89
trip.AddStopTime(stop59, stop_time='07:53:00') # Elmaamoura - 29
trip.AddStopTime(stop136, stop_time='07:54:00') # Hari Club - 74
trip.AddStopTime(stop137, stop_time='07:55:00') # Sidi Slim - 66
trip.AddStopTime(stop138, stop_time='07:56:00') # Palmasur - 37
trip.AddStopTime(stop139, stop_time='07:56:00') # Diva - 25
trip.AddStopTime(stop140, stop_time='07:56:00') # Palmariva - 29
trip.AddStopTime(stop133, stop_time='07:57:00') # Aguir - 44
trip.AddStopTime(stop134, stop_time='07:58:00') # Cap Jerba - 75
trip.AddStopTime(stop135, stop_time='07:59:00') # Elgassala - 55
trip.AddStopTime(stop58, stop_time='08:05:00') # Elmoustaoussef - 349
trip.AddStopTime(stop57, stop_time='08:07:00') # Elwachnia - 92
trip.AddStopTime(stop56, stop_time='08:08:00') # Arko - 73
trip.AddStopTime(stop55, stop_time='08:10:00') # Mosquet Arko - 120
trip.AddStopTime(stop54, stop_time='08:12:00') # Elazmouni - 110
trip.AddStopTime(stop53, stop_time='08:13:00') # Essaegh - 66
trip.AddStopTime(stop52, stop_time='08:14:00') # Mosquet Ben Ammar - 34
trip.AddStopTime(stop46, stop_time='08:16:00') # Midoun - 114
trip.AddStopTime(stop47, stop_time='08:18:00') # Hadher bach - 146
trip.AddStopTime(stop50, stop_time='08:20:00') # Boufaden - 116
trip.AddStopTime(stop51, stop_time='08:21:00') # Mahboubine - 53
trip.AddStopTime(stop82, stop_time='08:23:00') # Elweryemmi - 101
trip.AddStopTime(stop83, stop_time='08:24:00') # Ettouta - 47
trip.AddStopTime(stop84, stop_time='08:25:00') # elmehrab - 83
trip.AddStopTime(stop85, stop_time='08:26:00') # Elhajra elbidha - 42
trip.AddStopTime(stop86, stop_time='08:27:00') # Elhazem - 67
trip.AddStopTime(stop87, stop_time='08:28:00') # Ben Hamouda - 39
trip.AddStopTime(stop88, stop_time='08:29:00') # Hadj Dahmane - 41
trip.AddStopTime(stop89, stop_time='08:30:00') # ElKabou - 38
trip.AddStopTime(stop223, stop_time='08:32:00') # Le Collège - 92
trip.AddStopTime(stop90, stop_time='08:33:00') # Elmay - 58
trip.AddStopTime(stop175, stop_time='08:35:00') # Mosbah - 121
trip.AddStopTime(stop174, stop_time='08:35:00') # Ben Moussa - 26
trip.AddStopTime(stop161, stop_time='08:36:00') # Allamet - 72
trip.AddStopTime(stop160, stop_time='08:37:00') # Bir Ben Amor - 61
trip.AddStopTime(stop159, stop_time='08:39:00') # Omajen 3 - 92
trip.AddStopTime(stop147, stop_time='08:40:00') # Essouani - 83
trip.AddStopTime(stop222, stop_time='08:42:00') # Errahma - 118
trip.AddStopTime(stop221, stop_time='08:43:00') # Lycée Technique - 75
trip.AddStopTime(stop10, stop_time='08:46:00') # Houmet Souk - 159


trip = route.AddTrip(schedule, headsign="Houmet Souk vers Jerba La fidèle")
trip.AddStopTime(stop10, stop_time='08:30:00') # Houmet Souk - 0
trip.AddStopTime(stop221, stop_time='08:32:00') # Lycée Technique - 123
trip.AddStopTime(stop222, stop_time='08:33:00') # Errahma - 79
trip.AddStopTime(stop147, stop_time='08:35:00') # Essouani - 118
trip.AddStopTime(stop159, stop_time='08:36:00') # Omajen 3 - 83
trip.AddStopTime(stop160, stop_time='08:38:00') # Bir Ben Amor - 94
trip.AddStopTime(stop161, stop_time='08:39:00') # Allamet - 63
trip.AddStopTime(stop174, stop_time='08:40:00') # Ben Moussa - 72
trip.AddStopTime(stop175, stop_time='08:40:00') # Mosbah - 26
trip.AddStopTime(stop90, stop_time='08:42:00') # Elmay - 145
trip.AddStopTime(stop223, stop_time='08:43:00') # Le Collège - 61
trip.AddStopTime(stop89, stop_time='08:45:00') # ElKabou - 96
trip.AddStopTime(stop88, stop_time='08:46:00') # Hadj Dahmane - 38
trip.AddStopTime(stop87, stop_time='08:47:00') # Ben Hamouda - 39
trip.AddStopTime(stop86, stop_time='08:48:00') # Elhazem - 38
trip.AddStopTime(stop85, stop_time='08:49:00') # Elhajra elbidha - 77
trip.AddStopTime(stop84, stop_time='08:50:00') # elmehrab - 39
trip.AddStopTime(stop83, stop_time='08:51:00') # Ettouta - 83
trip.AddStopTime(stop82, stop_time='08:52:00') # Elweryemmi - 47
trip.AddStopTime(stop51, stop_time='08:54:00') # Mahboubine - 97
trip.AddStopTime(stop50, stop_time='08:55:00') # Boufaden - 53
trip.AddStopTime(stop47, stop_time='08:57:00') # Hadher bach - 115
trip.AddStopTime(stop46, stop_time='08:58:00') # Midoun - 85
trip.AddStopTime(stop52, stop_time='09:01:00') # Mosquet Ben Ammar - 180
trip.AddStopTime(stop53, stop_time='09:04:00') # Essaegh - 209
trip.AddStopTime(stop54, stop_time='09:06:00') # Elazmouni - 124
trip.AddStopTime(stop55, stop_time='09:07:00') # Mosquet Arko - 77
trip.AddStopTime(stop56, stop_time='09:09:00') # Arko - 126
trip.AddStopTime(stop57, stop_time='09:10:00') # Elwachnia - 73
trip.AddStopTime(stop58, stop_time='09:12:00') # Elmoustaoussef - 92
trip.AddStopTime(stop135, stop_time='09:18:00') # Elgassala - 369
trip.AddStopTime(stop134, stop_time='09:20:00') # Cap Jerba - 139
trip.AddStopTime(stop133, stop_time='09:22:00') # Aguir - 92
trip.AddStopTime(stop140, stop_time='09:23:00') # Palmariva - 44
trip.AddStopTime(stop139, stop_time='09:23:00') # Diva - 29
trip.AddStopTime(stop138, stop_time='09:23:00') # Palmasur - 25
trip.AddStopTime(stop137, stop_time='09:24:00') # Sidi Slim - 37
trip.AddStopTime(stop136, stop_time='09:25:00') # Hari Club - 39
trip.AddStopTime(stop59, stop_time='09:26:00') # Elmaamoura - 78
trip.AddStopTime(stop60, stop_time='09:27:00') # Carthago - 63
trip.AddStopTime(stop61, stop_time='09:28:00') # Calipso - 33
trip.AddStopTime(stop62, stop_time='09:30:00') # Jerba La douce - 112
trip.AddStopTime(stop63, stop_time='09:31:00') # Jerba Menzel - 32
trip.AddStopTime(stop64, stop_time='09:31:00') # Jerba La fidèle - 19

trip = route.AddTrip(schedule, headsign="Jerba La fidèle vers Houmet Souk")
trip.AddStopTime(stop64, stop_time='09:30:00') # Jerba La fidèle - 0
trip.AddStopTime(stop63, stop_time='09:30:00') # Jerba Menzel - 19
trip.AddStopTime(stop62, stop_time='09:31:00') # Jerba La douce - 33
trip.AddStopTime(stop61, stop_time='09:32:00') # Calipso - 44
trip.AddStopTime(stop60, stop_time='09:33:00') # Carthago - 89
trip.AddStopTime(stop59, stop_time='09:33:00') # Elmaamoura - 29
trip.AddStopTime(stop136, stop_time='09:34:00') # Hari Club - 74
trip.AddStopTime(stop137, stop_time='09:35:00') # Sidi Slim - 66
trip.AddStopTime(stop138, stop_time='09:36:00') # Palmasur - 37
trip.AddStopTime(stop139, stop_time='09:36:00') # Diva - 25
trip.AddStopTime(stop140, stop_time='09:36:00') # Palmariva - 29
trip.AddStopTime(stop133, stop_time='09:37:00') # Aguir - 44
trip.AddStopTime(stop134, stop_time='09:38:00') # Cap Jerba - 75
trip.AddStopTime(stop135, stop_time='09:39:00') # Elgassala - 55
trip.AddStopTime(stop58, stop_time='09:45:00') # Elmoustaoussef - 349
trip.AddStopTime(stop57, stop_time='09:47:00') # Elwachnia - 92
trip.AddStopTime(stop56, stop_time='09:48:00') # Arko - 73
trip.AddStopTime(stop55, stop_time='09:50:00') # Mosquet Arko - 120
trip.AddStopTime(stop54, stop_time='09:52:00') # Elazmouni - 110
trip.AddStopTime(stop53, stop_time='09:53:00') # Essaegh - 66
trip.AddStopTime(stop52, stop_time='09:54:00') # Mosquet Ben Ammar - 34
trip.AddStopTime(stop46, stop_time='09:56:00') # Midoun - 114
trip.AddStopTime(stop47, stop_time='09:58:00') # Hadher bach - 146
trip.AddStopTime(stop50, stop_time='10:00:00') # Boufaden - 116
trip.AddStopTime(stop51, stop_time='10:01:00') # Mahboubine - 53
trip.AddStopTime(stop82, stop_time='10:03:00') # Elweryemmi - 101
trip.AddStopTime(stop83, stop_time='10:04:00') # Ettouta - 47
trip.AddStopTime(stop84, stop_time='10:05:00') # elmehrab - 83
trip.AddStopTime(stop85, stop_time='10:06:00') # Elhajra elbidha - 42
trip.AddStopTime(stop86, stop_time='10:07:00') # Elhazem - 67
trip.AddStopTime(stop87, stop_time='10:08:00') # Ben Hamouda - 39
trip.AddStopTime(stop88, stop_time='10:09:00') # Hadj Dahmane - 41
trip.AddStopTime(stop89, stop_time='10:10:00') # ElKabou - 38
trip.AddStopTime(stop223, stop_time='10:12:00') # Le Collège - 92
trip.AddStopTime(stop90, stop_time='10:13:00') # Elmay - 58
trip.AddStopTime(stop175, stop_time='10:15:00') # Mosbah - 121
trip.AddStopTime(stop174, stop_time='10:15:00') # Ben Moussa - 26
trip.AddStopTime(stop161, stop_time='10:16:00') # Allamet - 72
trip.AddStopTime(stop160, stop_time='10:17:00') # Bir Ben Amor - 61
trip.AddStopTime(stop159, stop_time='10:19:00') # Omajen 3 - 92
trip.AddStopTime(stop147, stop_time='10:20:00') # Essouani - 83
trip.AddStopTime(stop222, stop_time='10:22:00') # Errahma - 118
trip.AddStopTime(stop221, stop_time='10:23:00') # Lycée Technique - 75
trip.AddStopTime(stop10, stop_time='10:26:00') # Houmet Souk - 159


trip = route.AddTrip(schedule, headsign="Houmet Souk vers Jerba La fidèle")
trip.AddStopTime(stop10, stop_time='10:00:00') # Houmet Souk - 0
trip.AddStopTime(stop221, stop_time='10:02:00') # Lycée Technique - 123
trip.AddStopTime(stop222, stop_time='10:03:00') # Errahma - 79
trip.AddStopTime(stop147, stop_time='10:05:00') # Essouani - 118
trip.AddStopTime(stop159, stop_time='10:06:00') # Omajen 3 - 83
trip.AddStopTime(stop160, stop_time='10:08:00') # Bir Ben Amor - 94
trip.AddStopTime(stop161, stop_time='10:09:00') # Allamet - 63
trip.AddStopTime(stop174, stop_time='10:10:00') # Ben Moussa - 72
trip.AddStopTime(stop175, stop_time='10:10:00') # Mosbah - 26
trip.AddStopTime(stop90, stop_time='10:12:00') # Elmay - 145
trip.AddStopTime(stop223, stop_time='10:13:00') # Le Collège - 61
trip.AddStopTime(stop89, stop_time='10:15:00') # ElKabou - 96
trip.AddStopTime(stop88, stop_time='10:16:00') # Hadj Dahmane - 38
trip.AddStopTime(stop87, stop_time='10:17:00') # Ben Hamouda - 39
trip.AddStopTime(stop86, stop_time='10:18:00') # Elhazem - 38
trip.AddStopTime(stop85, stop_time='10:19:00') # Elhajra elbidha - 77
trip.AddStopTime(stop84, stop_time='10:20:00') # elmehrab - 39
trip.AddStopTime(stop83, stop_time='10:21:00') # Ettouta - 83
trip.AddStopTime(stop82, stop_time='10:22:00') # Elweryemmi - 47
trip.AddStopTime(stop51, stop_time='10:24:00') # Mahboubine - 97
trip.AddStopTime(stop50, stop_time='10:25:00') # Boufaden - 53
trip.AddStopTime(stop47, stop_time='10:27:00') # Hadher bach - 115
trip.AddStopTime(stop46, stop_time='10:28:00') # Midoun - 85
trip.AddStopTime(stop52, stop_time='10:31:00') # Mosquet Ben Ammar - 180
trip.AddStopTime(stop53, stop_time='10:34:00') # Essaegh - 209
trip.AddStopTime(stop54, stop_time='10:36:00') # Elazmouni - 124
trip.AddStopTime(stop55, stop_time='10:37:00') # Mosquet Arko - 77
trip.AddStopTime(stop56, stop_time='10:39:00') # Arko - 126
trip.AddStopTime(stop57, stop_time='10:40:00') # Elwachnia - 73
trip.AddStopTime(stop58, stop_time='10:42:00') # Elmoustaoussef - 92
trip.AddStopTime(stop135, stop_time='10:48:00') # Elgassala - 369
trip.AddStopTime(stop134, stop_time='10:50:00') # Cap Jerba - 139
trip.AddStopTime(stop133, stop_time='10:52:00') # Aguir - 92
trip.AddStopTime(stop140, stop_time='10:53:00') # Palmariva - 44
trip.AddStopTime(stop139, stop_time='10:53:00') # Diva - 29
trip.AddStopTime(stop138, stop_time='10:53:00') # Palmasur - 25
trip.AddStopTime(stop137, stop_time='10:54:00') # Sidi Slim - 37
trip.AddStopTime(stop136, stop_time='10:55:00') # Hari Club - 39
trip.AddStopTime(stop59, stop_time='10:56:00') # Elmaamoura - 78
trip.AddStopTime(stop60, stop_time='10:57:00') # Carthago - 63
trip.AddStopTime(stop61, stop_time='10:58:00') # Calipso - 33
trip.AddStopTime(stop62, stop_time='11:00:00') # Jerba La douce - 112
trip.AddStopTime(stop63, stop_time='11:01:00') # Jerba Menzel - 32
trip.AddStopTime(stop64, stop_time='11:01:00') # Jerba La fidèle - 19

trip = route.AddTrip(schedule, headsign="Jerba La fidèle vers Houmet Souk")
trip.AddStopTime(stop64, stop_time='11:00:00') # Jerba La fidèle - 0
trip.AddStopTime(stop63, stop_time='11:00:00') # Jerba Menzel - 19
trip.AddStopTime(stop62, stop_time='11:01:00') # Jerba La douce - 33
trip.AddStopTime(stop61, stop_time='11:02:00') # Calipso - 44
trip.AddStopTime(stop60, stop_time='11:03:00') # Carthago - 89
trip.AddStopTime(stop59, stop_time='11:03:00') # Elmaamoura - 29
trip.AddStopTime(stop136, stop_time='11:04:00') # Hari Club - 74
trip.AddStopTime(stop137, stop_time='11:05:00') # Sidi Slim - 66
trip.AddStopTime(stop138, stop_time='11:06:00') # Palmasur - 37
trip.AddStopTime(stop139, stop_time='11:06:00') # Diva - 25
trip.AddStopTime(stop140, stop_time='11:06:00') # Palmariva - 29
trip.AddStopTime(stop133, stop_time='11:07:00') # Aguir - 44
trip.AddStopTime(stop134, stop_time='11:08:00') # Cap Jerba - 75
trip.AddStopTime(stop135, stop_time='11:09:00') # Elgassala - 55
trip.AddStopTime(stop58, stop_time='11:15:00') # Elmoustaoussef - 349
trip.AddStopTime(stop57, stop_time='11:17:00') # Elwachnia - 92
trip.AddStopTime(stop56, stop_time='11:18:00') # Arko - 73
trip.AddStopTime(stop55, stop_time='11:20:00') # Mosquet Arko - 120
trip.AddStopTime(stop54, stop_time='11:22:00') # Elazmouni - 110
trip.AddStopTime(stop53, stop_time='11:23:00') # Essaegh - 66
trip.AddStopTime(stop52, stop_time='11:24:00') # Mosquet Ben Ammar - 34
trip.AddStopTime(stop46, stop_time='11:26:00') # Midoun - 114
trip.AddStopTime(stop47, stop_time='11:28:00') # Hadher bach - 146
trip.AddStopTime(stop50, stop_time='11:30:00') # Boufaden - 116
trip.AddStopTime(stop51, stop_time='11:31:00') # Mahboubine - 53
trip.AddStopTime(stop82, stop_time='11:33:00') # Elweryemmi - 101
trip.AddStopTime(stop83, stop_time='11:34:00') # Ettouta - 47
trip.AddStopTime(stop84, stop_time='11:35:00') # elmehrab - 83
trip.AddStopTime(stop85, stop_time='11:36:00') # Elhajra elbidha - 42
trip.AddStopTime(stop86, stop_time='11:37:00') # Elhazem - 67
trip.AddStopTime(stop87, stop_time='11:38:00') # Ben Hamouda - 39
trip.AddStopTime(stop88, stop_time='11:39:00') # Hadj Dahmane - 41
trip.AddStopTime(stop89, stop_time='11:40:00') # ElKabou - 38
trip.AddStopTime(stop223, stop_time='11:42:00') # Le Collège - 92
trip.AddStopTime(stop90, stop_time='11:43:00') # Elmay - 58
trip.AddStopTime(stop175, stop_time='11:45:00') # Mosbah - 121
trip.AddStopTime(stop174, stop_time='11:45:00') # Ben Moussa - 26
trip.AddStopTime(stop161, stop_time='11:46:00') # Allamet - 72
trip.AddStopTime(stop160, stop_time='11:47:00') # Bir Ben Amor - 61
trip.AddStopTime(stop159, stop_time='11:49:00') # Omajen 3 - 92
trip.AddStopTime(stop147, stop_time='11:50:00') # Essouani - 83
trip.AddStopTime(stop222, stop_time='11:52:00') # Errahma - 118
trip.AddStopTime(stop221, stop_time='11:53:00') # Lycée Technique - 75
trip.AddStopTime(stop10, stop_time='11:56:00') # Houmet Souk - 159

trip = route.AddTrip(schedule, headsign="Houmet Souk vers Jerba La fidèle")
trip.AddStopTime(stop10, stop_time='11:15:00') # Houmet Souk - 0
trip.AddStopTime(stop221, stop_time='11:17:00') # Lycée Technique - 123
trip.AddStopTime(stop222, stop_time='11:18:00') # Errahma - 79
trip.AddStopTime(stop147, stop_time='11:20:00') # Essouani - 118
trip.AddStopTime(stop159, stop_time='11:21:00') # Omajen 3 - 83
trip.AddStopTime(stop160, stop_time='11:23:00') # Bir Ben Amor - 94
trip.AddStopTime(stop161, stop_time='11:24:00') # Allamet - 63
trip.AddStopTime(stop174, stop_time='11:25:00') # Ben Moussa - 72
trip.AddStopTime(stop175, stop_time='11:25:00') # Mosbah - 26
trip.AddStopTime(stop90, stop_time='11:27:00') # Elmay - 145
trip.AddStopTime(stop223, stop_time='11:28:00') # Le Collège - 61
trip.AddStopTime(stop89, stop_time='11:30:00') # ElKabou - 96
trip.AddStopTime(stop88, stop_time='11:31:00') # Hadj Dahmane - 38
trip.AddStopTime(stop87, stop_time='11:32:00') # Ben Hamouda - 39
trip.AddStopTime(stop86, stop_time='11:33:00') # Elhazem - 38
trip.AddStopTime(stop85, stop_time='11:34:00') # Elhajra elbidha - 77
trip.AddStopTime(stop84, stop_time='11:35:00') # elmehrab - 39
trip.AddStopTime(stop83, stop_time='11:36:00') # Ettouta - 83
trip.AddStopTime(stop82, stop_time='11:37:00') # Elweryemmi - 47
trip.AddStopTime(stop51, stop_time='11:39:00') # Mahboubine - 97
trip.AddStopTime(stop50, stop_time='11:40:00') # Boufaden - 53
trip.AddStopTime(stop47, stop_time='11:42:00') # Hadher bach - 115
trip.AddStopTime(stop46, stop_time='11:43:00') # Midoun - 85
trip.AddStopTime(stop52, stop_time='11:46:00') # Mosquet Ben Ammar - 180
trip.AddStopTime(stop53, stop_time='11:49:00') # Essaegh - 209
trip.AddStopTime(stop54, stop_time='11:51:00') # Elazmouni - 124
trip.AddStopTime(stop55, stop_time='11:52:00') # Mosquet Arko - 77
trip.AddStopTime(stop56, stop_time='11:54:00') # Arko - 126
trip.AddStopTime(stop57, stop_time='11:55:00') # Elwachnia - 73
trip.AddStopTime(stop58, stop_time='11:57:00') # Elmoustaoussef - 92
trip.AddStopTime(stop135, stop_time='12:03:00') # Elgassala - 369
trip.AddStopTime(stop134, stop_time='12:05:00') # Cap Jerba - 139
trip.AddStopTime(stop133, stop_time='12:07:00') # Aguir - 92
trip.AddStopTime(stop140, stop_time='12:08:00') # Palmariva - 44
trip.AddStopTime(stop139, stop_time='12:08:00') # Diva - 29
trip.AddStopTime(stop138, stop_time='12:08:00') # Palmasur - 25
trip.AddStopTime(stop137, stop_time='12:09:00') # Sidi Slim - 37
trip.AddStopTime(stop136, stop_time='12:10:00') # Hari Club - 39
trip.AddStopTime(stop59, stop_time='12:11:00') # Elmaamoura - 78
trip.AddStopTime(stop60, stop_time='12:12:00') # Carthago - 63
trip.AddStopTime(stop61, stop_time='12:13:00') # Calipso - 33
trip.AddStopTime(stop62, stop_time='12:15:00') # Jerba La douce - 112
trip.AddStopTime(stop63, stop_time='12:16:00') # Jerba Menzel - 32
trip.AddStopTime(stop64, stop_time='12:16:00') # Jerba La fidèle - 19

trip = route.AddTrip(schedule, headsign="Jerba La fidèle vers Houmet Souk")
trip.AddStopTime(stop64, stop_time='13:20:00') # Jerba La fidèle - 0
trip.AddStopTime(stop63, stop_time='13:20:00') # Jerba Menzel - 19
trip.AddStopTime(stop62, stop_time='13:21:00') # Jerba La douce - 33
trip.AddStopTime(stop61, stop_time='13:22:00') # Calipso - 44
trip.AddStopTime(stop60, stop_time='13:23:00') # Carthago - 89
trip.AddStopTime(stop59, stop_time='13:23:00') # Elmaamoura - 29
trip.AddStopTime(stop136, stop_time='13:24:00') # Hari Club - 74
trip.AddStopTime(stop137, stop_time='13:25:00') # Sidi Slim - 66
trip.AddStopTime(stop138, stop_time='13:26:00') # Palmasur - 37
trip.AddStopTime(stop139, stop_time='13:26:00') # Diva - 25
trip.AddStopTime(stop140, stop_time='13:26:00') # Palmariva - 29
trip.AddStopTime(stop133, stop_time='13:27:00') # Aguir - 44
trip.AddStopTime(stop134, stop_time='13:28:00') # Cap Jerba - 75
trip.AddStopTime(stop135, stop_time='13:29:00') # Elgassala - 55
trip.AddStopTime(stop58, stop_time='13:35:00') # Elmoustaoussef - 349
trip.AddStopTime(stop57, stop_time='13:37:00') # Elwachnia - 92
trip.AddStopTime(stop56, stop_time='13:38:00') # Arko - 73
trip.AddStopTime(stop55, stop_time='13:40:00') # Mosquet Arko - 120
trip.AddStopTime(stop54, stop_time='13:42:00') # Elazmouni - 110
trip.AddStopTime(stop53, stop_time='13:43:00') # Essaegh - 66
trip.AddStopTime(stop52, stop_time='13:44:00') # Mosquet Ben Ammar - 34
trip.AddStopTime(stop46, stop_time='13:46:00') # Midoun - 114
trip.AddStopTime(stop47, stop_time='13:48:00') # Hadher bach - 146
trip.AddStopTime(stop50, stop_time='13:50:00') # Boufaden - 116
trip.AddStopTime(stop51, stop_time='13:51:00') # Mahboubine - 53
trip.AddStopTime(stop82, stop_time='13:53:00') # Elweryemmi - 101
trip.AddStopTime(stop83, stop_time='13:54:00') # Ettouta - 47
trip.AddStopTime(stop84, stop_time='13:55:00') # elmehrab - 83
trip.AddStopTime(stop85, stop_time='13:56:00') # Elhajra elbidha - 42
trip.AddStopTime(stop86, stop_time='13:57:00') # Elhazem - 67
trip.AddStopTime(stop87, stop_time='13:58:00') # Ben Hamouda - 39
trip.AddStopTime(stop88, stop_time='13:59:00') # Hadj Dahmane - 41
trip.AddStopTime(stop89, stop_time='14:00:00') # ElKabou - 38
trip.AddStopTime(stop223, stop_time='14:02:00') # Le Collège - 92
trip.AddStopTime(stop90, stop_time='14:03:00') # Elmay - 58
trip.AddStopTime(stop175, stop_time='14:05:00') # Mosbah - 121
trip.AddStopTime(stop174, stop_time='14:05:00') # Ben Moussa - 26
trip.AddStopTime(stop161, stop_time='14:06:00') # Allamet - 72
trip.AddStopTime(stop160, stop_time='14:07:00') # Bir Ben Amor - 61
trip.AddStopTime(stop159, stop_time='14:09:00') # Omajen 3 - 92
trip.AddStopTime(stop147, stop_time='14:10:00') # Essouani - 83
trip.AddStopTime(stop222, stop_time='14:12:00') # Errahma - 118
trip.AddStopTime(stop221, stop_time='14:13:00') # Lycée Technique - 75
trip.AddStopTime(stop10, stop_time='14:16:00') # Houmet Souk - 159


trip = route.AddTrip(schedule, headsign="Houmet Souk vers Jerba La fidèle")
trip.AddStopTime(stop10, stop_time='12:15:00') # Houmet Souk - 0
trip.AddStopTime(stop221, stop_time='12:17:00') # Lycée Technique - 123
trip.AddStopTime(stop222, stop_time='12:18:00') # Errahma - 79
trip.AddStopTime(stop147, stop_time='12:20:00') # Essouani - 118
trip.AddStopTime(stop159, stop_time='12:21:00') # Omajen 3 - 83
trip.AddStopTime(stop160, stop_time='12:23:00') # Bir Ben Amor - 94
trip.AddStopTime(stop161, stop_time='12:24:00') # Allamet - 63
trip.AddStopTime(stop174, stop_time='12:25:00') # Ben Moussa - 72
trip.AddStopTime(stop175, stop_time='12:25:00') # Mosbah - 26
trip.AddStopTime(stop90, stop_time='12:27:00') # Elmay - 145
trip.AddStopTime(stop223, stop_time='12:28:00') # Le Collège - 61
trip.AddStopTime(stop89, stop_time='12:30:00') # ElKabou - 96
trip.AddStopTime(stop88, stop_time='12:31:00') # Hadj Dahmane - 38
trip.AddStopTime(stop87, stop_time='12:32:00') # Ben Hamouda - 39
trip.AddStopTime(stop86, stop_time='12:33:00') # Elhazem - 38
trip.AddStopTime(stop85, stop_time='12:34:00') # Elhajra elbidha - 77
trip.AddStopTime(stop84, stop_time='12:35:00') # elmehrab - 39
trip.AddStopTime(stop83, stop_time='12:36:00') # Ettouta - 83
trip.AddStopTime(stop82, stop_time='12:37:00') # Elweryemmi - 47
trip.AddStopTime(stop51, stop_time='12:39:00') # Mahboubine - 97
trip.AddStopTime(stop50, stop_time='12:40:00') # Boufaden - 53
trip.AddStopTime(stop47, stop_time='12:42:00') # Hadher bach - 115
trip.AddStopTime(stop46, stop_time='12:43:00') # Midoun - 85
trip.AddStopTime(stop52, stop_time='12:46:00') # Mosquet Ben Ammar - 180
trip.AddStopTime(stop53, stop_time='12:49:00') # Essaegh - 209
trip.AddStopTime(stop54, stop_time='12:51:00') # Elazmouni - 124
trip.AddStopTime(stop55, stop_time='12:52:00') # Mosquet Arko - 77
trip.AddStopTime(stop56, stop_time='12:54:00') # Arko - 126
trip.AddStopTime(stop57, stop_time='12:55:00') # Elwachnia - 73
trip.AddStopTime(stop58, stop_time='12:57:00') # Elmoustaoussef - 92
trip.AddStopTime(stop135, stop_time='13:03:00') # Elgassala - 369
trip.AddStopTime(stop134, stop_time='13:05:00') # Cap Jerba - 139
trip.AddStopTime(stop133, stop_time='13:07:00') # Aguir - 92
trip.AddStopTime(stop140, stop_time='13:08:00') # Palmariva - 44
trip.AddStopTime(stop139, stop_time='13:08:00') # Diva - 29
trip.AddStopTime(stop138, stop_time='13:08:00') # Palmasur - 25
trip.AddStopTime(stop137, stop_time='13:09:00') # Sidi Slim - 37
trip.AddStopTime(stop136, stop_time='13:10:00') # Hari Club - 39
trip.AddStopTime(stop59, stop_time='13:11:00') # Elmaamoura - 78
trip.AddStopTime(stop60, stop_time='13:12:00') # Carthago - 63
trip.AddStopTime(stop61, stop_time='13:13:00') # Calipso - 33
trip.AddStopTime(stop62, stop_time='13:15:00') # Jerba La douce - 112
trip.AddStopTime(stop63, stop_time='13:16:00') # Jerba Menzel - 32
trip.AddStopTime(stop64, stop_time='13:16:00') # Jerba La fidèle - 19

trip = route.AddTrip(schedule, headsign="Jerba La fidèle vers Houmet Souk")
trip.AddStopTime(stop64, stop_time='14:40:00') # Jerba La fidèle - 0
trip.AddStopTime(stop63, stop_time='14:40:00') # Jerba Menzel - 19
trip.AddStopTime(stop62, stop_time='14:41:00') # Jerba La douce - 33
trip.AddStopTime(stop61, stop_time='14:42:00') # Calipso - 44
trip.AddStopTime(stop60, stop_time='14:43:00') # Carthago - 89
trip.AddStopTime(stop59, stop_time='14:43:00') # Elmaamoura - 29
trip.AddStopTime(stop136, stop_time='14:44:00') # Hari Club - 74
trip.AddStopTime(stop137, stop_time='14:45:00') # Sidi Slim - 66
trip.AddStopTime(stop138, stop_time='14:46:00') # Palmasur - 37
trip.AddStopTime(stop139, stop_time='14:46:00') # Diva - 25
trip.AddStopTime(stop140, stop_time='14:46:00') # Palmariva - 29
trip.AddStopTime(stop133, stop_time='14:47:00') # Aguir - 44
trip.AddStopTime(stop134, stop_time='14:48:00') # Cap Jerba - 75
trip.AddStopTime(stop135, stop_time='14:49:00') # Elgassala - 55
trip.AddStopTime(stop58, stop_time='14:55:00') # Elmoustaoussef - 349
trip.AddStopTime(stop57, stop_time='14:57:00') # Elwachnia - 92
trip.AddStopTime(stop56, stop_time='14:58:00') # Arko - 73
trip.AddStopTime(stop55, stop_time='15:00:00') # Mosquet Arko - 120
trip.AddStopTime(stop54, stop_time='15:02:00') # Elazmouni - 110
trip.AddStopTime(stop53, stop_time='15:03:00') # Essaegh - 66
trip.AddStopTime(stop52, stop_time='15:04:00') # Mosquet Ben Ammar - 34
trip.AddStopTime(stop46, stop_time='15:06:00') # Midoun - 114
trip.AddStopTime(stop47, stop_time='15:08:00') # Hadher bach - 146
trip.AddStopTime(stop50, stop_time='15:10:00') # Boufaden - 116
trip.AddStopTime(stop51, stop_time='15:11:00') # Mahboubine - 53
trip.AddStopTime(stop82, stop_time='15:13:00') # Elweryemmi - 101
trip.AddStopTime(stop83, stop_time='15:14:00') # Ettouta - 47
trip.AddStopTime(stop84, stop_time='15:15:00') # elmehrab - 83
trip.AddStopTime(stop85, stop_time='15:16:00') # Elhajra elbidha - 42
trip.AddStopTime(stop86, stop_time='15:17:00') # Elhazem - 67
trip.AddStopTime(stop87, stop_time='15:18:00') # Ben Hamouda - 39
trip.AddStopTime(stop88, stop_time='15:19:00') # Hadj Dahmane - 41
trip.AddStopTime(stop89, stop_time='15:20:00') # ElKabou - 38
trip.AddStopTime(stop223, stop_time='15:22:00') # Le Collège - 92
trip.AddStopTime(stop90, stop_time='15:23:00') # Elmay - 58
trip.AddStopTime(stop175, stop_time='15:25:00') # Mosbah - 121
trip.AddStopTime(stop174, stop_time='15:25:00') # Ben Moussa - 26
trip.AddStopTime(stop161, stop_time='15:26:00') # Allamet - 72
trip.AddStopTime(stop160, stop_time='15:27:00') # Bir Ben Amor - 61
trip.AddStopTime(stop159, stop_time='15:29:00') # Omajen 3 - 92
trip.AddStopTime(stop147, stop_time='15:30:00') # Essouani - 83
trip.AddStopTime(stop222, stop_time='15:32:00') # Errahma - 118
trip.AddStopTime(stop221, stop_time='15:33:00') # Lycée Technique - 75
trip.AddStopTime(stop10, stop_time='15:36:00') # Houmet Souk - 159


trip = route.AddTrip(schedule, headsign="Houmet Souk vers Jerba La fidèle")
trip.AddStopTime(stop10, stop_time='13:45:00') # Houmet Souk - 0
trip.AddStopTime(stop221, stop_time='13:47:00') # Lycée Technique - 123
trip.AddStopTime(stop222, stop_time='13:48:00') # Errahma - 79
trip.AddStopTime(stop147, stop_time='13:50:00') # Essouani - 118
trip.AddStopTime(stop159, stop_time='13:51:00') # Omajen 3 - 83
trip.AddStopTime(stop160, stop_time='13:53:00') # Bir Ben Amor - 94
trip.AddStopTime(stop161, stop_time='13:54:00') # Allamet - 63
trip.AddStopTime(stop174, stop_time='13:55:00') # Ben Moussa - 72
trip.AddStopTime(stop175, stop_time='13:55:00') # Mosbah - 26
trip.AddStopTime(stop90, stop_time='13:57:00') # Elmay - 145
trip.AddStopTime(stop223, stop_time='13:58:00') # Le Collège - 61
trip.AddStopTime(stop89, stop_time='14:00:00') # ElKabou - 96
trip.AddStopTime(stop88, stop_time='14:01:00') # Hadj Dahmane - 38
trip.AddStopTime(stop87, stop_time='14:02:00') # Ben Hamouda - 39
trip.AddStopTime(stop86, stop_time='14:03:00') # Elhazem - 38
trip.AddStopTime(stop85, stop_time='14:04:00') # Elhajra elbidha - 77
trip.AddStopTime(stop84, stop_time='14:05:00') # elmehrab - 39
trip.AddStopTime(stop83, stop_time='14:06:00') # Ettouta - 83
trip.AddStopTime(stop82, stop_time='14:07:00') # Elweryemmi - 47
trip.AddStopTime(stop51, stop_time='14:09:00') # Mahboubine - 97
trip.AddStopTime(stop50, stop_time='14:10:00') # Boufaden - 53
trip.AddStopTime(stop47, stop_time='14:12:00') # Hadher bach - 115
trip.AddStopTime(stop46, stop_time='14:13:00') # Midoun - 85
trip.AddStopTime(stop52, stop_time='14:16:00') # Mosquet Ben Ammar - 180
trip.AddStopTime(stop53, stop_time='14:19:00') # Essaegh - 209
trip.AddStopTime(stop54, stop_time='14:21:00') # Elazmouni - 124
trip.AddStopTime(stop55, stop_time='14:22:00') # Mosquet Arko - 77
trip.AddStopTime(stop56, stop_time='14:24:00') # Arko - 126
trip.AddStopTime(stop57, stop_time='14:25:00') # Elwachnia - 73
trip.AddStopTime(stop58, stop_time='14:27:00') # Elmoustaoussef - 92
trip.AddStopTime(stop135, stop_time='14:33:00') # Elgassala - 369
trip.AddStopTime(stop134, stop_time='14:35:00') # Cap Jerba - 139
trip.AddStopTime(stop133, stop_time='14:37:00') # Aguir - 92
trip.AddStopTime(stop140, stop_time='14:38:00') # Palmariva - 44
trip.AddStopTime(stop139, stop_time='14:38:00') # Diva - 29
trip.AddStopTime(stop138, stop_time='14:38:00') # Palmasur - 25
trip.AddStopTime(stop137, stop_time='14:39:00') # Sidi Slim - 37
trip.AddStopTime(stop136, stop_time='14:40:00') # Hari Club - 39
trip.AddStopTime(stop59, stop_time='14:41:00') # Elmaamoura - 78
trip.AddStopTime(stop60, stop_time='14:42:00') # Carthago - 63
trip.AddStopTime(stop61, stop_time='14:43:00') # Calipso - 33
trip.AddStopTime(stop62, stop_time='14:45:00') # Jerba La douce - 112
trip.AddStopTime(stop63, stop_time='14:46:00') # Jerba Menzel - 32
trip.AddStopTime(stop64, stop_time='14:46:00') # Jerba La fidèle - 19

trip = route.AddTrip(schedule, headsign="Jerba La fidèle vers Houmet Souk")
trip.AddStopTime(stop64, stop_time='16:40:00') # Jerba La fidèle - 0
trip.AddStopTime(stop63, stop_time='16:40:00') # Jerba Menzel - 19
trip.AddStopTime(stop62, stop_time='16:41:00') # Jerba La douce - 33
trip.AddStopTime(stop61, stop_time='16:42:00') # Calipso - 44
trip.AddStopTime(stop60, stop_time='16:43:00') # Carthago - 89
trip.AddStopTime(stop59, stop_time='16:43:00') # Elmaamoura - 29
trip.AddStopTime(stop136, stop_time='16:44:00') # Hari Club - 74
trip.AddStopTime(stop137, stop_time='16:45:00') # Sidi Slim - 66
trip.AddStopTime(stop138, stop_time='16:46:00') # Palmasur - 37
trip.AddStopTime(stop139, stop_time='16:46:00') # Diva - 25
trip.AddStopTime(stop140, stop_time='16:46:00') # Palmariva - 29
trip.AddStopTime(stop133, stop_time='16:47:00') # Aguir - 44
trip.AddStopTime(stop134, stop_time='16:48:00') # Cap Jerba - 75
trip.AddStopTime(stop135, stop_time='16:49:00') # Elgassala - 55
trip.AddStopTime(stop58, stop_time='16:55:00') # Elmoustaoussef - 349
trip.AddStopTime(stop57, stop_time='16:57:00') # Elwachnia - 92
trip.AddStopTime(stop56, stop_time='16:58:00') # Arko - 73
trip.AddStopTime(stop55, stop_time='17:00:00') # Mosquet Arko - 120
trip.AddStopTime(stop54, stop_time='17:02:00') # Elazmouni - 110
trip.AddStopTime(stop53, stop_time='17:03:00') # Essaegh - 66
trip.AddStopTime(stop52, stop_time='17:04:00') # Mosquet Ben Ammar - 34
trip.AddStopTime(stop46, stop_time='17:06:00') # Midoun - 114
trip.AddStopTime(stop47, stop_time='17:08:00') # Hadher bach - 146
trip.AddStopTime(stop50, stop_time='17:10:00') # Boufaden - 116
trip.AddStopTime(stop51, stop_time='17:11:00') # Mahboubine - 53
trip.AddStopTime(stop82, stop_time='17:13:00') # Elweryemmi - 101
trip.AddStopTime(stop83, stop_time='17:14:00') # Ettouta - 47
trip.AddStopTime(stop84, stop_time='17:15:00') # elmehrab - 83
trip.AddStopTime(stop85, stop_time='17:16:00') # Elhajra elbidha - 42
trip.AddStopTime(stop86, stop_time='17:17:00') # Elhazem - 67
trip.AddStopTime(stop87, stop_time='17:18:00') # Ben Hamouda - 39
trip.AddStopTime(stop88, stop_time='17:19:00') # Hadj Dahmane - 41
trip.AddStopTime(stop89, stop_time='17:20:00') # ElKabou - 38
trip.AddStopTime(stop223, stop_time='17:22:00') # Le Collège - 92
trip.AddStopTime(stop90, stop_time='17:23:00') # Elmay - 58
trip.AddStopTime(stop175, stop_time='17:25:00') # Mosbah - 121
trip.AddStopTime(stop174, stop_time='17:25:00') # Ben Moussa - 26
trip.AddStopTime(stop161, stop_time='17:26:00') # Allamet - 72
trip.AddStopTime(stop160, stop_time='17:27:00') # Bir Ben Amor - 61
trip.AddStopTime(stop159, stop_time='17:29:00') # Omajen 3 - 92
trip.AddStopTime(stop147, stop_time='17:30:00') # Essouani - 83
trip.AddStopTime(stop222, stop_time='17:32:00') # Errahma - 118
trip.AddStopTime(stop221, stop_time='17:33:00') # Lycée Technique - 75
trip.AddStopTime(stop10, stop_time='17:36:00') # Houmet Souk - 159

trip = route.AddTrip(schedule, headsign="Houmet Souk vers Jerba La fidèle")
trip.AddStopTime(stop10, stop_time='14:30:00') # Houmet Souk - 0
trip.AddStopTime(stop221, stop_time='14:32:00') # Lycée Technique - 123
trip.AddStopTime(stop222, stop_time='14:33:00') # Errahma - 79
trip.AddStopTime(stop147, stop_time='14:35:00') # Essouani - 118
trip.AddStopTime(stop159, stop_time='14:36:00') # Omajen 3 - 83
trip.AddStopTime(stop160, stop_time='14:38:00') # Bir Ben Amor - 94
trip.AddStopTime(stop161, stop_time='14:39:00') # Allamet - 63
trip.AddStopTime(stop174, stop_time='14:40:00') # Ben Moussa - 72
trip.AddStopTime(stop175, stop_time='14:40:00') # Mosbah - 26
trip.AddStopTime(stop90, stop_time='14:42:00') # Elmay - 145
trip.AddStopTime(stop223, stop_time='14:43:00') # Le Collège - 61
trip.AddStopTime(stop89, stop_time='14:45:00') # ElKabou - 96
trip.AddStopTime(stop88, stop_time='14:46:00') # Hadj Dahmane - 38
trip.AddStopTime(stop87, stop_time='14:47:00') # Ben Hamouda - 39
trip.AddStopTime(stop86, stop_time='14:48:00') # Elhazem - 38
trip.AddStopTime(stop85, stop_time='14:49:00') # Elhajra elbidha - 77
trip.AddStopTime(stop84, stop_time='14:50:00') # elmehrab - 39
trip.AddStopTime(stop83, stop_time='14:51:00') # Ettouta - 83
trip.AddStopTime(stop82, stop_time='14:52:00') # Elweryemmi - 47
trip.AddStopTime(stop51, stop_time='14:54:00') # Mahboubine - 97
trip.AddStopTime(stop50, stop_time='14:55:00') # Boufaden - 53
trip.AddStopTime(stop47, stop_time='14:57:00') # Hadher bach - 115
trip.AddStopTime(stop46, stop_time='14:58:00') # Midoun - 85
trip.AddStopTime(stop52, stop_time='15:01:00') # Mosquet Ben Ammar - 180
trip.AddStopTime(stop53, stop_time='15:04:00') # Essaegh - 209
trip.AddStopTime(stop54, stop_time='15:06:00') # Elazmouni - 124
trip.AddStopTime(stop55, stop_time='15:07:00') # Mosquet Arko - 77
trip.AddStopTime(stop56, stop_time='15:09:00') # Arko - 126
trip.AddStopTime(stop57, stop_time='15:10:00') # Elwachnia - 73
trip.AddStopTime(stop58, stop_time='15:12:00') # Elmoustaoussef - 92
trip.AddStopTime(stop135, stop_time='15:18:00') # Elgassala - 369
trip.AddStopTime(stop134, stop_time='15:20:00') # Cap Jerba - 139
trip.AddStopTime(stop133, stop_time='15:22:00') # Aguir - 92
trip.AddStopTime(stop140, stop_time='15:23:00') # Palmariva - 44
trip.AddStopTime(stop139, stop_time='15:23:00') # Diva - 29
trip.AddStopTime(stop138, stop_time='15:23:00') # Palmasur - 25
trip.AddStopTime(stop137, stop_time='15:24:00') # Sidi Slim - 37
trip.AddStopTime(stop136, stop_time='15:25:00') # Hari Club - 39
trip.AddStopTime(stop59, stop_time='15:26:00') # Elmaamoura - 78
trip.AddStopTime(stop60, stop_time='15:27:00') # Carthago - 63
trip.AddStopTime(stop61, stop_time='15:28:00') # Calipso - 33
trip.AddStopTime(stop62, stop_time='15:30:00') # Jerba La douce - 112
trip.AddStopTime(stop63, stop_time='15:31:00') # Jerba Menzel - 32
trip.AddStopTime(stop64, stop_time='15:31:00') # Jerba La fidèle - 19

trip = route.AddTrip(schedule, headsign="Jerba La fidèle vers Houmet Souk")
trip.AddStopTime(stop64, stop_time='18:15:00') # Jerba La fidèle - 0
trip.AddStopTime(stop63, stop_time='18:15:00') # Jerba Menzel - 19
trip.AddStopTime(stop62, stop_time='18:16:00') # Jerba La douce - 33
trip.AddStopTime(stop61, stop_time='18:17:00') # Calipso - 44
trip.AddStopTime(stop60, stop_time='18:18:00') # Carthago - 89
trip.AddStopTime(stop59, stop_time='18:18:00') # Elmaamoura - 29
trip.AddStopTime(stop136, stop_time='18:19:00') # Hari Club - 74
trip.AddStopTime(stop137, stop_time='18:20:00') # Sidi Slim - 66
trip.AddStopTime(stop138, stop_time='18:21:00') # Palmasur - 37
trip.AddStopTime(stop139, stop_time='18:21:00') # Diva - 25
trip.AddStopTime(stop140, stop_time='18:21:00') # Palmariva - 29
trip.AddStopTime(stop133, stop_time='18:22:00') # Aguir - 44
trip.AddStopTime(stop134, stop_time='18:23:00') # Cap Jerba - 75
trip.AddStopTime(stop135, stop_time='18:24:00') # Elgassala - 55
trip.AddStopTime(stop58, stop_time='18:30:00') # Elmoustaoussef - 349
trip.AddStopTime(stop57, stop_time='18:32:00') # Elwachnia - 92
trip.AddStopTime(stop56, stop_time='18:33:00') # Arko - 73
trip.AddStopTime(stop55, stop_time='18:35:00') # Mosquet Arko - 120
trip.AddStopTime(stop54, stop_time='18:37:00') # Elazmouni - 110
trip.AddStopTime(stop53, stop_time='18:38:00') # Essaegh - 66
trip.AddStopTime(stop52, stop_time='18:39:00') # Mosquet Ben Ammar - 34
trip.AddStopTime(stop46, stop_time='18:41:00') # Midoun - 114
trip.AddStopTime(stop47, stop_time='18:43:00') # Hadher bach - 146
trip.AddStopTime(stop50, stop_time='18:45:00') # Boufaden - 116
trip.AddStopTime(stop51, stop_time='18:46:00') # Mahboubine - 53
trip.AddStopTime(stop82, stop_time='18:48:00') # Elweryemmi - 101
trip.AddStopTime(stop83, stop_time='18:49:00') # Ettouta - 47
trip.AddStopTime(stop84, stop_time='18:50:00') # elmehrab - 83
trip.AddStopTime(stop85, stop_time='18:51:00') # Elhajra elbidha - 42
trip.AddStopTime(stop86, stop_time='18:52:00') # Elhazem - 67
trip.AddStopTime(stop87, stop_time='18:53:00') # Ben Hamouda - 39
trip.AddStopTime(stop88, stop_time='18:54:00') # Hadj Dahmane - 41
trip.AddStopTime(stop89, stop_time='18:55:00') # ElKabou - 38
trip.AddStopTime(stop223, stop_time='18:57:00') # Le Collège - 92
trip.AddStopTime(stop90, stop_time='18:58:00') # Elmay - 58
trip.AddStopTime(stop175, stop_time='19:00:00') # Mosbah - 121
trip.AddStopTime(stop174, stop_time='19:00:00') # Ben Moussa - 26
trip.AddStopTime(stop161, stop_time='19:01:00') # Allamet - 72
trip.AddStopTime(stop160, stop_time='19:02:00') # Bir Ben Amor - 61
trip.AddStopTime(stop159, stop_time='19:04:00') # Omajen 3 - 92
trip.AddStopTime(stop147, stop_time='19:05:00') # Essouani - 83
trip.AddStopTime(stop222, stop_time='19:07:00') # Errahma - 118
trip.AddStopTime(stop221, stop_time='19:08:00') # Lycée Technique - 75
trip.AddStopTime(stop10, stop_time='19:11:00') # Houmet Souk - 159

trip = route.AddTrip(schedule, headsign="Houmet Souk vers Jerba La fidèle")
trip.AddStopTime(stop10, stop_time='15:30:00') # Houmet Souk - 0
trip.AddStopTime(stop221, stop_time='15:32:00') # Lycée Technique - 123
trip.AddStopTime(stop222, stop_time='15:33:00') # Errahma - 79
trip.AddStopTime(stop147, stop_time='15:35:00') # Essouani - 118
trip.AddStopTime(stop159, stop_time='15:36:00') # Omajen 3 - 83
trip.AddStopTime(stop160, stop_time='15:38:00') # Bir Ben Amor - 94
trip.AddStopTime(stop161, stop_time='15:39:00') # Allamet - 63
trip.AddStopTime(stop174, stop_time='15:40:00') # Ben Moussa - 72
trip.AddStopTime(stop175, stop_time='15:40:00') # Mosbah - 26
trip.AddStopTime(stop90, stop_time='15:42:00') # Elmay - 145
trip.AddStopTime(stop223, stop_time='15:43:00') # Le Collège - 61
trip.AddStopTime(stop89, stop_time='15:45:00') # ElKabou - 96
trip.AddStopTime(stop88, stop_time='15:46:00') # Hadj Dahmane - 38
trip.AddStopTime(stop87, stop_time='15:47:00') # Ben Hamouda - 39
trip.AddStopTime(stop86, stop_time='15:48:00') # Elhazem - 38
trip.AddStopTime(stop85, stop_time='15:49:00') # Elhajra elbidha - 77
trip.AddStopTime(stop84, stop_time='15:50:00') # elmehrab - 39
trip.AddStopTime(stop83, stop_time='15:51:00') # Ettouta - 83
trip.AddStopTime(stop82, stop_time='15:52:00') # Elweryemmi - 47
trip.AddStopTime(stop51, stop_time='15:54:00') # Mahboubine - 97
trip.AddStopTime(stop50, stop_time='15:55:00') # Boufaden - 53
trip.AddStopTime(stop47, stop_time='15:57:00') # Hadher bach - 115
trip.AddStopTime(stop46, stop_time='15:58:00') # Midoun - 85
trip.AddStopTime(stop52, stop_time='16:01:00') # Mosquet Ben Ammar - 180
trip.AddStopTime(stop53, stop_time='16:04:00') # Essaegh - 209
trip.AddStopTime(stop54, stop_time='16:06:00') # Elazmouni - 124
trip.AddStopTime(stop55, stop_time='16:07:00') # Mosquet Arko - 77
trip.AddStopTime(stop56, stop_time='16:09:00') # Arko - 126
trip.AddStopTime(stop57, stop_time='16:10:00') # Elwachnia - 73
trip.AddStopTime(stop58, stop_time='16:12:00') # Elmoustaoussef - 92
trip.AddStopTime(stop135, stop_time='16:18:00') # Elgassala - 369
trip.AddStopTime(stop134, stop_time='16:20:00') # Cap Jerba - 139
trip.AddStopTime(stop133, stop_time='16:22:00') # Aguir - 92
trip.AddStopTime(stop140, stop_time='16:23:00') # Palmariva - 44
trip.AddStopTime(stop139, stop_time='16:23:00') # Diva - 29
trip.AddStopTime(stop138, stop_time='16:23:00') # Palmasur - 25
trip.AddStopTime(stop137, stop_time='16:24:00') # Sidi Slim - 37
trip.AddStopTime(stop136, stop_time='16:25:00') # Hari Club - 39
trip.AddStopTime(stop59, stop_time='16:26:00') # Elmaamoura - 78
trip.AddStopTime(stop60, stop_time='16:27:00') # Carthago - 63
trip.AddStopTime(stop61, stop_time='16:28:00') # Calipso - 33
trip.AddStopTime(stop62, stop_time='16:30:00') # Jerba La douce - 112
trip.AddStopTime(stop63, stop_time='16:31:00') # Jerba Menzel - 32
trip.AddStopTime(stop64, stop_time='16:31:00') # Jerba La fidèle - 19

trip = route.AddTrip(schedule, headsign="Houmet Souk vers Jerba La fidèle")
trip.AddStopTime(stop10, stop_time='16:15:00') # Houmet Souk - 0
trip.AddStopTime(stop221, stop_time='16:17:00') # Lycée Technique - 123
trip.AddStopTime(stop222, stop_time='16:18:00') # Errahma - 79
trip.AddStopTime(stop147, stop_time='16:20:00') # Essouani - 118
trip.AddStopTime(stop159, stop_time='16:21:00') # Omajen 3 - 83
trip.AddStopTime(stop160, stop_time='16:23:00') # Bir Ben Amor - 94
trip.AddStopTime(stop161, stop_time='16:24:00') # Allamet - 63
trip.AddStopTime(stop174, stop_time='16:25:00') # Ben Moussa - 72
trip.AddStopTime(stop175, stop_time='16:25:00') # Mosbah - 26
trip.AddStopTime(stop90, stop_time='16:27:00') # Elmay - 145
trip.AddStopTime(stop223, stop_time='16:28:00') # Le Collège - 61
trip.AddStopTime(stop89, stop_time='16:30:00') # ElKabou - 96
trip.AddStopTime(stop88, stop_time='16:31:00') # Hadj Dahmane - 38
trip.AddStopTime(stop87, stop_time='16:32:00') # Ben Hamouda - 39
trip.AddStopTime(stop86, stop_time='16:33:00') # Elhazem - 38
trip.AddStopTime(stop85, stop_time='16:34:00') # Elhajra elbidha - 77
trip.AddStopTime(stop84, stop_time='16:35:00') # elmehrab - 39
trip.AddStopTime(stop83, stop_time='16:36:00') # Ettouta - 83
trip.AddStopTime(stop82, stop_time='16:37:00') # Elweryemmi - 47
trip.AddStopTime(stop51, stop_time='16:39:00') # Mahboubine - 97
trip.AddStopTime(stop50, stop_time='16:40:00') # Boufaden - 53
trip.AddStopTime(stop47, stop_time='16:42:00') # Hadher bach - 115
trip.AddStopTime(stop46, stop_time='16:43:00') # Midoun - 85
trip.AddStopTime(stop52, stop_time='16:46:00') # Mosquet Ben Ammar - 180
trip.AddStopTime(stop53, stop_time='16:49:00') # Essaegh - 209
trip.AddStopTime(stop54, stop_time='16:51:00') # Elazmouni - 124
trip.AddStopTime(stop55, stop_time='16:52:00') # Mosquet Arko - 77
trip.AddStopTime(stop56, stop_time='16:54:00') # Arko - 126
trip.AddStopTime(stop57, stop_time='16:55:00') # Elwachnia - 73
trip.AddStopTime(stop58, stop_time='16:57:00') # Elmoustaoussef - 92
trip.AddStopTime(stop135, stop_time='17:03:00') # Elgassala - 369
trip.AddStopTime(stop134, stop_time='17:05:00') # Cap Jerba - 139
trip.AddStopTime(stop133, stop_time='17:07:00') # Aguir - 92
trip.AddStopTime(stop140, stop_time='17:08:00') # Palmariva - 44
trip.AddStopTime(stop139, stop_time='17:08:00') # Diva - 29
trip.AddStopTime(stop138, stop_time='17:08:00') # Palmasur - 25
trip.AddStopTime(stop137, stop_time='17:09:00') # Sidi Slim - 37
trip.AddStopTime(stop136, stop_time='17:10:00') # Hari Club - 39
trip.AddStopTime(stop59, stop_time='17:11:00') # Elmaamoura - 78
trip.AddStopTime(stop60, stop_time='17:12:00') # Carthago - 63
trip.AddStopTime(stop61, stop_time='17:13:00') # Calipso - 33
trip.AddStopTime(stop62, stop_time='17:15:00') # Jerba La douce - 112
trip.AddStopTime(stop63, stop_time='17:16:00') # Jerba Menzel - 32
trip.AddStopTime(stop64, stop_time='17:16:00') # Jerba La fidèle - 19

trip = route.AddTrip(schedule, headsign="Houmet Souk vers Jerba La fidèle")
trip.AddStopTime(stop10, stop_time='17:15:00') # Houmet Souk - 0
trip.AddStopTime(stop221, stop_time='17:17:00') # Lycée Technique - 123
trip.AddStopTime(stop222, stop_time='17:18:00') # Errahma - 79
trip.AddStopTime(stop147, stop_time='17:20:00') # Essouani - 118
trip.AddStopTime(stop159, stop_time='17:21:00') # Omajen 3 - 83
trip.AddStopTime(stop160, stop_time='17:23:00') # Bir Ben Amor - 94
trip.AddStopTime(stop161, stop_time='17:24:00') # Allamet - 63
trip.AddStopTime(stop174, stop_time='17:25:00') # Ben Moussa - 72
trip.AddStopTime(stop175, stop_time='17:25:00') # Mosbah - 26
trip.AddStopTime(stop90, stop_time='17:27:00') # Elmay - 145
trip.AddStopTime(stop223, stop_time='17:28:00') # Le Collège - 61
trip.AddStopTime(stop89, stop_time='17:30:00') # ElKabou - 96
trip.AddStopTime(stop88, stop_time='17:31:00') # Hadj Dahmane - 38
trip.AddStopTime(stop87, stop_time='17:32:00') # Ben Hamouda - 39
trip.AddStopTime(stop86, stop_time='17:33:00') # Elhazem - 38
trip.AddStopTime(stop85, stop_time='17:34:00') # Elhajra elbidha - 77
trip.AddStopTime(stop84, stop_time='17:35:00') # elmehrab - 39
trip.AddStopTime(stop83, stop_time='17:36:00') # Ettouta - 83
trip.AddStopTime(stop82, stop_time='17:37:00') # Elweryemmi - 47
trip.AddStopTime(stop51, stop_time='17:39:00') # Mahboubine - 97
trip.AddStopTime(stop50, stop_time='17:40:00') # Boufaden - 53
trip.AddStopTime(stop47, stop_time='17:42:00') # Hadher bach - 115
trip.AddStopTime(stop46, stop_time='17:43:00') # Midoun - 85
trip.AddStopTime(stop52, stop_time='17:46:00') # Mosquet Ben Ammar - 180
trip.AddStopTime(stop53, stop_time='17:49:00') # Essaegh - 209
trip.AddStopTime(stop54, stop_time='17:51:00') # Elazmouni - 124
trip.AddStopTime(stop55, stop_time='17:52:00') # Mosquet Arko - 77
trip.AddStopTime(stop56, stop_time='17:54:00') # Arko - 126
trip.AddStopTime(stop57, stop_time='17:55:00') # Elwachnia - 73
trip.AddStopTime(stop58, stop_time='17:57:00') # Elmoustaoussef - 92
trip.AddStopTime(stop135, stop_time='18:03:00') # Elgassala - 369
trip.AddStopTime(stop134, stop_time='18:05:00') # Cap Jerba - 139
trip.AddStopTime(stop133, stop_time='18:07:00') # Aguir - 92
trip.AddStopTime(stop140, stop_time='18:08:00') # Palmariva - 44
trip.AddStopTime(stop139, stop_time='18:08:00') # Diva - 29
trip.AddStopTime(stop138, stop_time='18:08:00') # Palmasur - 25
trip.AddStopTime(stop137, stop_time='18:09:00') # Sidi Slim - 37
trip.AddStopTime(stop136, stop_time='18:10:00') # Hari Club - 39
trip.AddStopTime(stop59, stop_time='18:11:00') # Elmaamoura - 78
trip.AddStopTime(stop60, stop_time='18:12:00') # Carthago - 63
trip.AddStopTime(stop61, stop_time='18:13:00') # Calipso - 33
trip.AddStopTime(stop62, stop_time='18:15:00') # Jerba La douce - 112
trip.AddStopTime(stop63, stop_time='18:16:00') # Jerba Menzel - 32
trip.AddStopTime(stop64, stop_time='18:16:00') # Jerba La fidèle - 19


trip = route.AddTrip(schedule, headsign="Houmet Souk vers Jerba La fidèle")
trip.AddStopTime(stop10, stop_time='18:15:00') # Houmet Souk - 0
trip.AddStopTime(stop221, stop_time='18:17:00') # Lycée Technique - 123
trip.AddStopTime(stop222, stop_time='18:18:00') # Errahma - 79
trip.AddStopTime(stop147, stop_time='18:20:00') # Essouani - 118
trip.AddStopTime(stop159, stop_time='18:21:00') # Omajen 3 - 83
trip.AddStopTime(stop160, stop_time='18:23:00') # Bir Ben Amor - 94
trip.AddStopTime(stop161, stop_time='18:24:00') # Allamet - 63
trip.AddStopTime(stop174, stop_time='18:25:00') # Ben Moussa - 72
trip.AddStopTime(stop175, stop_time='18:25:00') # Mosbah - 26
trip.AddStopTime(stop90, stop_time='18:27:00') # Elmay - 145
trip.AddStopTime(stop223, stop_time='18:28:00') # Le Collège - 61
trip.AddStopTime(stop89, stop_time='18:30:00') # ElKabou - 96
trip.AddStopTime(stop88, stop_time='18:31:00') # Hadj Dahmane - 38
trip.AddStopTime(stop87, stop_time='18:32:00') # Ben Hamouda - 39
trip.AddStopTime(stop86, stop_time='18:33:00') # Elhazem - 38
trip.AddStopTime(stop85, stop_time='18:34:00') # Elhajra elbidha - 77
trip.AddStopTime(stop84, stop_time='18:35:00') # elmehrab - 39
trip.AddStopTime(stop83, stop_time='18:36:00') # Ettouta - 83
trip.AddStopTime(stop82, stop_time='18:37:00') # Elweryemmi - 47
trip.AddStopTime(stop51, stop_time='18:39:00') # Mahboubine - 97
trip.AddStopTime(stop50, stop_time='18:40:00') # Boufaden - 53
trip.AddStopTime(stop47, stop_time='18:42:00') # Hadher bach - 115
trip.AddStopTime(stop46, stop_time='18:43:00') # Midoun - 85
trip.AddStopTime(stop52, stop_time='18:46:00') # Mosquet Ben Ammar - 180
trip.AddStopTime(stop53, stop_time='18:49:00') # Essaegh - 209
trip.AddStopTime(stop54, stop_time='18:51:00') # Elazmouni - 124
trip.AddStopTime(stop55, stop_time='18:52:00') # Mosquet Arko - 77
trip.AddStopTime(stop56, stop_time='18:54:00') # Arko - 126
trip.AddStopTime(stop57, stop_time='18:55:00') # Elwachnia - 73
trip.AddStopTime(stop58, stop_time='18:57:00') # Elmoustaoussef - 92
trip.AddStopTime(stop135, stop_time='19:03:00') # Elgassala - 369
trip.AddStopTime(stop134, stop_time='19:05:00') # Cap Jerba - 139
trip.AddStopTime(stop133, stop_time='19:07:00') # Aguir - 92
trip.AddStopTime(stop140, stop_time='19:08:00') # Palmariva - 44
trip.AddStopTime(stop139, stop_time='19:08:00') # Diva - 29
trip.AddStopTime(stop138, stop_time='19:08:00') # Palmasur - 25
trip.AddStopTime(stop137, stop_time='19:09:00') # Sidi Slim - 37
trip.AddStopTime(stop136, stop_time='19:10:00') # Hari Club - 39
trip.AddStopTime(stop59, stop_time='19:11:00') # Elmaamoura - 78
trip.AddStopTime(stop60, stop_time='19:12:00') # Carthago - 63
trip.AddStopTime(stop61, stop_time='19:13:00') # Calipso - 33
trip.AddStopTime(stop62, stop_time='19:15:00') # Jerba La douce - 112
trip.AddStopTime(stop63, stop_time='19:16:00') # Jerba Menzel - 32
trip.AddStopTime(stop64, stop_time='19:16:00') # Jerba La fidèle - 19


route = schedule.AddRoute(short_name="SU411", long_name="Houmet Souk, Tanit",
                          route_type="Bus")

trip = route.AddTrip(schedule, headsign="Houmet Souk vers Tanit")
trip.AddStopTime(stop10, stop_time='06:00:00') # Houmet Souk - 0
trip.AddStopTime(stop14, stop_time='06:06:00') # Elwilayia - 349
trip.AddStopTime(stop15, stop_time='06:08:00') # Sidi Zayed - 102
trip.AddStopTime(stop16, stop_time='06:09:00') # Lobirette - 84
trip.AddStopTime(stop17, stop_time='06:10:00') # Fatou2 - 49
trip.AddStopTime(stop18, stop_time='06:13:00') # Sidi Ismail - 209
trip.AddStopTime(stop19, stop_time='06:16:00') # Arouay - 202
trip.AddStopTime(stop20, stop_time='06:18:00') # Croisement Guisen - 91
trip.AddStopTime(stop21, stop_time='06:20:00') # Elmagtaa - 108
trip.AddStopTime(stop22, stop_time='06:23:00') # Ras ettabia - 155
trip.AddStopTime(stop23, stop_time='06:26:00') # Athene - 156
trip.AddStopTime(stop24, stop_time='06:29:00') # Ulysse - 178
trip.AddStopTime(stop25, stop_time='06:31:00') # Eljazira - 139
trip.AddStopTime(stop26, stop_time='06:33:00') # Dalli - 121
trip.AddStopTime(stop27, stop_time='06:34:00') # Holiday - 79
trip.AddStopTime(stop28, stop_time='06:37:00') # Elmadina - 166
trip.AddStopTime(stop29, stop_time='06:39:00') # Abou Nawess - 140
trip.AddStopTime(stop30, stop_time='06:40:00') # Palm Beach - 53
trip.AddStopTime(stop31, stop_time='06:43:00') # Toumana - 151
trip.AddStopTime(stop32, stop_time='06:44:00') # Yasmina - 39
trip.AddStopTime(stop33, stop_time='06:47:00') # Dar Midoun - 163
trip.AddStopTime(stop34, stop_time='06:48:00') # R.D.V - 63
trip.AddStopTime(stop35, stop_time='06:50:00') # Hasdrubal - 134
trip.AddStopTime(stop36, stop_time='06:51:00') # Minenx - 81
trip.AddStopTime(stop37, stop_time='06:52:00') # Elhana - 87
trip.AddStopTime(stop38, stop_time='06:54:00') # Plazza - 109
trip.AddStopTime(stop39, stop_time='06:57:00') # Golf - 166
trip.AddStopTime(stop40, stop_time='06:58:00') # Yadis - 53
trip.AddStopTime(stop41, stop_time='06:59:00') # Elmahari - 68
trip.AddStopTime(stop42, stop_time='07:02:00') # Elmanara - 157
trip.AddStopTime(stop43, stop_time='07:03:00') # Abou Nawess Golf - 87
trip.AddStopTime(stop44, stop_time='07:05:00') # Dar Jeba - 149
trip.AddStopTime(stop45, stop_time='07:07:00') # Phare Ennadhour - 149
trip.AddStopTime(stop74, stop_time='07:13:00') # Tanit - 364

trip = route.AddTrip(schedule, headsign="Tanit vers Houmet Souk")
trip.AddStopTime(stop74, stop_time='07:15:00') # Tanit - 0
trip.AddStopTime(stop45, stop_time='07:20:00') # Phare Ennadhour - 298
trip.AddStopTime(stop44, stop_time='07:21:00') # Dar Jeba - 78
trip.AddStopTime(stop43, stop_time='07:21:00') # Abou Nawess Golf - 26
trip.AddStopTime(stop42, stop_time='07:21:00') # Elmanara - 26
trip.AddStopTime(stop41, stop_time='07:21:00') # Elmahari - 20
trip.AddStopTime(stop40, stop_time='07:22:00') # Yadis - 44
trip.AddStopTime(stop39, stop_time='07:24:00') # Golf - 112
trip.AddStopTime(stop38, stop_time='07:24:00') # Plazza - 22
trip.AddStopTime(stop37, stop_time='07:25:00') # Elhana - 32
trip.AddStopTime(stop36, stop_time='07:26:00') # Minenx - 47
trip.AddStopTime(stop35, stop_time='07:27:00') # Hasdrubal - 36
trip.AddStopTime(stop34, stop_time='07:29:00') # R.D.V - 106
trip.AddStopTime(stop33, stop_time='07:30:00') # Dar Midoun - 88
trip.AddStopTime(stop32, stop_time='07:33:00') # Yasmina - 158
trip.AddStopTime(stop31, stop_time='07:35:00') # Toumana - 107
trip.AddStopTime(stop30, stop_time='07:37:00') # Palm Beach - 121
trip.AddStopTime(stop29, stop_time='07:38:00') # Abou Nawess - 53
trip.AddStopTime(stop28, stop_time='07:40:00') # Elmadina - 149
trip.AddStopTime(stop27, stop_time='07:42:00') # Holiday - 134
trip.AddStopTime(stop26, stop_time='07:43:00') # Dalli - 83
trip.AddStopTime(stop25, stop_time='07:46:00') # Eljazira - 199
trip.AddStopTime(stop24, stop_time='07:48:00') # Ulysse - 147
trip.AddStopTime(stop23, stop_time='07:49:00') # Athene - 72
trip.AddStopTime(stop22, stop_time='07:52:00') # Ras ettabia - 197
trip.AddStopTime(stop21, stop_time='07:53:00') # Elmagtaa - 58
trip.AddStopTime(stop20, stop_time='07:55:00') # Croisement Guisen - 101
trip.AddStopTime(stop19, stop_time='07:59:00') # Arouay - 245
trip.AddStopTime(stop18, stop_time='08:02:00') # Sidi Ismail - 162
trip.AddStopTime(stop17, stop_time='08:04:00') # Fatou2 - 125
trip.AddStopTime(stop16, stop_time='08:09:00') # Lobirette - 309
trip.AddStopTime(stop15, stop_time='08:12:00') # Sidi Zayed - 203
trip.AddStopTime(stop14, stop_time='08:14:00') # Elwilayia - 90
trip.AddStopTime(stop10, stop_time='08:20:00') # Houmet Souk - 384


trip = route.AddTrip(schedule, headsign="Houmet Souk vers Tanit")
trip.AddStopTime(stop10, stop_time='07:15:00') # Houmet Souk - 0
trip.AddStopTime(stop14, stop_time='07:21:00') # Elwilayia - 349
trip.AddStopTime(stop15, stop_time='07:23:00') # Sidi Zayed - 102
trip.AddStopTime(stop16, stop_time='07:24:00') # Lobirette - 84
trip.AddStopTime(stop17, stop_time='07:25:00') # Fatou2 - 49
trip.AddStopTime(stop18, stop_time='07:28:00') # Sidi Ismail - 209
trip.AddStopTime(stop19, stop_time='07:31:00') # Arouay - 202
trip.AddStopTime(stop20, stop_time='07:33:00') # Croisement Guisen - 91
trip.AddStopTime(stop21, stop_time='07:35:00') # Elmagtaa - 108
trip.AddStopTime(stop22, stop_time='07:38:00') # Ras ettabia - 155
trip.AddStopTime(stop23, stop_time='07:41:00') # Athene - 156
trip.AddStopTime(stop24, stop_time='07:44:00') # Ulysse - 178
trip.AddStopTime(stop25, stop_time='07:46:00') # Eljazira - 139
trip.AddStopTime(stop26, stop_time='07:48:00') # Dalli - 121
trip.AddStopTime(stop27, stop_time='07:49:00') # Holiday - 79
trip.AddStopTime(stop28, stop_time='07:52:00') # Elmadina - 166
trip.AddStopTime(stop29, stop_time='07:54:00') # Abou Nawess - 140
trip.AddStopTime(stop30, stop_time='07:55:00') # Palm Beach - 53
trip.AddStopTime(stop31, stop_time='07:58:00') # Toumana - 151
trip.AddStopTime(stop32, stop_time='07:59:00') # Yasmina - 39
trip.AddStopTime(stop33, stop_time='08:02:00') # Dar Midoun - 163
trip.AddStopTime(stop34, stop_time='08:03:00') # R.D.V - 63
trip.AddStopTime(stop35, stop_time='08:05:00') # Hasdrubal - 134
trip.AddStopTime(stop36, stop_time='08:06:00') # Minenx - 81
trip.AddStopTime(stop37, stop_time='08:07:00') # Elhana - 87
trip.AddStopTime(stop38, stop_time='08:09:00') # Plazza - 109
trip.AddStopTime(stop39, stop_time='08:12:00') # Golf - 166
trip.AddStopTime(stop40, stop_time='08:13:00') # Yadis - 53
trip.AddStopTime(stop41, stop_time='08:14:00') # Elmahari - 68
trip.AddStopTime(stop42, stop_time='08:17:00') # Elmanara - 157
trip.AddStopTime(stop43, stop_time='08:18:00') # Abou Nawess Golf - 87
trip.AddStopTime(stop44, stop_time='08:20:00') # Dar Jeba - 149
trip.AddStopTime(stop45, stop_time='08:22:00') # Phare Ennadhour - 149
trip.AddStopTime(stop74, stop_time='08:28:00') # Tanit - 364

trip = route.AddTrip(schedule, headsign="Tanit vers Houmet Souk")
trip.AddStopTime(stop74, stop_time='08:15:00') # Tanit - 0
trip.AddStopTime(stop45, stop_time='08:20:00') # Phare Ennadhour - 298
trip.AddStopTime(stop44, stop_time='08:21:00') # Dar Jeba - 78
trip.AddStopTime(stop43, stop_time='08:21:00') # Abou Nawess Golf - 26
trip.AddStopTime(stop42, stop_time='08:21:00') # Elmanara - 26
trip.AddStopTime(stop41, stop_time='08:21:00') # Elmahari - 20
trip.AddStopTime(stop40, stop_time='08:22:00') # Yadis - 44
trip.AddStopTime(stop39, stop_time='08:24:00') # Golf - 112
trip.AddStopTime(stop38, stop_time='08:24:00') # Plazza - 22
trip.AddStopTime(stop37, stop_time='08:25:00') # Elhana - 32
trip.AddStopTime(stop36, stop_time='08:26:00') # Minenx - 47
trip.AddStopTime(stop35, stop_time='08:27:00') # Hasdrubal - 36
trip.AddStopTime(stop34, stop_time='08:29:00') # R.D.V - 106
trip.AddStopTime(stop33, stop_time='08:30:00') # Dar Midoun - 88
trip.AddStopTime(stop32, stop_time='08:33:00') # Yasmina - 158
trip.AddStopTime(stop31, stop_time='08:35:00') # Toumana - 107
trip.AddStopTime(stop30, stop_time='08:37:00') # Palm Beach - 121
trip.AddStopTime(stop29, stop_time='08:38:00') # Abou Nawess - 53
trip.AddStopTime(stop28, stop_time='08:40:00') # Elmadina - 149
trip.AddStopTime(stop27, stop_time='08:42:00') # Holiday - 134
trip.AddStopTime(stop26, stop_time='08:43:00') # Dalli - 83
trip.AddStopTime(stop25, stop_time='08:46:00') # Eljazira - 199
trip.AddStopTime(stop24, stop_time='08:48:00') # Ulysse - 147
trip.AddStopTime(stop23, stop_time='08:49:00') # Athene - 72
trip.AddStopTime(stop22, stop_time='08:52:00') # Ras ettabia - 197
trip.AddStopTime(stop21, stop_time='08:53:00') # Elmagtaa - 58
trip.AddStopTime(stop20, stop_time='08:55:00') # Croisement Guisen - 101
trip.AddStopTime(stop19, stop_time='08:59:00') # Arouay - 245
trip.AddStopTime(stop18, stop_time='09:02:00') # Sidi Ismail - 162
trip.AddStopTime(stop17, stop_time='09:04:00') # Fatou2 - 125
trip.AddStopTime(stop16, stop_time='09:09:00') # Lobirette - 309
trip.AddStopTime(stop15, stop_time='09:12:00') # Sidi Zayed - 203
trip.AddStopTime(stop14, stop_time='09:14:00') # Elwilayia - 90
trip.AddStopTime(stop10, stop_time='09:20:00') # Houmet Souk - 384


trip = route.AddTrip(schedule, headsign="Houmet Souk vers Tanit")
trip.AddStopTime(stop10, stop_time='08:00:00') # Houmet Souk - 0
trip.AddStopTime(stop14, stop_time='08:06:00') # Elwilayia - 349
trip.AddStopTime(stop15, stop_time='08:08:00') # Sidi Zayed - 102
trip.AddStopTime(stop16, stop_time='08:09:00') # Lobirette - 84
trip.AddStopTime(stop17, stop_time='08:10:00') # Fatou2 - 49
trip.AddStopTime(stop18, stop_time='08:13:00') # Sidi Ismail - 209
trip.AddStopTime(stop19, stop_time='08:16:00') # Arouay - 202
trip.AddStopTime(stop20, stop_time='08:18:00') # Croisement Guisen - 91
trip.AddStopTime(stop21, stop_time='08:20:00') # Elmagtaa - 108
trip.AddStopTime(stop22, stop_time='08:23:00') # Ras ettabia - 155
trip.AddStopTime(stop23, stop_time='08:26:00') # Athene - 156
trip.AddStopTime(stop24, stop_time='08:29:00') # Ulysse - 178
trip.AddStopTime(stop25, stop_time='08:31:00') # Eljazira - 139
trip.AddStopTime(stop26, stop_time='08:33:00') # Dalli - 121
trip.AddStopTime(stop27, stop_time='08:34:00') # Holiday - 79
trip.AddStopTime(stop28, stop_time='08:37:00') # Elmadina - 166
trip.AddStopTime(stop29, stop_time='08:39:00') # Abou Nawess - 140
trip.AddStopTime(stop30, stop_time='08:40:00') # Palm Beach - 53
trip.AddStopTime(stop31, stop_time='08:43:00') # Toumana - 151
trip.AddStopTime(stop32, stop_time='08:44:00') # Yasmina - 39
trip.AddStopTime(stop33, stop_time='08:47:00') # Dar Midoun - 163
trip.AddStopTime(stop34, stop_time='08:48:00') # R.D.V - 63
trip.AddStopTime(stop35, stop_time='08:50:00') # Hasdrubal - 134
trip.AddStopTime(stop36, stop_time='08:51:00') # Minenx - 81
trip.AddStopTime(stop37, stop_time='08:52:00') # Elhana - 87
trip.AddStopTime(stop38, stop_time='08:54:00') # Plazza - 109
trip.AddStopTime(stop39, stop_time='08:57:00') # Golf - 166
trip.AddStopTime(stop40, stop_time='08:58:00') # Yadis - 53
trip.AddStopTime(stop41, stop_time='08:59:00') # Elmahari - 68
trip.AddStopTime(stop42, stop_time='09:02:00') # Elmanara - 157
trip.AddStopTime(stop43, stop_time='09:03:00') # Abou Nawess Golf - 87
trip.AddStopTime(stop44, stop_time='09:05:00') # Dar Jeba - 149
trip.AddStopTime(stop45, stop_time='09:07:00') # Phare Ennadhour - 149
trip.AddStopTime(stop74, stop_time='09:13:00') # Tanit - 364

trip = route.AddTrip(schedule, headsign="Tanit vers Houmet Souk")
trip.AddStopTime(stop74, stop_time='08:45:00') # Tanit - 0
trip.AddStopTime(stop45, stop_time='08:50:00') # Phare Ennadhour - 298
trip.AddStopTime(stop44, stop_time='08:51:00') # Dar Jeba - 78
trip.AddStopTime(stop43, stop_time='08:51:00') # Abou Nawess Golf - 26
trip.AddStopTime(stop42, stop_time='08:51:00') # Elmanara - 26
trip.AddStopTime(stop41, stop_time='08:51:00') # Elmahari - 20
trip.AddStopTime(stop40, stop_time='08:52:00') # Yadis - 44
trip.AddStopTime(stop39, stop_time='08:54:00') # Golf - 112
trip.AddStopTime(stop38, stop_time='08:54:00') # Plazza - 22
trip.AddStopTime(stop37, stop_time='08:55:00') # Elhana - 32
trip.AddStopTime(stop36, stop_time='08:56:00') # Minenx - 47
trip.AddStopTime(stop35, stop_time='08:57:00') # Hasdrubal - 36
trip.AddStopTime(stop34, stop_time='08:59:00') # R.D.V - 106
trip.AddStopTime(stop33, stop_time='09:00:00') # Dar Midoun - 88
trip.AddStopTime(stop32, stop_time='09:03:00') # Yasmina - 158
trip.AddStopTime(stop31, stop_time='09:05:00') # Toumana - 107
trip.AddStopTime(stop30, stop_time='09:07:00') # Palm Beach - 121
trip.AddStopTime(stop29, stop_time='09:08:00') # Abou Nawess - 53
trip.AddStopTime(stop28, stop_time='09:10:00') # Elmadina - 149
trip.AddStopTime(stop27, stop_time='09:12:00') # Holiday - 134
trip.AddStopTime(stop26, stop_time='09:13:00') # Dalli - 83
trip.AddStopTime(stop25, stop_time='09:16:00') # Eljazira - 199
trip.AddStopTime(stop24, stop_time='09:18:00') # Ulysse - 147
trip.AddStopTime(stop23, stop_time='09:19:00') # Athene - 72
trip.AddStopTime(stop22, stop_time='09:22:00') # Ras ettabia - 197
trip.AddStopTime(stop21, stop_time='09:23:00') # Elmagtaa - 58
trip.AddStopTime(stop20, stop_time='09:25:00') # Croisement Guisen - 101
trip.AddStopTime(stop19, stop_time='09:29:00') # Arouay - 245
trip.AddStopTime(stop18, stop_time='09:32:00') # Sidi Ismail - 162
trip.AddStopTime(stop17, stop_time='09:34:00') # Fatou2 - 125
trip.AddStopTime(stop16, stop_time='09:39:00') # Lobirette - 309
trip.AddStopTime(stop15, stop_time='09:42:00') # Sidi Zayed - 203
trip.AddStopTime(stop14, stop_time='09:44:00') # Elwilayia - 90
trip.AddStopTime(stop10, stop_time='09:50:00') # Houmet Souk - 384

trip = route.AddTrip(schedule, headsign="Houmet Souk vers Tanit")
trip.AddStopTime(stop10, stop_time='09:15:00') # Houmet Souk - 0
trip.AddStopTime(stop14, stop_time='09:21:00') # Elwilayia - 349
trip.AddStopTime(stop15, stop_time='09:23:00') # Sidi Zayed - 102
trip.AddStopTime(stop16, stop_time='09:24:00') # Lobirette - 84
trip.AddStopTime(stop17, stop_time='09:25:00') # Fatou2 - 49
trip.AddStopTime(stop18, stop_time='09:28:00') # Sidi Ismail - 209
trip.AddStopTime(stop19, stop_time='09:31:00') # Arouay - 202
trip.AddStopTime(stop20, stop_time='09:33:00') # Croisement Guisen - 91
trip.AddStopTime(stop21, stop_time='09:35:00') # Elmagtaa - 108
trip.AddStopTime(stop22, stop_time='09:38:00') # Ras ettabia - 155
trip.AddStopTime(stop23, stop_time='09:41:00') # Athene - 156
trip.AddStopTime(stop24, stop_time='09:44:00') # Ulysse - 178
trip.AddStopTime(stop25, stop_time='09:46:00') # Eljazira - 139
trip.AddStopTime(stop26, stop_time='09:48:00') # Dalli - 121
trip.AddStopTime(stop27, stop_time='09:49:00') # Holiday - 79
trip.AddStopTime(stop28, stop_time='09:52:00') # Elmadina - 166
trip.AddStopTime(stop29, stop_time='09:54:00') # Abou Nawess - 140
trip.AddStopTime(stop30, stop_time='09:55:00') # Palm Beach - 53
trip.AddStopTime(stop31, stop_time='09:58:00') # Toumana - 151
trip.AddStopTime(stop32, stop_time='09:59:00') # Yasmina - 39
trip.AddStopTime(stop33, stop_time='10:02:00') # Dar Midoun - 163
trip.AddStopTime(stop34, stop_time='10:03:00') # R.D.V - 63
trip.AddStopTime(stop35, stop_time='10:05:00') # Hasdrubal - 134
trip.AddStopTime(stop36, stop_time='10:06:00') # Minenx - 81
trip.AddStopTime(stop37, stop_time='10:07:00') # Elhana - 87
trip.AddStopTime(stop38, stop_time='10:09:00') # Plazza - 109
trip.AddStopTime(stop39, stop_time='10:12:00') # Golf - 166
trip.AddStopTime(stop40, stop_time='10:13:00') # Yadis - 53
trip.AddStopTime(stop41, stop_time='10:14:00') # Elmahari - 68
trip.AddStopTime(stop42, stop_time='10:17:00') # Elmanara - 157
trip.AddStopTime(stop43, stop_time='10:18:00') # Abou Nawess Golf - 87
trip.AddStopTime(stop44, stop_time='10:20:00') # Dar Jeba - 149
trip.AddStopTime(stop45, stop_time='10:22:00') # Phare Ennadhour - 149
trip.AddStopTime(stop74, stop_time='10:28:00') # Tanit - 364

trip = route.AddTrip(schedule, headsign="Tanit vers Houmet Souk")
trip.AddStopTime(stop74, stop_time='10:10:00') # Tanit - 0
trip.AddStopTime(stop45, stop_time='10:15:00') # Phare Ennadhour - 298
trip.AddStopTime(stop44, stop_time='10:16:00') # Dar Jeba - 78
trip.AddStopTime(stop43, stop_time='10:16:00') # Abou Nawess Golf - 26
trip.AddStopTime(stop42, stop_time='10:16:00') # Elmanara - 26
trip.AddStopTime(stop41, stop_time='10:16:00') # Elmahari - 20
trip.AddStopTime(stop40, stop_time='10:17:00') # Yadis - 44
trip.AddStopTime(stop39, stop_time='10:19:00') # Golf - 112
trip.AddStopTime(stop38, stop_time='10:19:00') # Plazza - 22
trip.AddStopTime(stop37, stop_time='10:20:00') # Elhana - 32
trip.AddStopTime(stop36, stop_time='10:21:00') # Minenx - 47
trip.AddStopTime(stop35, stop_time='10:22:00') # Hasdrubal - 36
trip.AddStopTime(stop34, stop_time='10:24:00') # R.D.V - 106
trip.AddStopTime(stop33, stop_time='10:25:00') # Dar Midoun - 88
trip.AddStopTime(stop32, stop_time='10:28:00') # Yasmina - 158
trip.AddStopTime(stop31, stop_time='10:30:00') # Toumana - 107
trip.AddStopTime(stop30, stop_time='10:32:00') # Palm Beach - 121
trip.AddStopTime(stop29, stop_time='10:33:00') # Abou Nawess - 53
trip.AddStopTime(stop28, stop_time='10:35:00') # Elmadina - 149
trip.AddStopTime(stop27, stop_time='10:37:00') # Holiday - 134
trip.AddStopTime(stop26, stop_time='10:38:00') # Dalli - 83
trip.AddStopTime(stop25, stop_time='10:41:00') # Eljazira - 199
trip.AddStopTime(stop24, stop_time='10:43:00') # Ulysse - 147
trip.AddStopTime(stop23, stop_time='10:44:00') # Athene - 72
trip.AddStopTime(stop22, stop_time='10:47:00') # Ras ettabia - 197
trip.AddStopTime(stop21, stop_time='10:48:00') # Elmagtaa - 58
trip.AddStopTime(stop20, stop_time='10:50:00') # Croisement Guisen - 101
trip.AddStopTime(stop19, stop_time='10:54:00') # Arouay - 245
trip.AddStopTime(stop18, stop_time='10:57:00') # Sidi Ismail - 162
trip.AddStopTime(stop17, stop_time='10:59:00') # Fatou2 - 125
trip.AddStopTime(stop16, stop_time='11:04:00') # Lobirette - 309
trip.AddStopTime(stop15, stop_time='11:07:00') # Sidi Zayed - 203
trip.AddStopTime(stop14, stop_time='11:09:00') # Elwilayia - 90
trip.AddStopTime(stop10, stop_time='11:15:00') # Houmet Souk - 384


trip = route.AddTrip(schedule, headsign="Houmet Souk vers Tanit")
trip.AddStopTime(stop10, stop_time='10:15:00') # Houmet Souk - 0
trip.AddStopTime(stop14, stop_time='10:21:00') # Elwilayia - 349
trip.AddStopTime(stop15, stop_time='10:23:00') # Sidi Zayed - 102
trip.AddStopTime(stop16, stop_time='10:24:00') # Lobirette - 84
trip.AddStopTime(stop17, stop_time='10:25:00') # Fatou2 - 49
trip.AddStopTime(stop18, stop_time='10:28:00') # Sidi Ismail - 209
trip.AddStopTime(stop19, stop_time='10:31:00') # Arouay - 202
trip.AddStopTime(stop20, stop_time='10:33:00') # Croisement Guisen - 91
trip.AddStopTime(stop21, stop_time='10:35:00') # Elmagtaa - 108
trip.AddStopTime(stop22, stop_time='10:38:00') # Ras ettabia - 155
trip.AddStopTime(stop23, stop_time='10:41:00') # Athene - 156
trip.AddStopTime(stop24, stop_time='10:44:00') # Ulysse - 178
trip.AddStopTime(stop25, stop_time='10:46:00') # Eljazira - 139
trip.AddStopTime(stop26, stop_time='10:48:00') # Dalli - 121
trip.AddStopTime(stop27, stop_time='10:49:00') # Holiday - 79
trip.AddStopTime(stop28, stop_time='10:52:00') # Elmadina - 166
trip.AddStopTime(stop29, stop_time='10:54:00') # Abou Nawess - 140
trip.AddStopTime(stop30, stop_time='10:55:00') # Palm Beach - 53
trip.AddStopTime(stop31, stop_time='10:58:00') # Toumana - 151
trip.AddStopTime(stop32, stop_time='10:59:00') # Yasmina - 39
trip.AddStopTime(stop33, stop_time='11:02:00') # Dar Midoun - 163
trip.AddStopTime(stop34, stop_time='11:03:00') # R.D.V - 63
trip.AddStopTime(stop35, stop_time='11:05:00') # Hasdrubal - 134
trip.AddStopTime(stop36, stop_time='11:06:00') # Minenx - 81
trip.AddStopTime(stop37, stop_time='11:07:00') # Elhana - 87
trip.AddStopTime(stop38, stop_time='11:09:00') # Plazza - 109
trip.AddStopTime(stop39, stop_time='11:12:00') # Golf - 166
trip.AddStopTime(stop40, stop_time='11:13:00') # Yadis - 53
trip.AddStopTime(stop41, stop_time='11:14:00') # Elmahari - 68
trip.AddStopTime(stop42, stop_time='11:17:00') # Elmanara - 157
trip.AddStopTime(stop43, stop_time='11:18:00') # Abou Nawess Golf - 87
trip.AddStopTime(stop44, stop_time='11:20:00') # Dar Jeba - 149
trip.AddStopTime(stop45, stop_time='11:22:00') # Phare Ennadhour - 149
trip.AddStopTime(stop74, stop_time='11:28:00') # Tanit - 364

trip = route.AddTrip(schedule, headsign="Tanit vers Houmet Souk")
trip.AddStopTime(stop74, stop_time='11:00:00') # Tanit - 0
trip.AddStopTime(stop45, stop_time='11:05:00') # Phare Ennadhour - 298
trip.AddStopTime(stop44, stop_time='11:06:00') # Dar Jeba - 78
trip.AddStopTime(stop43, stop_time='11:06:00') # Abou Nawess Golf - 26
trip.AddStopTime(stop42, stop_time='11:06:00') # Elmanara - 26
trip.AddStopTime(stop41, stop_time='11:06:00') # Elmahari - 20
trip.AddStopTime(stop40, stop_time='11:07:00') # Yadis - 44
trip.AddStopTime(stop39, stop_time='11:09:00') # Golf - 112
trip.AddStopTime(stop38, stop_time='11:09:00') # Plazza - 22
trip.AddStopTime(stop37, stop_time='11:10:00') # Elhana - 32
trip.AddStopTime(stop36, stop_time='11:11:00') # Minenx - 47
trip.AddStopTime(stop35, stop_time='11:12:00') # Hasdrubal - 36
trip.AddStopTime(stop34, stop_time='11:14:00') # R.D.V - 106
trip.AddStopTime(stop33, stop_time='11:15:00') # Dar Midoun - 88
trip.AddStopTime(stop32, stop_time='11:18:00') # Yasmina - 158
trip.AddStopTime(stop31, stop_time='11:20:00') # Toumana - 107
trip.AddStopTime(stop30, stop_time='11:22:00') # Palm Beach - 121
trip.AddStopTime(stop29, stop_time='11:23:00') # Abou Nawess - 53
trip.AddStopTime(stop28, stop_time='11:25:00') # Elmadina - 149
trip.AddStopTime(stop27, stop_time='11:27:00') # Holiday - 134
trip.AddStopTime(stop26, stop_time='11:28:00') # Dalli - 83
trip.AddStopTime(stop25, stop_time='11:31:00') # Eljazira - 199
trip.AddStopTime(stop24, stop_time='11:33:00') # Ulysse - 147
trip.AddStopTime(stop23, stop_time='11:34:00') # Athene - 72
trip.AddStopTime(stop22, stop_time='11:37:00') # Ras ettabia - 197
trip.AddStopTime(stop21, stop_time='11:38:00') # Elmagtaa - 58
trip.AddStopTime(stop20, stop_time='11:40:00') # Croisement Guisen - 101
trip.AddStopTime(stop19, stop_time='11:44:00') # Arouay - 245
trip.AddStopTime(stop18, stop_time='11:47:00') # Sidi Ismail - 162
trip.AddStopTime(stop17, stop_time='11:49:00') # Fatou2 - 125
trip.AddStopTime(stop16, stop_time='11:54:00') # Lobirette - 309
trip.AddStopTime(stop15, stop_time='11:57:00') # Sidi Zayed - 203
trip.AddStopTime(stop14, stop_time='11:59:00') # Elwilayia - 90
trip.AddStopTime(stop10, stop_time='12:05:00') # Houmet Souk - 384

trip = route.AddTrip(schedule, headsign="Houmet Souk vers Tanit")
trip.AddStopTime(stop10, stop_time='11:15:00') # Houmet Souk - 0
trip.AddStopTime(stop14, stop_time='11:21:00') # Elwilayia - 349
trip.AddStopTime(stop15, stop_time='11:23:00') # Sidi Zayed - 102
trip.AddStopTime(stop16, stop_time='11:24:00') # Lobirette - 84
trip.AddStopTime(stop17, stop_time='11:25:00') # Fatou2 - 49
trip.AddStopTime(stop18, stop_time='11:28:00') # Sidi Ismail - 209
trip.AddStopTime(stop19, stop_time='11:31:00') # Arouay - 202
trip.AddStopTime(stop20, stop_time='11:33:00') # Croisement Guisen - 91
trip.AddStopTime(stop21, stop_time='11:35:00') # Elmagtaa - 108
trip.AddStopTime(stop22, stop_time='11:38:00') # Ras ettabia - 155
trip.AddStopTime(stop23, stop_time='11:41:00') # Athene - 156
trip.AddStopTime(stop24, stop_time='11:44:00') # Ulysse - 178
trip.AddStopTime(stop25, stop_time='11:46:00') # Eljazira - 139
trip.AddStopTime(stop26, stop_time='11:48:00') # Dalli - 121
trip.AddStopTime(stop27, stop_time='11:49:00') # Holiday - 79
trip.AddStopTime(stop28, stop_time='11:52:00') # Elmadina - 166
trip.AddStopTime(stop29, stop_time='11:54:00') # Abou Nawess - 140
trip.AddStopTime(stop30, stop_time='11:55:00') # Palm Beach - 53
trip.AddStopTime(stop31, stop_time='11:58:00') # Toumana - 151
trip.AddStopTime(stop32, stop_time='11:59:00') # Yasmina - 39
trip.AddStopTime(stop33, stop_time='12:02:00') # Dar Midoun - 163
trip.AddStopTime(stop34, stop_time='12:03:00') # R.D.V - 63
trip.AddStopTime(stop35, stop_time='12:05:00') # Hasdrubal - 134
trip.AddStopTime(stop36, stop_time='12:06:00') # Minenx - 81
trip.AddStopTime(stop37, stop_time='12:07:00') # Elhana - 87
trip.AddStopTime(stop38, stop_time='12:09:00') # Plazza - 109
trip.AddStopTime(stop39, stop_time='12:12:00') # Golf - 166
trip.AddStopTime(stop40, stop_time='12:13:00') # Yadis - 53
trip.AddStopTime(stop41, stop_time='12:14:00') # Elmahari - 68
trip.AddStopTime(stop42, stop_time='12:17:00') # Elmanara - 157
trip.AddStopTime(stop43, stop_time='12:18:00') # Abou Nawess Golf - 87
trip.AddStopTime(stop44, stop_time='12:20:00') # Dar Jeba - 149
trip.AddStopTime(stop45, stop_time='12:22:00') # Phare Ennadhour - 149
trip.AddStopTime(stop74, stop_time='12:28:00') # Tanit - 364

trip = route.AddTrip(schedule, headsign="Tanit vers Houmet Souk")
trip.AddStopTime(stop74, stop_time='11:50:00') # Tanit - 0
trip.AddStopTime(stop45, stop_time='11:55:00') # Phare Ennadhour - 298
trip.AddStopTime(stop44, stop_time='11:56:00') # Dar Jeba - 78
trip.AddStopTime(stop43, stop_time='11:56:00') # Abou Nawess Golf - 26
trip.AddStopTime(stop42, stop_time='11:56:00') # Elmanara - 26
trip.AddStopTime(stop41, stop_time='11:56:00') # Elmahari - 20
trip.AddStopTime(stop40, stop_time='11:57:00') # Yadis - 44
trip.AddStopTime(stop39, stop_time='11:59:00') # Golf - 112
trip.AddStopTime(stop38, stop_time='11:59:00') # Plazza - 22
trip.AddStopTime(stop37, stop_time='12:00:00') # Elhana - 32
trip.AddStopTime(stop36, stop_time='12:01:00') # Minenx - 47
trip.AddStopTime(stop35, stop_time='12:02:00') # Hasdrubal - 36
trip.AddStopTime(stop34, stop_time='12:04:00') # R.D.V - 106
trip.AddStopTime(stop33, stop_time='12:05:00') # Dar Midoun - 88
trip.AddStopTime(stop32, stop_time='12:08:00') # Yasmina - 158
trip.AddStopTime(stop31, stop_time='12:10:00') # Toumana - 107
trip.AddStopTime(stop30, stop_time='12:12:00') # Palm Beach - 121
trip.AddStopTime(stop29, stop_time='12:13:00') # Abou Nawess - 53
trip.AddStopTime(stop28, stop_time='12:15:00') # Elmadina - 149
trip.AddStopTime(stop27, stop_time='12:17:00') # Holiday - 134
trip.AddStopTime(stop26, stop_time='12:18:00') # Dalli - 83
trip.AddStopTime(stop25, stop_time='12:21:00') # Eljazira - 199
trip.AddStopTime(stop24, stop_time='12:23:00') # Ulysse - 147
trip.AddStopTime(stop23, stop_time='12:24:00') # Athene - 72
trip.AddStopTime(stop22, stop_time='12:27:00') # Ras ettabia - 197
trip.AddStopTime(stop21, stop_time='12:28:00') # Elmagtaa - 58
trip.AddStopTime(stop20, stop_time='12:30:00') # Croisement Guisen - 101
trip.AddStopTime(stop19, stop_time='12:34:00') # Arouay - 245
trip.AddStopTime(stop18, stop_time='12:37:00') # Sidi Ismail - 162
trip.AddStopTime(stop17, stop_time='12:39:00') # Fatou2 - 125
trip.AddStopTime(stop16, stop_time='12:44:00') # Lobirette - 309
trip.AddStopTime(stop15, stop_time='12:47:00') # Sidi Zayed - 203
trip.AddStopTime(stop14, stop_time='12:49:00') # Elwilayia - 90
trip.AddStopTime(stop10, stop_time='12:55:00') # Houmet Souk - 384

trip = route.AddTrip(schedule, headsign="Houmet Souk vers Tanit")
trip.AddStopTime(stop10, stop_time='12:15:00') # Houmet Souk - 0
trip.AddStopTime(stop14, stop_time='12:21:00') # Elwilayia - 349
trip.AddStopTime(stop15, stop_time='12:23:00') # Sidi Zayed - 102
trip.AddStopTime(stop16, stop_time='12:24:00') # Lobirette - 84
trip.AddStopTime(stop17, stop_time='12:25:00') # Fatou2 - 49
trip.AddStopTime(stop18, stop_time='12:28:00') # Sidi Ismail - 209
trip.AddStopTime(stop19, stop_time='12:31:00') # Arouay - 202
trip.AddStopTime(stop20, stop_time='12:33:00') # Croisement Guisen - 91
trip.AddStopTime(stop21, stop_time='12:35:00') # Elmagtaa - 108
trip.AddStopTime(stop22, stop_time='12:38:00') # Ras ettabia - 155
trip.AddStopTime(stop23, stop_time='12:41:00') # Athene - 156
trip.AddStopTime(stop24, stop_time='12:44:00') # Ulysse - 178
trip.AddStopTime(stop25, stop_time='12:46:00') # Eljazira - 139
trip.AddStopTime(stop26, stop_time='12:48:00') # Dalli - 121
trip.AddStopTime(stop27, stop_time='12:49:00') # Holiday - 79
trip.AddStopTime(stop28, stop_time='12:52:00') # Elmadina - 166
trip.AddStopTime(stop29, stop_time='12:54:00') # Abou Nawess - 140
trip.AddStopTime(stop30, stop_time='12:55:00') # Palm Beach - 53
trip.AddStopTime(stop31, stop_time='12:58:00') # Toumana - 151
trip.AddStopTime(stop32, stop_time='12:59:00') # Yasmina - 39
trip.AddStopTime(stop33, stop_time='13:02:00') # Dar Midoun - 163
trip.AddStopTime(stop34, stop_time='13:03:00') # R.D.V - 63
trip.AddStopTime(stop35, stop_time='13:05:00') # Hasdrubal - 134
trip.AddStopTime(stop36, stop_time='13:06:00') # Minenx - 81
trip.AddStopTime(stop37, stop_time='13:07:00') # Elhana - 87
trip.AddStopTime(stop38, stop_time='13:09:00') # Plazza - 109
trip.AddStopTime(stop39, stop_time='13:12:00') # Golf - 166
trip.AddStopTime(stop40, stop_time='13:13:00') # Yadis - 53
trip.AddStopTime(stop41, stop_time='13:14:00') # Elmahari - 68
trip.AddStopTime(stop42, stop_time='13:17:00') # Elmanara - 157
trip.AddStopTime(stop43, stop_time='13:18:00') # Abou Nawess Golf - 87
trip.AddStopTime(stop44, stop_time='13:20:00') # Dar Jeba - 149
trip.AddStopTime(stop45, stop_time='13:22:00') # Phare Ennadhour - 149
trip.AddStopTime(stop74, stop_time='13:28:00') # Tanit - 364

trip = route.AddTrip(schedule, headsign="Tanit vers Houmet Souk")
trip.AddStopTime(stop74, stop_time='13:00:00') # Tanit - 0
trip.AddStopTime(stop45, stop_time='13:05:00') # Phare Ennadhour - 298
trip.AddStopTime(stop44, stop_time='13:06:00') # Dar Jeba - 78
trip.AddStopTime(stop43, stop_time='13:06:00') # Abou Nawess Golf - 26
trip.AddStopTime(stop42, stop_time='13:06:00') # Elmanara - 26
trip.AddStopTime(stop41, stop_time='13:06:00') # Elmahari - 20
trip.AddStopTime(stop40, stop_time='13:07:00') # Yadis - 44
trip.AddStopTime(stop39, stop_time='13:09:00') # Golf - 112
trip.AddStopTime(stop38, stop_time='13:09:00') # Plazza - 22
trip.AddStopTime(stop37, stop_time='13:10:00') # Elhana - 32
trip.AddStopTime(stop36, stop_time='13:11:00') # Minenx - 47
trip.AddStopTime(stop35, stop_time='13:12:00') # Hasdrubal - 36
trip.AddStopTime(stop34, stop_time='13:14:00') # R.D.V - 106
trip.AddStopTime(stop33, stop_time='13:15:00') # Dar Midoun - 88
trip.AddStopTime(stop32, stop_time='13:18:00') # Yasmina - 158
trip.AddStopTime(stop31, stop_time='13:20:00') # Toumana - 107
trip.AddStopTime(stop30, stop_time='13:22:00') # Palm Beach - 121
trip.AddStopTime(stop29, stop_time='13:23:00') # Abou Nawess - 53
trip.AddStopTime(stop28, stop_time='13:25:00') # Elmadina - 149
trip.AddStopTime(stop27, stop_time='13:27:00') # Holiday - 134
trip.AddStopTime(stop26, stop_time='13:28:00') # Dalli - 83
trip.AddStopTime(stop25, stop_time='13:31:00') # Eljazira - 199
trip.AddStopTime(stop24, stop_time='13:33:00') # Ulysse - 147
trip.AddStopTime(stop23, stop_time='13:34:00') # Athene - 72
trip.AddStopTime(stop22, stop_time='13:37:00') # Ras ettabia - 197
trip.AddStopTime(stop21, stop_time='13:38:00') # Elmagtaa - 58
trip.AddStopTime(stop20, stop_time='13:40:00') # Croisement Guisen - 101
trip.AddStopTime(stop19, stop_time='13:44:00') # Arouay - 245
trip.AddStopTime(stop18, stop_time='13:47:00') # Sidi Ismail - 162
trip.AddStopTime(stop17, stop_time='13:49:00') # Fatou2 - 125
trip.AddStopTime(stop16, stop_time='13:54:00') # Lobirette - 309
trip.AddStopTime(stop15, stop_time='13:57:00') # Sidi Zayed - 203
trip.AddStopTime(stop14, stop_time='13:59:00') # Elwilayia - 90
trip.AddStopTime(stop10, stop_time='14:05:00') # Houmet Souk - 384

trip = route.AddTrip(schedule, headsign="Houmet Souk vers Tanit")
trip.AddStopTime(stop10, stop_time='13:15:00') # Houmet Souk - 0
trip.AddStopTime(stop14, stop_time='13:21:00') # Elwilayia - 349
trip.AddStopTime(stop15, stop_time='13:23:00') # Sidi Zayed - 102
trip.AddStopTime(stop16, stop_time='13:24:00') # Lobirette - 84
trip.AddStopTime(stop17, stop_time='13:25:00') # Fatou2 - 49
trip.AddStopTime(stop18, stop_time='13:28:00') # Sidi Ismail - 209
trip.AddStopTime(stop19, stop_time='13:31:00') # Arouay - 202
trip.AddStopTime(stop20, stop_time='13:33:00') # Croisement Guisen - 91
trip.AddStopTime(stop21, stop_time='13:35:00') # Elmagtaa - 108
trip.AddStopTime(stop22, stop_time='13:38:00') # Ras ettabia - 155
trip.AddStopTime(stop23, stop_time='13:41:00') # Athene - 156
trip.AddStopTime(stop24, stop_time='13:44:00') # Ulysse - 178
trip.AddStopTime(stop25, stop_time='13:46:00') # Eljazira - 139
trip.AddStopTime(stop26, stop_time='13:48:00') # Dalli - 121
trip.AddStopTime(stop27, stop_time='13:49:00') # Holiday - 79
trip.AddStopTime(stop28, stop_time='13:52:00') # Elmadina - 166
trip.AddStopTime(stop29, stop_time='13:54:00') # Abou Nawess - 140
trip.AddStopTime(stop30, stop_time='13:55:00') # Palm Beach - 53
trip.AddStopTime(stop31, stop_time='13:58:00') # Toumana - 151
trip.AddStopTime(stop32, stop_time='13:59:00') # Yasmina - 39
trip.AddStopTime(stop33, stop_time='14:02:00') # Dar Midoun - 163
trip.AddStopTime(stop34, stop_time='14:03:00') # R.D.V - 63
trip.AddStopTime(stop35, stop_time='14:05:00') # Hasdrubal - 134
trip.AddStopTime(stop36, stop_time='14:06:00') # Minenx - 81
trip.AddStopTime(stop37, stop_time='14:07:00') # Elhana - 87
trip.AddStopTime(stop38, stop_time='14:09:00') # Plazza - 109
trip.AddStopTime(stop39, stop_time='14:12:00') # Golf - 166
trip.AddStopTime(stop40, stop_time='14:13:00') # Yadis - 53
trip.AddStopTime(stop41, stop_time='14:14:00') # Elmahari - 68
trip.AddStopTime(stop42, stop_time='14:17:00') # Elmanara - 157
trip.AddStopTime(stop43, stop_time='14:18:00') # Abou Nawess Golf - 87
trip.AddStopTime(stop44, stop_time='14:20:00') # Dar Jeba - 149
trip.AddStopTime(stop45, stop_time='14:22:00') # Phare Ennadhour - 149
trip.AddStopTime(stop74, stop_time='14:28:00') # Tanit - 364

trip = route.AddTrip(schedule, headsign="Tanit vers Houmet Souk")
trip.AddStopTime(stop74, stop_time='14:30:00') # Tanit - 0
trip.AddStopTime(stop45, stop_time='14:35:00') # Phare Ennadhour - 298
trip.AddStopTime(stop44, stop_time='14:36:00') # Dar Jeba - 78
trip.AddStopTime(stop43, stop_time='14:36:00') # Abou Nawess Golf - 26
trip.AddStopTime(stop42, stop_time='14:36:00') # Elmanara - 26
trip.AddStopTime(stop41, stop_time='14:36:00') # Elmahari - 20
trip.AddStopTime(stop40, stop_time='14:37:00') # Yadis - 44
trip.AddStopTime(stop39, stop_time='14:39:00') # Golf - 112
trip.AddStopTime(stop38, stop_time='14:39:00') # Plazza - 22
trip.AddStopTime(stop37, stop_time='14:40:00') # Elhana - 32
trip.AddStopTime(stop36, stop_time='14:41:00') # Minenx - 47
trip.AddStopTime(stop35, stop_time='14:42:00') # Hasdrubal - 36
trip.AddStopTime(stop34, stop_time='14:44:00') # R.D.V - 106
trip.AddStopTime(stop33, stop_time='14:45:00') # Dar Midoun - 88
trip.AddStopTime(stop32, stop_time='14:48:00') # Yasmina - 158
trip.AddStopTime(stop31, stop_time='14:50:00') # Toumana - 107
trip.AddStopTime(stop30, stop_time='14:52:00') # Palm Beach - 121
trip.AddStopTime(stop29, stop_time='14:53:00') # Abou Nawess - 53
trip.AddStopTime(stop28, stop_time='14:55:00') # Elmadina - 149
trip.AddStopTime(stop27, stop_time='14:57:00') # Holiday - 134
trip.AddStopTime(stop26, stop_time='14:58:00') # Dalli - 83
trip.AddStopTime(stop25, stop_time='15:01:00') # Eljazira - 199
trip.AddStopTime(stop24, stop_time='15:03:00') # Ulysse - 147
trip.AddStopTime(stop23, stop_time='15:04:00') # Athene - 72
trip.AddStopTime(stop22, stop_time='15:07:00') # Ras ettabia - 197
trip.AddStopTime(stop21, stop_time='15:08:00') # Elmagtaa - 58
trip.AddStopTime(stop20, stop_time='15:10:00') # Croisement Guisen - 101
trip.AddStopTime(stop19, stop_time='15:14:00') # Arouay - 245
trip.AddStopTime(stop18, stop_time='15:17:00') # Sidi Ismail - 162
trip.AddStopTime(stop17, stop_time='15:19:00') # Fatou2 - 125
trip.AddStopTime(stop16, stop_time='15:24:00') # Lobirette - 309
trip.AddStopTime(stop15, stop_time='15:27:00') # Sidi Zayed - 203
trip.AddStopTime(stop14, stop_time='15:29:00') # Elwilayia - 90
trip.AddStopTime(stop10, stop_time='15:35:00') # Houmet Souk - 384

trip = route.AddTrip(schedule, headsign="Houmet Souk vers Tanit")
trip.AddStopTime(stop10, stop_time='14:00:00') # Houmet Souk - 0
trip.AddStopTime(stop14, stop_time='14:06:00') # Elwilayia - 349
trip.AddStopTime(stop15, stop_time='14:08:00') # Sidi Zayed - 102
trip.AddStopTime(stop16, stop_time='14:09:00') # Lobirette - 84
trip.AddStopTime(stop17, stop_time='14:10:00') # Fatou2 - 49
trip.AddStopTime(stop18, stop_time='14:13:00') # Sidi Ismail - 209
trip.AddStopTime(stop19, stop_time='14:16:00') # Arouay - 202
trip.AddStopTime(stop20, stop_time='14:18:00') # Croisement Guisen - 91
trip.AddStopTime(stop21, stop_time='14:20:00') # Elmagtaa - 108
trip.AddStopTime(stop22, stop_time='14:23:00') # Ras ettabia - 155
trip.AddStopTime(stop23, stop_time='14:26:00') # Athene - 156
trip.AddStopTime(stop24, stop_time='14:29:00') # Ulysse - 178
trip.AddStopTime(stop25, stop_time='14:31:00') # Eljazira - 139
trip.AddStopTime(stop26, stop_time='14:33:00') # Dalli - 121
trip.AddStopTime(stop27, stop_time='14:34:00') # Holiday - 79
trip.AddStopTime(stop28, stop_time='14:37:00') # Elmadina - 166
trip.AddStopTime(stop29, stop_time='14:39:00') # Abou Nawess - 140
trip.AddStopTime(stop30, stop_time='14:40:00') # Palm Beach - 53
trip.AddStopTime(stop31, stop_time='14:43:00') # Toumana - 151
trip.AddStopTime(stop32, stop_time='14:44:00') # Yasmina - 39
trip.AddStopTime(stop33, stop_time='14:47:00') # Dar Midoun - 163
trip.AddStopTime(stop34, stop_time='14:48:00') # R.D.V - 63
trip.AddStopTime(stop35, stop_time='14:50:00') # Hasdrubal - 134
trip.AddStopTime(stop36, stop_time='14:51:00') # Minenx - 81
trip.AddStopTime(stop37, stop_time='14:52:00') # Elhana - 87
trip.AddStopTime(stop38, stop_time='14:54:00') # Plazza - 109
trip.AddStopTime(stop39, stop_time='14:57:00') # Golf - 166
trip.AddStopTime(stop40, stop_time='14:58:00') # Yadis - 53
trip.AddStopTime(stop41, stop_time='14:59:00') # Elmahari - 68
trip.AddStopTime(stop42, stop_time='15:02:00') # Elmanara - 157
trip.AddStopTime(stop43, stop_time='15:03:00') # Abou Nawess Golf - 87
trip.AddStopTime(stop44, stop_time='15:05:00') # Dar Jeba - 149
trip.AddStopTime(stop45, stop_time='15:07:00') # Phare Ennadhour - 149
trip.AddStopTime(stop74, stop_time='15:13:00') # Tanit - 364

trip = route.AddTrip(schedule, headsign="Tanit vers Houmet Souk")
trip.AddStopTime(stop74, stop_time='15:00:00') # Tanit - 0
trip.AddStopTime(stop45, stop_time='15:05:00') # Phare Ennadhour - 298
trip.AddStopTime(stop44, stop_time='15:06:00') # Dar Jeba - 78
trip.AddStopTime(stop43, stop_time='15:06:00') # Abou Nawess Golf - 26
trip.AddStopTime(stop42, stop_time='15:06:00') # Elmanara - 26
trip.AddStopTime(stop41, stop_time='15:06:00') # Elmahari - 20
trip.AddStopTime(stop40, stop_time='15:07:00') # Yadis - 44
trip.AddStopTime(stop39, stop_time='15:09:00') # Golf - 112
trip.AddStopTime(stop38, stop_time='15:09:00') # Plazza - 22
trip.AddStopTime(stop37, stop_time='15:10:00') # Elhana - 32
trip.AddStopTime(stop36, stop_time='15:11:00') # Minenx - 47
trip.AddStopTime(stop35, stop_time='15:12:00') # Hasdrubal - 36
trip.AddStopTime(stop34, stop_time='15:14:00') # R.D.V - 106
trip.AddStopTime(stop33, stop_time='15:15:00') # Dar Midoun - 88
trip.AddStopTime(stop32, stop_time='15:18:00') # Yasmina - 158
trip.AddStopTime(stop31, stop_time='15:20:00') # Toumana - 107
trip.AddStopTime(stop30, stop_time='15:22:00') # Palm Beach - 121
trip.AddStopTime(stop29, stop_time='15:23:00') # Abou Nawess - 53
trip.AddStopTime(stop28, stop_time='15:25:00') # Elmadina - 149
trip.AddStopTime(stop27, stop_time='15:27:00') # Holiday - 134
trip.AddStopTime(stop26, stop_time='15:28:00') # Dalli - 83
trip.AddStopTime(stop25, stop_time='15:31:00') # Eljazira - 199
trip.AddStopTime(stop24, stop_time='15:33:00') # Ulysse - 147
trip.AddStopTime(stop23, stop_time='15:34:00') # Athene - 72
trip.AddStopTime(stop22, stop_time='15:37:00') # Ras ettabia - 197
trip.AddStopTime(stop21, stop_time='15:38:00') # Elmagtaa - 58
trip.AddStopTime(stop20, stop_time='15:40:00') # Croisement Guisen - 101
trip.AddStopTime(stop19, stop_time='15:44:00') # Arouay - 245
trip.AddStopTime(stop18, stop_time='15:47:00') # Sidi Ismail - 162
trip.AddStopTime(stop17, stop_time='15:49:00') # Fatou2 - 125
trip.AddStopTime(stop16, stop_time='15:54:00') # Lobirette - 309
trip.AddStopTime(stop15, stop_time='15:57:00') # Sidi Zayed - 203
trip.AddStopTime(stop14, stop_time='15:59:00') # Elwilayia - 90
trip.AddStopTime(stop10, stop_time='16:05:00') # Houmet Souk - 384


trip = route.AddTrip(schedule, headsign="Houmet Souk vers Tanit")
trip.AddStopTime(stop10, stop_time='15:15:00') # Houmet Souk - 0
trip.AddStopTime(stop14, stop_time='15:21:00') # Elwilayia - 349
trip.AddStopTime(stop15, stop_time='15:23:00') # Sidi Zayed - 102
trip.AddStopTime(stop16, stop_time='15:24:00') # Lobirette - 84
trip.AddStopTime(stop17, stop_time='15:25:00') # Fatou2 - 49
trip.AddStopTime(stop18, stop_time='15:28:00') # Sidi Ismail - 209
trip.AddStopTime(stop19, stop_time='15:31:00') # Arouay - 202
trip.AddStopTime(stop20, stop_time='15:33:00') # Croisement Guisen - 91
trip.AddStopTime(stop21, stop_time='15:35:00') # Elmagtaa - 108
trip.AddStopTime(stop22, stop_time='15:38:00') # Ras ettabia - 155
trip.AddStopTime(stop23, stop_time='15:41:00') # Athene - 156
trip.AddStopTime(stop24, stop_time='15:44:00') # Ulysse - 178
trip.AddStopTime(stop25, stop_time='15:46:00') # Eljazira - 139
trip.AddStopTime(stop26, stop_time='15:48:00') # Dalli - 121
trip.AddStopTime(stop27, stop_time='15:49:00') # Holiday - 79
trip.AddStopTime(stop28, stop_time='15:52:00') # Elmadina - 166
trip.AddStopTime(stop29, stop_time='15:54:00') # Abou Nawess - 140
trip.AddStopTime(stop30, stop_time='15:55:00') # Palm Beach - 53
trip.AddStopTime(stop31, stop_time='15:58:00') # Toumana - 151
trip.AddStopTime(stop32, stop_time='15:59:00') # Yasmina - 39
trip.AddStopTime(stop33, stop_time='16:02:00') # Dar Midoun - 163
trip.AddStopTime(stop34, stop_time='16:03:00') # R.D.V - 63
trip.AddStopTime(stop35, stop_time='16:05:00') # Hasdrubal - 134
trip.AddStopTime(stop36, stop_time='16:06:00') # Minenx - 81
trip.AddStopTime(stop37, stop_time='16:07:00') # Elhana - 87
trip.AddStopTime(stop38, stop_time='16:09:00') # Plazza - 109
trip.AddStopTime(stop39, stop_time='16:12:00') # Golf - 166
trip.AddStopTime(stop40, stop_time='16:13:00') # Yadis - 53
trip.AddStopTime(stop41, stop_time='16:14:00') # Elmahari - 68
trip.AddStopTime(stop42, stop_time='16:17:00') # Elmanara - 157
trip.AddStopTime(stop43, stop_time='16:18:00') # Abou Nawess Golf - 87
trip.AddStopTime(stop44, stop_time='16:20:00') # Dar Jeba - 149
trip.AddStopTime(stop45, stop_time='16:22:00') # Phare Ennadhour - 149
trip.AddStopTime(stop74, stop_time='16:28:00') # Tanit - 364

trip = route.AddTrip(schedule, headsign="Tanit vers Houmet Souk")
trip.AddStopTime(stop74, stop_time='16:00:00') # Tanit - 0
trip.AddStopTime(stop45, stop_time='16:05:00') # Phare Ennadhour - 298
trip.AddStopTime(stop44, stop_time='16:06:00') # Dar Jeba - 78
trip.AddStopTime(stop43, stop_time='16:06:00') # Abou Nawess Golf - 26
trip.AddStopTime(stop42, stop_time='16:06:00') # Elmanara - 26
trip.AddStopTime(stop41, stop_time='16:06:00') # Elmahari - 20
trip.AddStopTime(stop40, stop_time='16:07:00') # Yadis - 44
trip.AddStopTime(stop39, stop_time='16:09:00') # Golf - 112
trip.AddStopTime(stop38, stop_time='16:09:00') # Plazza - 22
trip.AddStopTime(stop37, stop_time='16:10:00') # Elhana - 32
trip.AddStopTime(stop36, stop_time='16:11:00') # Minenx - 47
trip.AddStopTime(stop35, stop_time='16:12:00') # Hasdrubal - 36
trip.AddStopTime(stop34, stop_time='16:14:00') # R.D.V - 106
trip.AddStopTime(stop33, stop_time='16:15:00') # Dar Midoun - 88
trip.AddStopTime(stop32, stop_time='16:18:00') # Yasmina - 158
trip.AddStopTime(stop31, stop_time='16:20:00') # Toumana - 107
trip.AddStopTime(stop30, stop_time='16:22:00') # Palm Beach - 121
trip.AddStopTime(stop29, stop_time='16:23:00') # Abou Nawess - 53
trip.AddStopTime(stop28, stop_time='16:25:00') # Elmadina - 149
trip.AddStopTime(stop27, stop_time='16:27:00') # Holiday - 134
trip.AddStopTime(stop26, stop_time='16:28:00') # Dalli - 83
trip.AddStopTime(stop25, stop_time='16:31:00') # Eljazira - 199
trip.AddStopTime(stop24, stop_time='16:33:00') # Ulysse - 147
trip.AddStopTime(stop23, stop_time='16:34:00') # Athene - 72
trip.AddStopTime(stop22, stop_time='16:37:00') # Ras ettabia - 197
trip.AddStopTime(stop21, stop_time='16:38:00') # Elmagtaa - 58
trip.AddStopTime(stop20, stop_time='16:40:00') # Croisement Guisen - 101
trip.AddStopTime(stop19, stop_time='16:44:00') # Arouay - 245
trip.AddStopTime(stop18, stop_time='16:47:00') # Sidi Ismail - 162
trip.AddStopTime(stop17, stop_time='16:49:00') # Fatou2 - 125
trip.AddStopTime(stop16, stop_time='16:54:00') # Lobirette - 309
trip.AddStopTime(stop15, stop_time='16:57:00') # Sidi Zayed - 203
trip.AddStopTime(stop14, stop_time='16:59:00') # Elwilayia - 90
trip.AddStopTime(stop10, stop_time='17:05:00') # Houmet Souk - 384

trip = route.AddTrip(schedule, headsign="Houmet Souk vers Tanit")
trip.AddStopTime(stop10, stop_time='16:00:00') # Houmet Souk - 0
trip.AddStopTime(stop14, stop_time='16:06:00') # Elwilayia - 349
trip.AddStopTime(stop15, stop_time='16:08:00') # Sidi Zayed - 102
trip.AddStopTime(stop16, stop_time='16:09:00') # Lobirette - 84
trip.AddStopTime(stop17, stop_time='16:10:00') # Fatou2 - 49
trip.AddStopTime(stop18, stop_time='16:13:00') # Sidi Ismail - 209
trip.AddStopTime(stop19, stop_time='16:16:00') # Arouay - 202
trip.AddStopTime(stop20, stop_time='16:18:00') # Croisement Guisen - 91
trip.AddStopTime(stop21, stop_time='16:20:00') # Elmagtaa - 108
trip.AddStopTime(stop22, stop_time='16:23:00') # Ras ettabia - 155
trip.AddStopTime(stop23, stop_time='16:26:00') # Athene - 156
trip.AddStopTime(stop24, stop_time='16:29:00') # Ulysse - 178
trip.AddStopTime(stop25, stop_time='16:31:00') # Eljazira - 139
trip.AddStopTime(stop26, stop_time='16:33:00') # Dalli - 121
trip.AddStopTime(stop27, stop_time='16:34:00') # Holiday - 79
trip.AddStopTime(stop28, stop_time='16:37:00') # Elmadina - 166
trip.AddStopTime(stop29, stop_time='16:39:00') # Abou Nawess - 140
trip.AddStopTime(stop30, stop_time='16:40:00') # Palm Beach - 53
trip.AddStopTime(stop31, stop_time='16:43:00') # Toumana - 151
trip.AddStopTime(stop32, stop_time='16:44:00') # Yasmina - 39
trip.AddStopTime(stop33, stop_time='16:47:00') # Dar Midoun - 163
trip.AddStopTime(stop34, stop_time='16:48:00') # R.D.V - 63
trip.AddStopTime(stop35, stop_time='16:50:00') # Hasdrubal - 134
trip.AddStopTime(stop36, stop_time='16:51:00') # Minenx - 81
trip.AddStopTime(stop37, stop_time='16:52:00') # Elhana - 87
trip.AddStopTime(stop38, stop_time='16:54:00') # Plazza - 109
trip.AddStopTime(stop39, stop_time='16:57:00') # Golf - 166
trip.AddStopTime(stop40, stop_time='16:58:00') # Yadis - 53
trip.AddStopTime(stop41, stop_time='16:59:00') # Elmahari - 68
trip.AddStopTime(stop42, stop_time='17:02:00') # Elmanara - 157
trip.AddStopTime(stop43, stop_time='17:03:00') # Abou Nawess Golf - 87
trip.AddStopTime(stop44, stop_time='17:05:00') # Dar Jeba - 149
trip.AddStopTime(stop45, stop_time='17:07:00') # Phare Ennadhour - 149
trip.AddStopTime(stop74, stop_time='17:13:00') # Tanit - 364

trip = route.AddTrip(schedule, headsign="Tanit vers Houmet Souk")
trip.AddStopTime(stop74, stop_time='16:15:00') # Tanit - 0
trip.AddStopTime(stop45, stop_time='16:20:00') # Phare Ennadhour - 298
trip.AddStopTime(stop44, stop_time='16:21:00') # Dar Jeba - 78
trip.AddStopTime(stop43, stop_time='16:21:00') # Abou Nawess Golf - 26
trip.AddStopTime(stop42, stop_time='16:21:00') # Elmanara - 26
trip.AddStopTime(stop41, stop_time='16:21:00') # Elmahari - 20
trip.AddStopTime(stop40, stop_time='16:22:00') # Yadis - 44
trip.AddStopTime(stop39, stop_time='16:24:00') # Golf - 112
trip.AddStopTime(stop38, stop_time='16:24:00') # Plazza - 22
trip.AddStopTime(stop37, stop_time='16:25:00') # Elhana - 32
trip.AddStopTime(stop36, stop_time='16:26:00') # Minenx - 47
trip.AddStopTime(stop35, stop_time='16:27:00') # Hasdrubal - 36
trip.AddStopTime(stop34, stop_time='16:29:00') # R.D.V - 106
trip.AddStopTime(stop33, stop_time='16:30:00') # Dar Midoun - 88
trip.AddStopTime(stop32, stop_time='16:33:00') # Yasmina - 158
trip.AddStopTime(stop31, stop_time='16:35:00') # Toumana - 107
trip.AddStopTime(stop30, stop_time='16:37:00') # Palm Beach - 121
trip.AddStopTime(stop29, stop_time='16:38:00') # Abou Nawess - 53
trip.AddStopTime(stop28, stop_time='16:40:00') # Elmadina - 149
trip.AddStopTime(stop27, stop_time='16:42:00') # Holiday - 134
trip.AddStopTime(stop26, stop_time='16:43:00') # Dalli - 83
trip.AddStopTime(stop25, stop_time='16:46:00') # Eljazira - 199
trip.AddStopTime(stop24, stop_time='16:48:00') # Ulysse - 147
trip.AddStopTime(stop23, stop_time='16:49:00') # Athene - 72
trip.AddStopTime(stop22, stop_time='16:52:00') # Ras ettabia - 197
trip.AddStopTime(stop21, stop_time='16:53:00') # Elmagtaa - 58
trip.AddStopTime(stop20, stop_time='16:55:00') # Croisement Guisen - 101
trip.AddStopTime(stop19, stop_time='16:59:00') # Arouay - 245
trip.AddStopTime(stop18, stop_time='17:02:00') # Sidi Ismail - 162
trip.AddStopTime(stop17, stop_time='17:04:00') # Fatou2 - 125
trip.AddStopTime(stop16, stop_time='17:09:00') # Lobirette - 309
trip.AddStopTime(stop15, stop_time='17:12:00') # Sidi Zayed - 203
trip.AddStopTime(stop14, stop_time='17:14:00') # Elwilayia - 90
trip.AddStopTime(stop10, stop_time='17:20:00') # Houmet Souk - 384

trip = route.AddTrip(schedule, headsign="Houmet Souk vers Tanit")
trip.AddStopTime(stop10, stop_time='17:15:00') # Houmet Souk - 0
trip.AddStopTime(stop14, stop_time='17:21:00') # Elwilayia - 349
trip.AddStopTime(stop15, stop_time='17:23:00') # Sidi Zayed - 102
trip.AddStopTime(stop16, stop_time='17:24:00') # Lobirette - 84
trip.AddStopTime(stop17, stop_time='17:25:00') # Fatou2 - 49
trip.AddStopTime(stop18, stop_time='17:28:00') # Sidi Ismail - 209
trip.AddStopTime(stop19, stop_time='17:31:00') # Arouay - 202
trip.AddStopTime(stop20, stop_time='17:33:00') # Croisement Guisen - 91
trip.AddStopTime(stop21, stop_time='17:35:00') # Elmagtaa - 108
trip.AddStopTime(stop22, stop_time='17:38:00') # Ras ettabia - 155
trip.AddStopTime(stop23, stop_time='17:41:00') # Athene - 156
trip.AddStopTime(stop24, stop_time='17:44:00') # Ulysse - 178
trip.AddStopTime(stop25, stop_time='17:46:00') # Eljazira - 139
trip.AddStopTime(stop26, stop_time='17:48:00') # Dalli - 121
trip.AddStopTime(stop27, stop_time='17:49:00') # Holiday - 79
trip.AddStopTime(stop28, stop_time='17:52:00') # Elmadina - 166
trip.AddStopTime(stop29, stop_time='17:54:00') # Abou Nawess - 140
trip.AddStopTime(stop30, stop_time='17:55:00') # Palm Beach - 53
trip.AddStopTime(stop31, stop_time='17:58:00') # Toumana - 151
trip.AddStopTime(stop32, stop_time='17:59:00') # Yasmina - 39
trip.AddStopTime(stop33, stop_time='18:02:00') # Dar Midoun - 163
trip.AddStopTime(stop34, stop_time='18:03:00') # R.D.V - 63
trip.AddStopTime(stop35, stop_time='18:05:00') # Hasdrubal - 134
trip.AddStopTime(stop36, stop_time='18:06:00') # Minenx - 81
trip.AddStopTime(stop37, stop_time='18:07:00') # Elhana - 87
trip.AddStopTime(stop38, stop_time='18:09:00') # Plazza - 109
trip.AddStopTime(stop39, stop_time='18:12:00') # Golf - 166
trip.AddStopTime(stop40, stop_time='18:13:00') # Yadis - 53
trip.AddStopTime(stop41, stop_time='18:14:00') # Elmahari - 68
trip.AddStopTime(stop42, stop_time='18:17:00') # Elmanara - 157
trip.AddStopTime(stop43, stop_time='18:18:00') # Abou Nawess Golf - 87
trip.AddStopTime(stop44, stop_time='18:20:00') # Dar Jeba - 149
trip.AddStopTime(stop45, stop_time='18:22:00') # Phare Ennadhour - 149
trip.AddStopTime(stop74, stop_time='18:28:00') # Tanit - 364

trip = route.AddTrip(schedule, headsign="Tanit vers Houmet Souk")
trip.AddStopTime(stop74, stop_time='17:20:00') # Tanit - 0
trip.AddStopTime(stop45, stop_time='17:25:00') # Phare Ennadhour - 298
trip.AddStopTime(stop44, stop_time='17:26:00') # Dar Jeba - 78
trip.AddStopTime(stop43, stop_time='17:26:00') # Abou Nawess Golf - 26
trip.AddStopTime(stop42, stop_time='17:26:00') # Elmanara - 26
trip.AddStopTime(stop41, stop_time='17:26:00') # Elmahari - 20
trip.AddStopTime(stop40, stop_time='17:27:00') # Yadis - 44
trip.AddStopTime(stop39, stop_time='17:29:00') # Golf - 112
trip.AddStopTime(stop38, stop_time='17:29:00') # Plazza - 22
trip.AddStopTime(stop37, stop_time='17:30:00') # Elhana - 32
trip.AddStopTime(stop36, stop_time='17:31:00') # Minenx - 47
trip.AddStopTime(stop35, stop_time='17:32:00') # Hasdrubal - 36
trip.AddStopTime(stop34, stop_time='17:34:00') # R.D.V - 106
trip.AddStopTime(stop33, stop_time='17:35:00') # Dar Midoun - 88
trip.AddStopTime(stop32, stop_time='17:38:00') # Yasmina - 158
trip.AddStopTime(stop31, stop_time='17:40:00') # Toumana - 107
trip.AddStopTime(stop30, stop_time='17:42:00') # Palm Beach - 121
trip.AddStopTime(stop29, stop_time='17:43:00') # Abou Nawess - 53
trip.AddStopTime(stop28, stop_time='17:45:00') # Elmadina - 149
trip.AddStopTime(stop27, stop_time='17:47:00') # Holiday - 134
trip.AddStopTime(stop26, stop_time='17:48:00') # Dalli - 83
trip.AddStopTime(stop25, stop_time='17:51:00') # Eljazira - 199
trip.AddStopTime(stop24, stop_time='17:53:00') # Ulysse - 147
trip.AddStopTime(stop23, stop_time='17:54:00') # Athene - 72
trip.AddStopTime(stop22, stop_time='17:57:00') # Ras ettabia - 197
trip.AddStopTime(stop21, stop_time='17:58:00') # Elmagtaa - 58
trip.AddStopTime(stop20, stop_time='18:00:00') # Croisement Guisen - 101
trip.AddStopTime(stop19, stop_time='18:04:00') # Arouay - 245
trip.AddStopTime(stop18, stop_time='18:07:00') # Sidi Ismail - 162
trip.AddStopTime(stop17, stop_time='18:09:00') # Fatou2 - 125
trip.AddStopTime(stop16, stop_time='18:14:00') # Lobirette - 309
trip.AddStopTime(stop15, stop_time='18:17:00') # Sidi Zayed - 203
trip.AddStopTime(stop14, stop_time='18:19:00') # Elwilayia - 90
trip.AddStopTime(stop10, stop_time='18:25:00') # Houmet Souk - 384


trip = route.AddTrip(schedule, headsign="Houmet Souk vers Tanit")
trip.AddStopTime(stop10, stop_time='18:15:00') # Houmet Souk - 0
trip.AddStopTime(stop14, stop_time='18:21:00') # Elwilayia - 349
trip.AddStopTime(stop15, stop_time='18:23:00') # Sidi Zayed - 102
trip.AddStopTime(stop16, stop_time='18:24:00') # Lobirette - 84
trip.AddStopTime(stop17, stop_time='18:25:00') # Fatou2 - 49
trip.AddStopTime(stop18, stop_time='18:28:00') # Sidi Ismail - 209
trip.AddStopTime(stop19, stop_time='18:31:00') # Arouay - 202
trip.AddStopTime(stop20, stop_time='18:33:00') # Croisement Guisen - 91
trip.AddStopTime(stop21, stop_time='18:35:00') # Elmagtaa - 108
trip.AddStopTime(stop22, stop_time='18:38:00') # Ras ettabia - 155
trip.AddStopTime(stop23, stop_time='18:41:00') # Athene - 156
trip.AddStopTime(stop24, stop_time='18:44:00') # Ulysse - 178
trip.AddStopTime(stop25, stop_time='18:46:00') # Eljazira - 139
trip.AddStopTime(stop26, stop_time='18:48:00') # Dalli - 121
trip.AddStopTime(stop27, stop_time='18:49:00') # Holiday - 79
trip.AddStopTime(stop28, stop_time='18:52:00') # Elmadina - 166
trip.AddStopTime(stop29, stop_time='18:54:00') # Abou Nawess - 140
trip.AddStopTime(stop30, stop_time='18:55:00') # Palm Beach - 53
trip.AddStopTime(stop31, stop_time='18:58:00') # Toumana - 151
trip.AddStopTime(stop32, stop_time='18:59:00') # Yasmina - 39
trip.AddStopTime(stop33, stop_time='19:02:00') # Dar Midoun - 163
trip.AddStopTime(stop34, stop_time='19:03:00') # R.D.V - 63
trip.AddStopTime(stop35, stop_time='19:05:00') # Hasdrubal - 134
trip.AddStopTime(stop36, stop_time='19:06:00') # Minenx - 81
trip.AddStopTime(stop37, stop_time='19:07:00') # Elhana - 87
trip.AddStopTime(stop38, stop_time='19:09:00') # Plazza - 109
trip.AddStopTime(stop39, stop_time='19:12:00') # Golf - 166
trip.AddStopTime(stop40, stop_time='19:13:00') # Yadis - 53
trip.AddStopTime(stop41, stop_time='19:14:00') # Elmahari - 68
trip.AddStopTime(stop42, stop_time='19:17:00') # Elmanara - 157
trip.AddStopTime(stop43, stop_time='19:18:00') # Abou Nawess Golf - 87
trip.AddStopTime(stop44, stop_time='19:20:00') # Dar Jeba - 149
trip.AddStopTime(stop45, stop_time='19:22:00') # Phare Ennadhour - 149
trip.AddStopTime(stop74, stop_time='19:28:00') # Tanit - 364

trip = route.AddTrip(schedule, headsign="Tanit vers Houmet Souk")
trip.AddStopTime(stop74, stop_time='18:00:00') # Tanit - 0
trip.AddStopTime(stop45, stop_time='18:05:00') # Phare Ennadhour - 298
trip.AddStopTime(stop44, stop_time='18:06:00') # Dar Jeba - 78
trip.AddStopTime(stop43, stop_time='18:06:00') # Abou Nawess Golf - 26
trip.AddStopTime(stop42, stop_time='18:06:00') # Elmanara - 26
trip.AddStopTime(stop41, stop_time='18:06:00') # Elmahari - 20
trip.AddStopTime(stop40, stop_time='18:07:00') # Yadis - 44
trip.AddStopTime(stop39, stop_time='18:09:00') # Golf - 112
trip.AddStopTime(stop38, stop_time='18:09:00') # Plazza - 22
trip.AddStopTime(stop37, stop_time='18:10:00') # Elhana - 32
trip.AddStopTime(stop36, stop_time='18:11:00') # Minenx - 47
trip.AddStopTime(stop35, stop_time='18:12:00') # Hasdrubal - 36
trip.AddStopTime(stop34, stop_time='18:14:00') # R.D.V - 106
trip.AddStopTime(stop33, stop_time='18:15:00') # Dar Midoun - 88
trip.AddStopTime(stop32, stop_time='18:18:00') # Yasmina - 158
trip.AddStopTime(stop31, stop_time='18:20:00') # Toumana - 107
trip.AddStopTime(stop30, stop_time='18:22:00') # Palm Beach - 121
trip.AddStopTime(stop29, stop_time='18:23:00') # Abou Nawess - 53
trip.AddStopTime(stop28, stop_time='18:25:00') # Elmadina - 149
trip.AddStopTime(stop27, stop_time='18:27:00') # Holiday - 134
trip.AddStopTime(stop26, stop_time='18:28:00') # Dalli - 83
trip.AddStopTime(stop25, stop_time='18:31:00') # Eljazira - 199
trip.AddStopTime(stop24, stop_time='18:33:00') # Ulysse - 147
trip.AddStopTime(stop23, stop_time='18:34:00') # Athene - 72
trip.AddStopTime(stop22, stop_time='18:37:00') # Ras ettabia - 197
trip.AddStopTime(stop21, stop_time='18:38:00') # Elmagtaa - 58
trip.AddStopTime(stop20, stop_time='18:40:00') # Croisement Guisen - 101
trip.AddStopTime(stop19, stop_time='18:44:00') # Arouay - 245
trip.AddStopTime(stop18, stop_time='18:47:00') # Sidi Ismail - 162
trip.AddStopTime(stop17, stop_time='18:49:00') # Fatou2 - 125
trip.AddStopTime(stop16, stop_time='18:54:00') # Lobirette - 309
trip.AddStopTime(stop15, stop_time='18:57:00') # Sidi Zayed - 203
trip.AddStopTime(stop14, stop_time='18:59:00') # Elwilayia - 90
trip.AddStopTime(stop10, stop_time='19:05:00') # Houmet Souk - 384


trip = route.AddTrip(schedule, headsign="Houmet Souk vers Tanit")
trip.AddStopTime(stop10, stop_time='20:45:00') # Houmet Souk - 0
trip.AddStopTime(stop14, stop_time='20:51:00') # Elwilayia - 349
trip.AddStopTime(stop15, stop_time='20:53:00') # Sidi Zayed - 102
trip.AddStopTime(stop16, stop_time='20:54:00') # Lobirette - 84
trip.AddStopTime(stop17, stop_time='20:55:00') # Fatou2 - 49
trip.AddStopTime(stop18, stop_time='20:58:00') # Sidi Ismail - 209
trip.AddStopTime(stop19, stop_time='21:01:00') # Arouay - 202
trip.AddStopTime(stop20, stop_time='21:03:00') # Croisement Guisen - 91
trip.AddStopTime(stop21, stop_time='21:05:00') # Elmagtaa - 108
trip.AddStopTime(stop22, stop_time='21:08:00') # Ras ettabia - 155
trip.AddStopTime(stop23, stop_time='21:11:00') # Athene - 156
trip.AddStopTime(stop24, stop_time='21:14:00') # Ulysse - 178
trip.AddStopTime(stop25, stop_time='21:16:00') # Eljazira - 139
trip.AddStopTime(stop26, stop_time='21:18:00') # Dalli - 121
trip.AddStopTime(stop27, stop_time='21:19:00') # Holiday - 79
trip.AddStopTime(stop28, stop_time='21:22:00') # Elmadina - 166
trip.AddStopTime(stop29, stop_time='21:24:00') # Abou Nawess - 140
trip.AddStopTime(stop30, stop_time='21:25:00') # Palm Beach - 53
trip.AddStopTime(stop31, stop_time='21:28:00') # Toumana - 151
trip.AddStopTime(stop32, stop_time='21:29:00') # Yasmina - 39
trip.AddStopTime(stop33, stop_time='21:32:00') # Dar Midoun - 163
trip.AddStopTime(stop34, stop_time='21:33:00') # R.D.V - 63
trip.AddStopTime(stop35, stop_time='21:35:00') # Hasdrubal - 134
trip.AddStopTime(stop36, stop_time='21:36:00') # Minenx - 81
trip.AddStopTime(stop37, stop_time='21:37:00') # Elhana - 87
trip.AddStopTime(stop38, stop_time='21:39:00') # Plazza - 109
trip.AddStopTime(stop39, stop_time='21:42:00') # Golf - 166
trip.AddStopTime(stop40, stop_time='21:43:00') # Yadis - 53
trip.AddStopTime(stop41, stop_time='21:44:00') # Elmahari - 68
trip.AddStopTime(stop42, stop_time='21:47:00') # Elmanara - 157
trip.AddStopTime(stop43, stop_time='21:48:00') # Abou Nawess Golf - 87
trip.AddStopTime(stop44, stop_time='21:50:00') # Dar Jeba - 149
trip.AddStopTime(stop45, stop_time='21:52:00') # Phare Ennadhour - 149
trip.AddStopTime(stop74, stop_time='21:58:00') # Tanit - 364

trip = route.AddTrip(schedule, headsign="Tanit vers Houmet Souk")
trip.AddStopTime(stop74, stop_time='19:00:00') # Tanit - 0
trip.AddStopTime(stop45, stop_time='19:05:00') # Phare Ennadhour - 298
trip.AddStopTime(stop44, stop_time='19:06:00') # Dar Jeba - 78
trip.AddStopTime(stop43, stop_time='19:06:00') # Abou Nawess Golf - 26
trip.AddStopTime(stop42, stop_time='19:06:00') # Elmanara - 26
trip.AddStopTime(stop41, stop_time='19:06:00') # Elmahari - 20
trip.AddStopTime(stop40, stop_time='19:07:00') # Yadis - 44
trip.AddStopTime(stop39, stop_time='19:09:00') # Golf - 112
trip.AddStopTime(stop38, stop_time='19:09:00') # Plazza - 22
trip.AddStopTime(stop37, stop_time='19:10:00') # Elhana - 32
trip.AddStopTime(stop36, stop_time='19:11:00') # Minenx - 47
trip.AddStopTime(stop35, stop_time='19:12:00') # Hasdrubal - 36
trip.AddStopTime(stop34, stop_time='19:14:00') # R.D.V - 106
trip.AddStopTime(stop33, stop_time='19:15:00') # Dar Midoun - 88
trip.AddStopTime(stop32, stop_time='19:18:00') # Yasmina - 158
trip.AddStopTime(stop31, stop_time='19:20:00') # Toumana - 107
trip.AddStopTime(stop30, stop_time='19:22:00') # Palm Beach - 121
trip.AddStopTime(stop29, stop_time='19:23:00') # Abou Nawess - 53
trip.AddStopTime(stop28, stop_time='19:25:00') # Elmadina - 149
trip.AddStopTime(stop27, stop_time='19:27:00') # Holiday - 134
trip.AddStopTime(stop26, stop_time='19:28:00') # Dalli - 83
trip.AddStopTime(stop25, stop_time='19:31:00') # Eljazira - 199
trip.AddStopTime(stop24, stop_time='19:33:00') # Ulysse - 147
trip.AddStopTime(stop23, stop_time='19:34:00') # Athene - 72
trip.AddStopTime(stop22, stop_time='19:37:00') # Ras ettabia - 197
trip.AddStopTime(stop21, stop_time='19:38:00') # Elmagtaa - 58
trip.AddStopTime(stop20, stop_time='19:40:00') # Croisement Guisen - 101
trip.AddStopTime(stop19, stop_time='19:44:00') # Arouay - 245
trip.AddStopTime(stop18, stop_time='19:47:00') # Sidi Ismail - 162
trip.AddStopTime(stop17, stop_time='19:49:00') # Fatou2 - 125
trip.AddStopTime(stop16, stop_time='19:54:00') # Lobirette - 309
trip.AddStopTime(stop15, stop_time='19:57:00') # Sidi Zayed - 203
trip.AddStopTime(stop14, stop_time='19:59:00') # Elwilayia - 90
trip.AddStopTime(stop10, stop_time='20:05:00') # Houmet Souk - 384


trip = route.AddTrip(schedule, headsign="Tanit vers Houmet Souk")
trip.AddStopTime(stop74, stop_time='21:50:00') # Tanit - 0
trip.AddStopTime(stop45, stop_time='21:55:00') # Phare Ennadhour - 298
trip.AddStopTime(stop44, stop_time='21:56:00') # Dar Jeba - 78
trip.AddStopTime(stop43, stop_time='21:56:00') # Abou Nawess Golf - 26
trip.AddStopTime(stop42, stop_time='21:56:00') # Elmanara - 26
trip.AddStopTime(stop41, stop_time='21:56:00') # Elmahari - 20
trip.AddStopTime(stop40, stop_time='21:57:00') # Yadis - 44
trip.AddStopTime(stop39, stop_time='21:59:00') # Golf - 112
trip.AddStopTime(stop38, stop_time='21:59:00') # Plazza - 22
trip.AddStopTime(stop37, stop_time='22:00:00') # Elhana - 32
trip.AddStopTime(stop36, stop_time='22:01:00') # Minenx - 47
trip.AddStopTime(stop35, stop_time='22:02:00') # Hasdrubal - 36
trip.AddStopTime(stop34, stop_time='22:04:00') # R.D.V - 106
trip.AddStopTime(stop33, stop_time='22:05:00') # Dar Midoun - 88
trip.AddStopTime(stop32, stop_time='22:08:00') # Yasmina - 158
trip.AddStopTime(stop31, stop_time='22:10:00') # Toumana - 107
trip.AddStopTime(stop30, stop_time='22:12:00') # Palm Beach - 121
trip.AddStopTime(stop29, stop_time='22:13:00') # Abou Nawess - 53
trip.AddStopTime(stop28, stop_time='22:15:00') # Elmadina - 149
trip.AddStopTime(stop27, stop_time='22:17:00') # Holiday - 134
trip.AddStopTime(stop26, stop_time='22:18:00') # Dalli - 83
trip.AddStopTime(stop25, stop_time='22:21:00') # Eljazira - 199
trip.AddStopTime(stop24, stop_time='22:23:00') # Ulysse - 147
trip.AddStopTime(stop23, stop_time='22:24:00') # Athene - 72
trip.AddStopTime(stop22, stop_time='22:27:00') # Ras ettabia - 197
trip.AddStopTime(stop21, stop_time='22:28:00') # Elmagtaa - 58
trip.AddStopTime(stop20, stop_time='22:30:00') # Croisement Guisen - 101
trip.AddStopTime(stop19, stop_time='22:34:00') # Arouay - 245
trip.AddStopTime(stop18, stop_time='22:37:00') # Sidi Ismail - 162
trip.AddStopTime(stop17, stop_time='22:39:00') # Fatou2 - 125
trip.AddStopTime(stop16, stop_time='22:44:00') # Lobirette - 309
trip.AddStopTime(stop15, stop_time='22:47:00') # Sidi Zayed - 203
trip.AddStopTime(stop14, stop_time='22:49:00') # Elwilayia - 90
trip.AddStopTime(stop10, stop_time='22:55:00') # Houmet Souk - 384



route = schedule.AddRoute(short_name="SU412", long_name="Houmet Souk, Ajim",
                          route_type="Bus")

trip = route.AddTrip(schedule, headsign="Houmet Souk vers Ajim")
trip.AddStopTime(stop10, stop_time='07:00:00') # Houmet Souk - 0
trip.AddStopTime(stop190, stop_time='07:04:00') # Hnini - 211
trip.AddStopTime(stop191, stop_time='07:05:00') # Elbarkaoui - 67
trip.AddStopTime(stop192, stop_time='07:05:00') # Elhachen - 22
trip.AddStopTime(stop193, stop_time='07:06:00') # Sidi Hassen - 30
trip.AddStopTime(stop194, stop_time='07:06:00') # Saoud - 21
trip.AddStopTime(stop195, stop_time='07:06:00') # Jaballah 1 - 27
trip.AddStopTime(stop196, stop_time='07:07:00') # Jaballah 2 - 33
trip.AddStopTime(stop197, stop_time='07:08:00') # Slim - 52
trip.AddStopTime(stop198, stop_time='07:09:00') # Bazim - 89
trip.AddStopTime(stop202, stop_time='07:22:00') # Elkharouba - 759
trip.AddStopTime(stop203, stop_time='07:23:00') # Fekih Amor - 82
trip.AddStopTime(stop204, stop_time='07:24:00') # Bousmael - 58
trip.AddStopTime(stop205, stop_time='07:25:00') # Fekih Massaoud - 74
trip.AddStopTime(stop206, stop_time='07:25:00') # Bel Haj Yahyia - 23
trip.AddStopTime(stop207, stop_time='07:25:00') # 26-26 - 28
trip.AddStopTime(stop208, stop_time='07:26:00') # Mezran - 62
trip.AddStopTime(stop209, stop_time='07:27:00') # Ben Hafsia - 51
trip.AddStopTime(stop210, stop_time='07:28:00') # Eddaoula - 72
trip.AddStopTime(stop189, stop_time='07:29:00') # Elgroo - 75
trip.AddStopTime(stop102, stop_time='07:39:00') # Ajim - 610

trip = route.AddTrip(schedule, headsign="Ajim vers Houmet Souk")
trip.AddStopTime(stop102, stop_time='06:30:00') # Ajim - 0
trip.AddStopTime(stop189, stop_time='06:41:00') # Elgroo - 630
trip.AddStopTime(stop210, stop_time='06:43:00') # Eddaoula - 104
trip.AddStopTime(stop209, stop_time='06:44:00') # Ben Hafsia - 68
trip.AddStopTime(stop208, stop_time='06:45:00') # Mezran - 50
trip.AddStopTime(stop207, stop_time='06:46:00') # 26-26 - 61
trip.AddStopTime(stop206, stop_time='06:46:00') # Bel Haj Yahyia - 28
trip.AddStopTime(stop205, stop_time='06:46:00') # Fekih Massaoud - 22
trip.AddStopTime(stop204, stop_time='06:47:00') # Bousmael - 46
trip.AddStopTime(stop203, stop_time='06:48:00') # Fekih Amor - 61
trip.AddStopTime(stop202, stop_time='06:49:00') # Elkharouba - 71
trip.AddStopTime(stop198, stop_time='07:02:00') # Bazim - 787
trip.AddStopTime(stop197, stop_time='07:03:00') # Slim - 83
trip.AddStopTime(stop196, stop_time='07:04:00') # Jaballah 2 - 86
trip.AddStopTime(stop195, stop_time='07:05:00') # Jaballah 1 - 36
trip.AddStopTime(stop194, stop_time='07:06:00') # Saoud - 32
trip.AddStopTime(stop193, stop_time='07:06:00') # Sidi Hassen - 25
trip.AddStopTime(stop192, stop_time='07:07:00') # Elhachen - 31
trip.AddStopTime(stop191, stop_time='07:07:00') # Elbarkaoui - 22
trip.AddStopTime(stop190, stop_time='07:08:00') # Hnini - 63
trip.AddStopTime(stop10, stop_time='07:11:00') # Houmet Souk - 197

trip = route.AddTrip(schedule, headsign="Houmet Souk vers Ajim")
trip.AddStopTime(stop10, stop_time='08:00:00') # Houmet Souk - 0
trip.AddStopTime(stop190, stop_time='08:04:00') # Hnini - 211
trip.AddStopTime(stop191, stop_time='08:05:00') # Elbarkaoui - 67
trip.AddStopTime(stop192, stop_time='08:05:00') # Elhachen - 22
trip.AddStopTime(stop193, stop_time='08:06:00') # Sidi Hassen - 30
trip.AddStopTime(stop194, stop_time='08:06:00') # Saoud - 21
trip.AddStopTime(stop195, stop_time='08:06:00') # Jaballah 1 - 27
trip.AddStopTime(stop196, stop_time='08:07:00') # Jaballah 2 - 33
trip.AddStopTime(stop197, stop_time='08:08:00') # Slim - 52
trip.AddStopTime(stop198, stop_time='08:09:00') # Bazim - 89
trip.AddStopTime(stop202, stop_time='08:22:00') # Elkharouba - 759
trip.AddStopTime(stop203, stop_time='08:23:00') # Fekih Amor - 82
trip.AddStopTime(stop204, stop_time='08:24:00') # Bousmael - 58
trip.AddStopTime(stop205, stop_time='08:25:00') # Fekih Massaoud - 74
trip.AddStopTime(stop206, stop_time='08:25:00') # Bel Haj Yahyia - 23
trip.AddStopTime(stop207, stop_time='08:25:00') # 26-26 - 28
trip.AddStopTime(stop208, stop_time='08:26:00') # Mezran - 62
trip.AddStopTime(stop209, stop_time='08:27:00') # Ben Hafsia - 51
trip.AddStopTime(stop210, stop_time='08:28:00') # Eddaoula - 72
trip.AddStopTime(stop189, stop_time='08:29:00') # Elgroo - 75
trip.AddStopTime(stop102, stop_time='08:39:00') # Ajim - 610

trip = route.AddTrip(schedule, headsign="Ajim vers Houmet Souk")
trip.AddStopTime(stop102, stop_time='07:25:00') # Ajim - 0
trip.AddStopTime(stop189, stop_time='07:36:00') # Elgroo - 630
trip.AddStopTime(stop210, stop_time='07:38:00') # Eddaoula - 104
trip.AddStopTime(stop209, stop_time='07:39:00') # Ben Hafsia - 68
trip.AddStopTime(stop208, stop_time='07:40:00') # Mezran - 50
trip.AddStopTime(stop207, stop_time='07:41:00') # 26-26 - 61
trip.AddStopTime(stop206, stop_time='07:41:00') # Bel Haj Yahyia - 28
trip.AddStopTime(stop205, stop_time='07:41:00') # Fekih Massaoud - 22
trip.AddStopTime(stop204, stop_time='07:42:00') # Bousmael - 46
trip.AddStopTime(stop203, stop_time='07:43:00') # Fekih Amor - 61
trip.AddStopTime(stop202, stop_time='07:44:00') # Elkharouba - 71
trip.AddStopTime(stop198, stop_time='07:57:00') # Bazim - 787
trip.AddStopTime(stop197, stop_time='07:58:00') # Slim - 83
trip.AddStopTime(stop196, stop_time='07:59:00') # Jaballah 2 - 86
trip.AddStopTime(stop195, stop_time='08:00:00') # Jaballah 1 - 36
trip.AddStopTime(stop194, stop_time='08:01:00') # Saoud - 32
trip.AddStopTime(stop193, stop_time='08:01:00') # Sidi Hassen - 25
trip.AddStopTime(stop192, stop_time='08:02:00') # Elhachen - 31
trip.AddStopTime(stop191, stop_time='08:02:00') # Elbarkaoui - 22
trip.AddStopTime(stop190, stop_time='08:03:00') # Hnini - 63
trip.AddStopTime(stop10, stop_time='08:06:00') # Houmet Souk - 197

trip = route.AddTrip(schedule, headsign="Houmet Souk vers Ajim")
trip.AddStopTime(stop10, stop_time='11:15:00') # Houmet Souk - 0
trip.AddStopTime(stop190, stop_time='11:19:00') # Hnini - 211
trip.AddStopTime(stop191, stop_time='11:20:00') # Elbarkaoui - 67
trip.AddStopTime(stop192, stop_time='11:20:00') # Elhachen - 22
trip.AddStopTime(stop193, stop_time='11:21:00') # Sidi Hassen - 30
trip.AddStopTime(stop194, stop_time='11:21:00') # Saoud - 21
trip.AddStopTime(stop195, stop_time='11:21:00') # Jaballah 1 - 27
trip.AddStopTime(stop196, stop_time='11:22:00') # Jaballah 2 - 33
trip.AddStopTime(stop197, stop_time='11:23:00') # Slim - 52
trip.AddStopTime(stop198, stop_time='11:24:00') # Bazim - 89
trip.AddStopTime(stop202, stop_time='11:37:00') # Elkharouba - 759
trip.AddStopTime(stop203, stop_time='11:38:00') # Fekih Amor - 82
trip.AddStopTime(stop204, stop_time='11:39:00') # Bousmael - 58
trip.AddStopTime(stop205, stop_time='11:40:00') # Fekih Massaoud - 74
trip.AddStopTime(stop206, stop_time='11:40:00') # Bel Haj Yahyia - 23
trip.AddStopTime(stop207, stop_time='11:40:00') # 26-26 - 28
trip.AddStopTime(stop208, stop_time='11:41:00') # Mezran - 62
trip.AddStopTime(stop209, stop_time='11:42:00') # Ben Hafsia - 51
trip.AddStopTime(stop210, stop_time='11:43:00') # Eddaoula - 72
trip.AddStopTime(stop189, stop_time='11:44:00') # Elgroo - 75
trip.AddStopTime(stop102, stop_time='11:54:00') # Ajim - 610

trip = route.AddTrip(schedule, headsign="Ajim vers Houmet Souk")
trip.AddStopTime(stop102, stop_time='08:00:00') # Ajim - 0
trip.AddStopTime(stop189, stop_time='08:11:00') # Elgroo - 630
trip.AddStopTime(stop210, stop_time='08:13:00') # Eddaoula - 104
trip.AddStopTime(stop209, stop_time='08:14:00') # Ben Hafsia - 68
trip.AddStopTime(stop208, stop_time='08:15:00') # Mezran - 50
trip.AddStopTime(stop207, stop_time='08:16:00') # 26-26 - 61
trip.AddStopTime(stop206, stop_time='08:16:00') # Bel Haj Yahyia - 28
trip.AddStopTime(stop205, stop_time='08:16:00') # Fekih Massaoud - 22
trip.AddStopTime(stop204, stop_time='08:17:00') # Bousmael - 46
trip.AddStopTime(stop203, stop_time='08:18:00') # Fekih Amor - 61
trip.AddStopTime(stop202, stop_time='08:19:00') # Elkharouba - 71
trip.AddStopTime(stop198, stop_time='08:32:00') # Bazim - 787
trip.AddStopTime(stop197, stop_time='08:33:00') # Slim - 83
trip.AddStopTime(stop196, stop_time='08:34:00') # Jaballah 2 - 86
trip.AddStopTime(stop195, stop_time='08:35:00') # Jaballah 1 - 36
trip.AddStopTime(stop194, stop_time='08:36:00') # Saoud - 32
trip.AddStopTime(stop193, stop_time='08:36:00') # Sidi Hassen - 25
trip.AddStopTime(stop192, stop_time='08:37:00') # Elhachen - 31
trip.AddStopTime(stop191, stop_time='08:37:00') # Elbarkaoui - 22
trip.AddStopTime(stop190, stop_time='08:38:00') # Hnini - 63
trip.AddStopTime(stop10, stop_time='08:41:00') # Houmet Souk - 197


trip = route.AddTrip(schedule, headsign="Houmet Souk vers Ajim")
trip.AddStopTime(stop10, stop_time='12:15:00') # Houmet Souk - 0
trip.AddStopTime(stop190, stop_time='12:19:00') # Hnini - 211
trip.AddStopTime(stop191, stop_time='12:20:00') # Elbarkaoui - 67
trip.AddStopTime(stop192, stop_time='12:20:00') # Elhachen - 22
trip.AddStopTime(stop193, stop_time='12:21:00') # Sidi Hassen - 30
trip.AddStopTime(stop194, stop_time='12:21:00') # Saoud - 21
trip.AddStopTime(stop195, stop_time='12:21:00') # Jaballah 1 - 27
trip.AddStopTime(stop196, stop_time='12:22:00') # Jaballah 2 - 33
trip.AddStopTime(stop197, stop_time='12:23:00') # Slim - 52
trip.AddStopTime(stop198, stop_time='12:24:00') # Bazim - 89
trip.AddStopTime(stop202, stop_time='12:37:00') # Elkharouba - 759
trip.AddStopTime(stop203, stop_time='12:38:00') # Fekih Amor - 82
trip.AddStopTime(stop204, stop_time='12:39:00') # Bousmael - 58
trip.AddStopTime(stop205, stop_time='12:40:00') # Fekih Massaoud - 74
trip.AddStopTime(stop206, stop_time='12:40:00') # Bel Haj Yahyia - 23
trip.AddStopTime(stop207, stop_time='12:40:00') # 26-26 - 28
trip.AddStopTime(stop208, stop_time='12:41:00') # Mezran - 62
trip.AddStopTime(stop209, stop_time='12:42:00') # Ben Hafsia - 51
trip.AddStopTime(stop210, stop_time='12:43:00') # Eddaoula - 72
trip.AddStopTime(stop189, stop_time='12:44:00') # Elgroo - 75
trip.AddStopTime(stop102, stop_time='12:54:00') # Ajim - 610

trip = route.AddTrip(schedule, headsign="Ajim vers Houmet Souk")
trip.AddStopTime(stop102, stop_time='09:00:00') # Ajim - 0
trip.AddStopTime(stop189, stop_time='09:11:00') # Elgroo - 630
trip.AddStopTime(stop210, stop_time='09:13:00') # Eddaoula - 104
trip.AddStopTime(stop209, stop_time='09:14:00') # Ben Hafsia - 68
trip.AddStopTime(stop208, stop_time='09:15:00') # Mezran - 50
trip.AddStopTime(stop207, stop_time='09:16:00') # 26-26 - 61
trip.AddStopTime(stop206, stop_time='09:16:00') # Bel Haj Yahyia - 28
trip.AddStopTime(stop205, stop_time='09:16:00') # Fekih Massaoud - 22
trip.AddStopTime(stop204, stop_time='09:17:00') # Bousmael - 46
trip.AddStopTime(stop203, stop_time='09:18:00') # Fekih Amor - 61
trip.AddStopTime(stop202, stop_time='09:19:00') # Elkharouba - 71
trip.AddStopTime(stop198, stop_time='09:32:00') # Bazim - 787
trip.AddStopTime(stop197, stop_time='09:33:00') # Slim - 83
trip.AddStopTime(stop196, stop_time='09:34:00') # Jaballah 2 - 86
trip.AddStopTime(stop195, stop_time='09:35:00') # Jaballah 1 - 36
trip.AddStopTime(stop194, stop_time='09:36:00') # Saoud - 32
trip.AddStopTime(stop193, stop_time='09:36:00') # Sidi Hassen - 25
trip.AddStopTime(stop192, stop_time='09:37:00') # Elhachen - 31
trip.AddStopTime(stop191, stop_time='09:37:00') # Elbarkaoui - 22
trip.AddStopTime(stop190, stop_time='09:38:00') # Hnini - 63
trip.AddStopTime(stop10, stop_time='09:41:00') # Houmet Souk - 197



trip = route.AddTrip(schedule, headsign="Houmet Souk vers Ajim")
trip.AddStopTime(stop10, stop_time='13:15:00') # Houmet Souk - 0
trip.AddStopTime(stop190, stop_time='13:19:00') # Hnini - 211
trip.AddStopTime(stop191, stop_time='13:20:00') # Elbarkaoui - 67
trip.AddStopTime(stop192, stop_time='13:20:00') # Elhachen - 22
trip.AddStopTime(stop193, stop_time='13:21:00') # Sidi Hassen - 30
trip.AddStopTime(stop194, stop_time='13:21:00') # Saoud - 21
trip.AddStopTime(stop195, stop_time='13:21:00') # Jaballah 1 - 27
trip.AddStopTime(stop196, stop_time='13:22:00') # Jaballah 2 - 33
trip.AddStopTime(stop197, stop_time='13:23:00') # Slim - 52
trip.AddStopTime(stop198, stop_time='13:24:00') # Bazim - 89
trip.AddStopTime(stop202, stop_time='13:37:00') # Elkharouba - 759
trip.AddStopTime(stop203, stop_time='13:38:00') # Fekih Amor - 82
trip.AddStopTime(stop204, stop_time='13:39:00') # Bousmael - 58
trip.AddStopTime(stop205, stop_time='13:40:00') # Fekih Massaoud - 74
trip.AddStopTime(stop206, stop_time='13:40:00') # Bel Haj Yahyia - 23
trip.AddStopTime(stop207, stop_time='13:40:00') # 26-26 - 28
trip.AddStopTime(stop208, stop_time='13:41:00') # Mezran - 62
trip.AddStopTime(stop209, stop_time='13:42:00') # Ben Hafsia - 51
trip.AddStopTime(stop210, stop_time='13:43:00') # Eddaoula - 72
trip.AddStopTime(stop189, stop_time='13:44:00') # Elgroo - 75
trip.AddStopTime(stop102, stop_time='13:54:00') # Ajim - 610

trip = route.AddTrip(schedule, headsign="Ajim vers Houmet Souk")
trip.AddStopTime(stop102, stop_time='12:00:00') # Ajim - 0
trip.AddStopTime(stop189, stop_time='12:11:00') # Elgroo - 630
trip.AddStopTime(stop210, stop_time='12:13:00') # Eddaoula - 104
trip.AddStopTime(stop209, stop_time='12:14:00') # Ben Hafsia - 68
trip.AddStopTime(stop208, stop_time='12:15:00') # Mezran - 50
trip.AddStopTime(stop207, stop_time='12:16:00') # 26-26 - 61
trip.AddStopTime(stop206, stop_time='12:16:00') # Bel Haj Yahyia - 28
trip.AddStopTime(stop205, stop_time='12:16:00') # Fekih Massaoud - 22
trip.AddStopTime(stop204, stop_time='12:17:00') # Bousmael - 46
trip.AddStopTime(stop203, stop_time='12:18:00') # Fekih Amor - 61
trip.AddStopTime(stop202, stop_time='12:19:00') # Elkharouba - 71
trip.AddStopTime(stop198, stop_time='12:32:00') # Bazim - 787
trip.AddStopTime(stop197, stop_time='12:33:00') # Slim - 83
trip.AddStopTime(stop196, stop_time='12:34:00') # Jaballah 2 - 86
trip.AddStopTime(stop195, stop_time='12:35:00') # Jaballah 1 - 36
trip.AddStopTime(stop194, stop_time='12:36:00') # Saoud - 32
trip.AddStopTime(stop193, stop_time='12:36:00') # Sidi Hassen - 25
trip.AddStopTime(stop192, stop_time='12:37:00') # Elhachen - 31
trip.AddStopTime(stop191, stop_time='12:37:00') # Elbarkaoui - 22
trip.AddStopTime(stop190, stop_time='12:38:00') # Hnini - 63
trip.AddStopTime(stop10, stop_time='12:41:00') # Houmet Souk - 197


trip = route.AddTrip(schedule, headsign="Houmet Souk vers Ajim")
trip.AddStopTime(stop10, stop_time='16:15:00') # Houmet Souk - 0
trip.AddStopTime(stop190, stop_time='16:19:00') # Hnini - 211
trip.AddStopTime(stop191, stop_time='16:20:00') # Elbarkaoui - 67
trip.AddStopTime(stop192, stop_time='16:20:00') # Elhachen - 22
trip.AddStopTime(stop193, stop_time='16:21:00') # Sidi Hassen - 30
trip.AddStopTime(stop194, stop_time='16:21:00') # Saoud - 21
trip.AddStopTime(stop195, stop_time='16:21:00') # Jaballah 1 - 27
trip.AddStopTime(stop196, stop_time='16:22:00') # Jaballah 2 - 33
trip.AddStopTime(stop197, stop_time='16:23:00') # Slim - 52
trip.AddStopTime(stop198, stop_time='16:24:00') # Bazim - 89
trip.AddStopTime(stop202, stop_time='16:37:00') # Elkharouba - 759
trip.AddStopTime(stop203, stop_time='16:38:00') # Fekih Amor - 82
trip.AddStopTime(stop204, stop_time='16:39:00') # Bousmael - 58
trip.AddStopTime(stop205, stop_time='16:40:00') # Fekih Massaoud - 74
trip.AddStopTime(stop206, stop_time='16:40:00') # Bel Haj Yahyia - 23
trip.AddStopTime(stop207, stop_time='16:40:00') # 26-26 - 28
trip.AddStopTime(stop208, stop_time='16:41:00') # Mezran - 62
trip.AddStopTime(stop209, stop_time='16:42:00') # Ben Hafsia - 51
trip.AddStopTime(stop210, stop_time='16:43:00') # Eddaoula - 72
trip.AddStopTime(stop189, stop_time='16:44:00') # Elgroo - 75
trip.AddStopTime(stop102, stop_time='16:54:00') # Ajim - 610

trip = route.AddTrip(schedule, headsign="Ajim vers Houmet Souk")
trip.AddStopTime(stop102, stop_time='13:15:00') # Ajim - 0
trip.AddStopTime(stop189, stop_time='13:26:00') # Elgroo - 630
trip.AddStopTime(stop210, stop_time='13:28:00') # Eddaoula - 104
trip.AddStopTime(stop209, stop_time='13:29:00') # Ben Hafsia - 68
trip.AddStopTime(stop208, stop_time='13:30:00') # Mezran - 50
trip.AddStopTime(stop207, stop_time='13:31:00') # 26-26 - 61
trip.AddStopTime(stop206, stop_time='13:31:00') # Bel Haj Yahyia - 28
trip.AddStopTime(stop205, stop_time='13:31:00') # Fekih Massaoud - 22
trip.AddStopTime(stop204, stop_time='13:32:00') # Bousmael - 46
trip.AddStopTime(stop203, stop_time='13:33:00') # Fekih Amor - 61
trip.AddStopTime(stop202, stop_time='13:34:00') # Elkharouba - 71
trip.AddStopTime(stop198, stop_time='13:47:00') # Bazim - 787
trip.AddStopTime(stop197, stop_time='13:48:00') # Slim - 83
trip.AddStopTime(stop196, stop_time='13:49:00') # Jaballah 2 - 86
trip.AddStopTime(stop195, stop_time='13:50:00') # Jaballah 1 - 36
trip.AddStopTime(stop194, stop_time='13:51:00') # Saoud - 32
trip.AddStopTime(stop193, stop_time='13:51:00') # Sidi Hassen - 25
trip.AddStopTime(stop192, stop_time='13:52:00') # Elhachen - 31
trip.AddStopTime(stop191, stop_time='13:52:00') # Elbarkaoui - 22
trip.AddStopTime(stop190, stop_time='13:53:00') # Hnini - 63
trip.AddStopTime(stop10, stop_time='13:56:00') # Houmet Souk - 197

trip = route.AddTrip(schedule, headsign="Houmet Souk vers Ajim")
trip.AddStopTime(stop10, stop_time='17:15:00') # Houmet Souk - 0
trip.AddStopTime(stop190, stop_time='17:19:00') # Hnini - 211
trip.AddStopTime(stop191, stop_time='17:20:00') # Elbarkaoui - 67
trip.AddStopTime(stop192, stop_time='17:20:00') # Elhachen - 22
trip.AddStopTime(stop193, stop_time='17:21:00') # Sidi Hassen - 30
trip.AddStopTime(stop194, stop_time='17:21:00') # Saoud - 21
trip.AddStopTime(stop195, stop_time='17:21:00') # Jaballah 1 - 27
trip.AddStopTime(stop196, stop_time='17:22:00') # Jaballah 2 - 33
trip.AddStopTime(stop197, stop_time='17:23:00') # Slim - 52
trip.AddStopTime(stop198, stop_time='17:24:00') # Bazim - 89
trip.AddStopTime(stop202, stop_time='17:37:00') # Elkharouba - 759
trip.AddStopTime(stop203, stop_time='17:38:00') # Fekih Amor - 82
trip.AddStopTime(stop204, stop_time='17:39:00') # Bousmael - 58
trip.AddStopTime(stop205, stop_time='17:40:00') # Fekih Massaoud - 74
trip.AddStopTime(stop206, stop_time='17:40:00') # Bel Haj Yahyia - 23
trip.AddStopTime(stop207, stop_time='17:40:00') # 26-26 - 28
trip.AddStopTime(stop208, stop_time='17:41:00') # Mezran - 62
trip.AddStopTime(stop209, stop_time='17:42:00') # Ben Hafsia - 51
trip.AddStopTime(stop210, stop_time='17:43:00') # Eddaoula - 72
trip.AddStopTime(stop189, stop_time='17:44:00') # Elgroo - 75
trip.AddStopTime(stop102, stop_time='17:54:00') # Ajim - 610

trip = route.AddTrip(schedule, headsign="Ajim vers Houmet Souk")
trip.AddStopTime(stop102, stop_time='14:00:00') # Ajim - 0
trip.AddStopTime(stop189, stop_time='14:11:00') # Elgroo - 630
trip.AddStopTime(stop210, stop_time='14:13:00') # Eddaoula - 104
trip.AddStopTime(stop209, stop_time='14:14:00') # Ben Hafsia - 68
trip.AddStopTime(stop208, stop_time='14:15:00') # Mezran - 50
trip.AddStopTime(stop207, stop_time='14:16:00') # 26-26 - 61
trip.AddStopTime(stop206, stop_time='14:16:00') # Bel Haj Yahyia - 28
trip.AddStopTime(stop205, stop_time='14:16:00') # Fekih Massaoud - 22
trip.AddStopTime(stop204, stop_time='14:17:00') # Bousmael - 46
trip.AddStopTime(stop203, stop_time='14:18:00') # Fekih Amor - 61
trip.AddStopTime(stop202, stop_time='14:19:00') # Elkharouba - 71
trip.AddStopTime(stop198, stop_time='14:32:00') # Bazim - 787
trip.AddStopTime(stop197, stop_time='14:33:00') # Slim - 83
trip.AddStopTime(stop196, stop_time='14:34:00') # Jaballah 2 - 86
trip.AddStopTime(stop195, stop_time='14:35:00') # Jaballah 1 - 36
trip.AddStopTime(stop194, stop_time='14:36:00') # Saoud - 32
trip.AddStopTime(stop193, stop_time='14:36:00') # Sidi Hassen - 25
trip.AddStopTime(stop192, stop_time='14:37:00') # Elhachen - 31
trip.AddStopTime(stop191, stop_time='14:37:00') # Elbarkaoui - 22
trip.AddStopTime(stop190, stop_time='14:38:00') # Hnini - 63
trip.AddStopTime(stop10, stop_time='14:41:00') # Houmet Souk - 197

trip = route.AddTrip(schedule, headsign="Houmet Souk vers Ajim")
trip.AddStopTime(stop10, stop_time='18:15:00') # Houmet Souk - 0
trip.AddStopTime(stop190, stop_time='18:19:00') # Hnini - 211
trip.AddStopTime(stop191, stop_time='18:20:00') # Elbarkaoui - 67
trip.AddStopTime(stop192, stop_time='18:20:00') # Elhachen - 22
trip.AddStopTime(stop193, stop_time='18:21:00') # Sidi Hassen - 30
trip.AddStopTime(stop194, stop_time='18:21:00') # Saoud - 21
trip.AddStopTime(stop195, stop_time='18:21:00') # Jaballah 1 - 27
trip.AddStopTime(stop196, stop_time='18:22:00') # Jaballah 2 - 33
trip.AddStopTime(stop197, stop_time='18:23:00') # Slim - 52
trip.AddStopTime(stop198, stop_time='18:24:00') # Bazim - 89
trip.AddStopTime(stop202, stop_time='18:37:00') # Elkharouba - 759
trip.AddStopTime(stop203, stop_time='18:38:00') # Fekih Amor - 82
trip.AddStopTime(stop204, stop_time='18:39:00') # Bousmael - 58
trip.AddStopTime(stop205, stop_time='18:40:00') # Fekih Massaoud - 74
trip.AddStopTime(stop206, stop_time='18:40:00') # Bel Haj Yahyia - 23
trip.AddStopTime(stop207, stop_time='18:40:00') # 26-26 - 28
trip.AddStopTime(stop208, stop_time='18:41:00') # Mezran - 62
trip.AddStopTime(stop209, stop_time='18:42:00') # Ben Hafsia - 51
trip.AddStopTime(stop210, stop_time='18:43:00') # Eddaoula - 72
trip.AddStopTime(stop189, stop_time='18:44:00') # Elgroo - 75
trip.AddStopTime(stop102, stop_time='18:54:00') # Ajim - 610

trip = route.AddTrip(schedule, headsign="Ajim vers Houmet Souk")
trip.AddStopTime(stop102, stop_time='17:00:00') # Ajim - 0
trip.AddStopTime(stop189, stop_time='17:11:00') # Elgroo - 630
trip.AddStopTime(stop210, stop_time='17:13:00') # Eddaoula - 104
trip.AddStopTime(stop209, stop_time='17:14:00') # Ben Hafsia - 68
trip.AddStopTime(stop208, stop_time='17:15:00') # Mezran - 50
trip.AddStopTime(stop207, stop_time='17:16:00') # 26-26 - 61
trip.AddStopTime(stop206, stop_time='17:16:00') # Bel Haj Yahyia - 28
trip.AddStopTime(stop205, stop_time='17:16:00') # Fekih Massaoud - 22
trip.AddStopTime(stop204, stop_time='17:17:00') # Bousmael - 46
trip.AddStopTime(stop203, stop_time='17:18:00') # Fekih Amor - 61
trip.AddStopTime(stop202, stop_time='17:19:00') # Elkharouba - 71
trip.AddStopTime(stop198, stop_time='17:32:00') # Bazim - 787
trip.AddStopTime(stop197, stop_time='17:33:00') # Slim - 83
trip.AddStopTime(stop196, stop_time='17:34:00') # Jaballah 2 - 86
trip.AddStopTime(stop195, stop_time='17:35:00') # Jaballah 1 - 36
trip.AddStopTime(stop194, stop_time='17:36:00') # Saoud - 32
trip.AddStopTime(stop193, stop_time='17:36:00') # Sidi Hassen - 25
trip.AddStopTime(stop192, stop_time='17:37:00') # Elhachen - 31
trip.AddStopTime(stop191, stop_time='17:37:00') # Elbarkaoui - 22
trip.AddStopTime(stop190, stop_time='17:38:00') # Hnini - 63
trip.AddStopTime(stop10, stop_time='17:41:00') # Houmet Souk - 197


trip = route.AddTrip(schedule, headsign="Ajim vers Houmet Souk")
trip.AddStopTime(stop102, stop_time='17:45:00') # Ajim - 0
trip.AddStopTime(stop189, stop_time='17:56:00') # Elgroo - 630
trip.AddStopTime(stop210, stop_time='17:58:00') # Eddaoula - 104
trip.AddStopTime(stop209, stop_time='17:59:00') # Ben Hafsia - 68
trip.AddStopTime(stop208, stop_time='18:00:00') # Mezran - 50
trip.AddStopTime(stop207, stop_time='18:01:00') # 26-26 - 61
trip.AddStopTime(stop206, stop_time='18:01:00') # Bel Haj Yahyia - 28
trip.AddStopTime(stop205, stop_time='18:01:00') # Fekih Massaoud - 22
trip.AddStopTime(stop204, stop_time='18:02:00') # Bousmael - 46
trip.AddStopTime(stop203, stop_time='18:03:00') # Fekih Amor - 61
trip.AddStopTime(stop202, stop_time='18:04:00') # Elkharouba - 71
trip.AddStopTime(stop198, stop_time='18:17:00') # Bazim - 787
trip.AddStopTime(stop197, stop_time='18:18:00') # Slim - 83
trip.AddStopTime(stop196, stop_time='18:19:00') # Jaballah 2 - 86
trip.AddStopTime(stop195, stop_time='18:20:00') # Jaballah 1 - 36
trip.AddStopTime(stop194, stop_time='18:21:00') # Saoud - 32
trip.AddStopTime(stop193, stop_time='18:21:00') # Sidi Hassen - 25
trip.AddStopTime(stop192, stop_time='18:22:00') # Elhachen - 31
trip.AddStopTime(stop191, stop_time='18:22:00') # Elbarkaoui - 22
trip.AddStopTime(stop190, stop_time='18:23:00') # Hnini - 63
trip.AddStopTime(stop10, stop_time='18:26:00') # Houmet Souk - 197



route = schedule.AddRoute(short_name="SU413", long_name="Houmet Souk, Bni Maaguel, Midoun",
                          route_type="Bus")
trip = route.AddTrip(schedule, headsign="Houmet Souk vers Bni Maaguel")
trip.AddStopTime(stop10, stop_time='08:00:00') # Houmet Souk - 0
trip.AddStopTime(stop11, stop_time='08:03:00') # L'hôpital - 208
trip.AddStopTime(stop148, stop_time='08:05:00') # Souk Ejoumla - 140
trip.AddStopTime(stop149, stop_time='08:06:00') # Houassa - 63
trip.AddStopTime(stop150, stop_time='08:06:00') # Echahben - 28
trip.AddStopTime(stop151, stop_time='08:10:00') # Elassas - 240
trip.AddStopTime(stop152, stop_time='08:14:00') # Hanout Salah - 251
trip.AddStopTime(stop153, stop_time='08:19:00') # Elmajen - 283
trip.AddStopTime(stop154, stop_time='08:24:00') # Croisement Ibn Sina - 276
trip.AddStopTime(stop172, stop_time='08:26:00') # Sadguyène 1 - 117
trip.AddStopTime(stop173, stop_time='08:29:00') # Mosquet Boulaymane - 199
trip.AddStopTime(stop49, stop_time='08:31:00') # Mosquet Elgayed 1 - 137
trip.AddStopTime(stop48, stop_time='08:32:00') # Fadhloun - 34
trip.AddStopTime(stop46, stop_time='08:37:00') # Midoun - 308
trip.AddStopTime(stop47, stop_time='08:39:00') # Hadher bach - 146
trip.AddStopTime(stop51, stop_time='08:42:00') # Mahboubine - 169
trip.AddStopTime(stop132, stop_time='08:45:00') # Elkoucha - 152
trip.AddStopTime(stop131, stop_time='08:46:00') # Latrech - 51
trip.AddStopTime(stop130, stop_time='08:48:00') # Bedouin - 115
trip.AddStopTime(stop129, stop_time='08:49:00') # Elhajjam - 73
trip.AddStopTime(stop128, stop_time='08:51:00') # Bir Bouaziz - 104
trip.AddStopTime(stop127, stop_time='08:54:00') # La poste - 187
trip.AddStopTime(stop126, stop_time='08:55:00') # Bni Maaguel - 83

trip = route.AddTrip(schedule, headsign="Bni Maaguel vers Houmet Souk")
trip.AddStopTime(stop126, stop_time='07:00:00') # Bni Maaguel - 0
trip.AddStopTime(stop127, stop_time='07:01:00') # La poste - 88
trip.AddStopTime(stop128, stop_time='07:04:00') # Bir Bouaziz - 186
trip.AddStopTime(stop129, stop_time='07:06:00') # Elhajjam - 103
trip.AddStopTime(stop130, stop_time='07:07:00') # Bedouin - 80
trip.AddStopTime(stop131, stop_time='07:09:00') # Latrech - 143
trip.AddStopTime(stop132, stop_time='07:10:00') # Elkoucha - 51
trip.AddStopTime(stop51, stop_time='07:12:00') # Mahboubine - 143
trip.AddStopTime(stop47, stop_time='07:15:00') # Hadher bach - 168
trip.AddStopTime(stop46, stop_time='07:16:00') # Midoun - 85
trip.AddStopTime(stop48, stop_time='07:21:00') # Fadhloun - 321
trip.AddStopTime(stop49, stop_time='07:22:00') # Mosquet Elgayed 1 - 34
trip.AddStopTime(stop173, stop_time='07:28:00') # Mosquet Boulaymane - 347
trip.AddStopTime(stop172, stop_time='07:34:00') # Sadguyène 1 - 349
trip.AddStopTime(stop154, stop_time='07:35:00') # Croisement Ibn Sina - 80
trip.AddStopTime(stop153, stop_time='07:37:00') # Elmajen - 106
trip.AddStopTime(stop152, stop_time='07:39:00') # Hanout Salah - 110
trip.AddStopTime(stop151, stop_time='07:41:00') # Elassas - 123
trip.AddStopTime(stop150, stop_time='07:44:00') # Echahben - 206
trip.AddStopTime(stop149, stop_time='07:47:00') # Houassa - 167
trip.AddStopTime(stop148, stop_time='07:48:00') # Souk Ejoumla - 67
trip.AddStopTime(stop11, stop_time='07:51:00') # L'hôpital - 151
trip.AddStopTime(stop10, stop_time='07:55:00') # Houmet Souk - 218


trip = route.AddTrip(schedule, headsign="Houmet Souk vers Bni Maaguel")
trip.AddStopTime(stop10, stop_time='10:30:00') # Houmet Souk - 0
trip.AddStopTime(stop11, stop_time='10:33:00') # L'hôpital - 208
trip.AddStopTime(stop148, stop_time='10:35:00') # Souk Ejoumla - 140
trip.AddStopTime(stop149, stop_time='10:36:00') # Houassa - 63
trip.AddStopTime(stop150, stop_time='10:36:00') # Echahben - 28
trip.AddStopTime(stop151, stop_time='10:40:00') # Elassas - 240
trip.AddStopTime(stop152, stop_time='10:44:00') # Hanout Salah - 251
trip.AddStopTime(stop153, stop_time='10:49:00') # Elmajen - 283
trip.AddStopTime(stop154, stop_time='10:54:00') # Croisement Ibn Sina - 276
trip.AddStopTime(stop172, stop_time='10:56:00') # Sadguyène 1 - 117
trip.AddStopTime(stop173, stop_time='10:59:00') # Mosquet Boulaymane - 199
trip.AddStopTime(stop49, stop_time='11:01:00') # Mosquet Elgayed 1 - 137
trip.AddStopTime(stop48, stop_time='11:02:00') # Fadhloun - 34
trip.AddStopTime(stop46, stop_time='11:07:00') # Midoun - 308
trip.AddStopTime(stop47, stop_time='11:09:00') # Hadher bach - 146
trip.AddStopTime(stop51, stop_time='11:12:00') # Mahboubine - 169
trip.AddStopTime(stop132, stop_time='11:15:00') # Elkoucha - 152
trip.AddStopTime(stop131, stop_time='11:16:00') # Latrech - 51
trip.AddStopTime(stop130, stop_time='11:18:00') # Bedouin - 115
trip.AddStopTime(stop129, stop_time='11:19:00') # Elhajjam - 73
trip.AddStopTime(stop128, stop_time='11:21:00') # Bir Bouaziz - 104
trip.AddStopTime(stop127, stop_time='11:24:00') # La poste - 187
trip.AddStopTime(stop126, stop_time='11:25:00') # Bni Maaguel - 83

trip = route.AddTrip(schedule, headsign="Bni Maaguel vers Houmet Souk")
trip.AddStopTime(stop126, stop_time='08:15:00') # Bni Maaguel - 0
trip.AddStopTime(stop127, stop_time='08:16:00') # La poste - 88
trip.AddStopTime(stop128, stop_time='08:19:00') # Bir Bouaziz - 186
trip.AddStopTime(stop129, stop_time='08:21:00') # Elhajjam - 103
trip.AddStopTime(stop130, stop_time='08:22:00') # Bedouin - 80
trip.AddStopTime(stop131, stop_time='08:24:00') # Latrech - 143
trip.AddStopTime(stop132, stop_time='08:25:00') # Elkoucha - 51
trip.AddStopTime(stop51, stop_time='08:27:00') # Mahboubine - 143
trip.AddStopTime(stop47, stop_time='08:30:00') # Hadher bach - 168
trip.AddStopTime(stop46, stop_time='08:31:00') # Midoun - 85
trip.AddStopTime(stop48, stop_time='08:36:00') # Fadhloun - 321
trip.AddStopTime(stop49, stop_time='08:37:00') # Mosquet Elgayed 1 - 34
trip.AddStopTime(stop173, stop_time='08:43:00') # Mosquet Boulaymane - 347
trip.AddStopTime(stop172, stop_time='08:49:00') # Sadguyène 1 - 349
trip.AddStopTime(stop154, stop_time='08:50:00') # Croisement Ibn Sina - 80
trip.AddStopTime(stop153, stop_time='08:52:00') # Elmajen - 106
trip.AddStopTime(stop152, stop_time='08:54:00') # Hanout Salah - 110
trip.AddStopTime(stop151, stop_time='08:56:00') # Elassas - 123
trip.AddStopTime(stop150, stop_time='08:59:00') # Echahben - 206
trip.AddStopTime(stop149, stop_time='09:02:00') # Houassa - 167
trip.AddStopTime(stop148, stop_time='09:03:00') # Souk Ejoumla - 67
trip.AddStopTime(stop11, stop_time='09:06:00') # L'hôpital - 151
trip.AddStopTime(stop10, stop_time='09:10:00') # Houmet Souk - 218

trip = route.AddTrip(schedule, headsign="Houmet Souk vers Bni Maaguel")
trip.AddStopTime(stop10, stop_time='12:15:00') # Houmet Souk - 0
trip.AddStopTime(stop11, stop_time='12:18:00') # L'hôpital - 208
trip.AddStopTime(stop148, stop_time='12:20:00') # Souk Ejoumla - 140
trip.AddStopTime(stop149, stop_time='12:21:00') # Houassa - 63
trip.AddStopTime(stop150, stop_time='12:21:00') # Echahben - 28
trip.AddStopTime(stop151, stop_time='12:25:00') # Elassas - 240
trip.AddStopTime(stop152, stop_time='12:29:00') # Hanout Salah - 251
trip.AddStopTime(stop153, stop_time='12:34:00') # Elmajen - 283
trip.AddStopTime(stop154, stop_time='12:39:00') # Croisement Ibn Sina - 276
trip.AddStopTime(stop172, stop_time='12:41:00') # Sadguyène 1 - 117
trip.AddStopTime(stop173, stop_time='12:44:00') # Mosquet Boulaymane - 199
trip.AddStopTime(stop49, stop_time='12:46:00') # Mosquet Elgayed 1 - 137
trip.AddStopTime(stop48, stop_time='12:47:00') # Fadhloun - 34
trip.AddStopTime(stop46, stop_time='12:52:00') # Midoun - 308
trip.AddStopTime(stop47, stop_time='12:54:00') # Hadher bach - 146
trip.AddStopTime(stop51, stop_time='12:57:00') # Mahboubine - 169
trip.AddStopTime(stop132, stop_time='13:00:00') # Elkoucha - 152
trip.AddStopTime(stop131, stop_time='13:01:00') # Latrech - 51
trip.AddStopTime(stop130, stop_time='13:03:00') # Bedouin - 115
trip.AddStopTime(stop129, stop_time='13:04:00') # Elhajjam - 73
trip.AddStopTime(stop128, stop_time='13:06:00') # Bir Bouaziz - 104
trip.AddStopTime(stop127, stop_time='13:09:00') # La poste - 187
trip.AddStopTime(stop126, stop_time='13:10:00') # Bni Maaguel - 83

trip = route.AddTrip(schedule, headsign="Bni Maaguel vers Houmet Souk")
trip.AddStopTime(stop126, stop_time='09:30:00') # Bni Maaguel - 0
trip.AddStopTime(stop127, stop_time='09:31:00') # La poste - 88
trip.AddStopTime(stop128, stop_time='09:34:00') # Bir Bouaziz - 186
trip.AddStopTime(stop129, stop_time='09:36:00') # Elhajjam - 103
trip.AddStopTime(stop130, stop_time='09:37:00') # Bedouin - 80
trip.AddStopTime(stop131, stop_time='09:39:00') # Latrech - 143
trip.AddStopTime(stop132, stop_time='09:40:00') # Elkoucha - 51
trip.AddStopTime(stop51, stop_time='09:42:00') # Mahboubine - 143
trip.AddStopTime(stop47, stop_time='09:45:00') # Hadher bach - 168
trip.AddStopTime(stop46, stop_time='09:46:00') # Midoun - 85
trip.AddStopTime(stop48, stop_time='09:51:00') # Fadhloun - 321
trip.AddStopTime(stop49, stop_time='09:52:00') # Mosquet Elgayed 1 - 34
trip.AddStopTime(stop173, stop_time='09:58:00') # Mosquet Boulaymane - 347
trip.AddStopTime(stop172, stop_time='10:04:00') # Sadguyène 1 - 349
trip.AddStopTime(stop154, stop_time='10:05:00') # Croisement Ibn Sina - 80
trip.AddStopTime(stop153, stop_time='10:07:00') # Elmajen - 106
trip.AddStopTime(stop152, stop_time='10:09:00') # Hanout Salah - 110
trip.AddStopTime(stop151, stop_time='10:11:00') # Elassas - 123
trip.AddStopTime(stop150, stop_time='10:14:00') # Echahben - 206
trip.AddStopTime(stop149, stop_time='10:17:00') # Houassa - 167
trip.AddStopTime(stop148, stop_time='10:18:00') # Souk Ejoumla - 67
trip.AddStopTime(stop11, stop_time='10:21:00') # L'hôpital - 151
trip.AddStopTime(stop10, stop_time='10:25:00') # Houmet Souk - 218

trip = route.AddTrip(schedule, headsign="Houmet Souk vers Bni Maaguel")
trip.AddStopTime(stop10, stop_time='16:15:00') # Houmet Souk - 0
trip.AddStopTime(stop11, stop_time='16:18:00') # L'hôpital - 208
trip.AddStopTime(stop148, stop_time='16:20:00') # Souk Ejoumla - 140
trip.AddStopTime(stop149, stop_time='16:21:00') # Houassa - 63
trip.AddStopTime(stop150, stop_time='16:21:00') # Echahben - 28
trip.AddStopTime(stop151, stop_time='16:25:00') # Elassas - 240
trip.AddStopTime(stop152, stop_time='16:29:00') # Hanout Salah - 251
trip.AddStopTime(stop153, stop_time='16:34:00') # Elmajen - 283
trip.AddStopTime(stop154, stop_time='16:39:00') # Croisement Ibn Sina - 276
trip.AddStopTime(stop172, stop_time='16:41:00') # Sadguyène 1 - 117
trip.AddStopTime(stop173, stop_time='16:44:00') # Mosquet Boulaymane - 199
trip.AddStopTime(stop49, stop_time='16:46:00') # Mosquet Elgayed 1 - 137
trip.AddStopTime(stop48, stop_time='16:47:00') # Fadhloun - 34
trip.AddStopTime(stop46, stop_time='16:52:00') # Midoun - 308
trip.AddStopTime(stop47, stop_time='16:54:00') # Hadher bach - 146
trip.AddStopTime(stop51, stop_time='16:57:00') # Mahboubine - 169
trip.AddStopTime(stop132, stop_time='17:00:00') # Elkoucha - 152
trip.AddStopTime(stop131, stop_time='17:01:00') # Latrech - 51
trip.AddStopTime(stop130, stop_time='17:03:00') # Bedouin - 115
trip.AddStopTime(stop129, stop_time='17:04:00') # Elhajjam - 73
trip.AddStopTime(stop128, stop_time='17:06:00') # Bir Bouaziz - 104
trip.AddStopTime(stop127, stop_time='17:09:00') # La poste - 187
trip.AddStopTime(stop126, stop_time='17:10:00') # Bni Maaguel - 83

trip = route.AddTrip(schedule, headsign="Bni Maaguel vers Houmet Souk")
trip.AddStopTime(stop126, stop_time='11:30:00') # Bni Maaguel - 0
trip.AddStopTime(stop127, stop_time='11:31:00') # La poste - 88
trip.AddStopTime(stop128, stop_time='11:34:00') # Bir Bouaziz - 186
trip.AddStopTime(stop129, stop_time='11:36:00') # Elhajjam - 103
trip.AddStopTime(stop130, stop_time='11:37:00') # Bedouin - 80
trip.AddStopTime(stop131, stop_time='11:39:00') # Latrech - 143
trip.AddStopTime(stop132, stop_time='11:40:00') # Elkoucha - 51
trip.AddStopTime(stop51, stop_time='11:42:00') # Mahboubine - 143
trip.AddStopTime(stop47, stop_time='11:45:00') # Hadher bach - 168
trip.AddStopTime(stop46, stop_time='11:46:00') # Midoun - 85
trip.AddStopTime(stop48, stop_time='11:51:00') # Fadhloun - 321
trip.AddStopTime(stop49, stop_time='11:52:00') # Mosquet Elgayed 1 - 34
trip.AddStopTime(stop173, stop_time='11:58:00') # Mosquet Boulaymane - 347
trip.AddStopTime(stop172, stop_time='12:04:00') # Sadguyène 1 - 349
trip.AddStopTime(stop154, stop_time='12:05:00') # Croisement Ibn Sina - 80
trip.AddStopTime(stop153, stop_time='12:07:00') # Elmajen - 106
trip.AddStopTime(stop152, stop_time='12:09:00') # Hanout Salah - 110
trip.AddStopTime(stop151, stop_time='12:11:00') # Elassas - 123
trip.AddStopTime(stop150, stop_time='12:14:00') # Echahben - 206
trip.AddStopTime(stop149, stop_time='12:17:00') # Houassa - 167
trip.AddStopTime(stop148, stop_time='12:18:00') # Souk Ejoumla - 67
trip.AddStopTime(stop11, stop_time='12:21:00') # L'hôpital - 151
trip.AddStopTime(stop10, stop_time='12:25:00') # Houmet Souk - 218

trip = route.AddTrip(schedule, headsign="Houmet Souk vers Bni Maaguel")
trip.AddStopTime(stop10, stop_time='18:15:00') # Houmet Souk - 0
trip.AddStopTime(stop11, stop_time='18:18:00') # L'hôpital - 208
trip.AddStopTime(stop148, stop_time='18:20:00') # Souk Ejoumla - 140
trip.AddStopTime(stop149, stop_time='18:21:00') # Houassa - 63
trip.AddStopTime(stop150, stop_time='18:21:00') # Echahben - 28
trip.AddStopTime(stop151, stop_time='18:25:00') # Elassas - 240
trip.AddStopTime(stop152, stop_time='18:29:00') # Hanout Salah - 251
trip.AddStopTime(stop153, stop_time='18:34:00') # Elmajen - 283
trip.AddStopTime(stop154, stop_time='18:39:00') # Croisement Ibn Sina - 276
trip.AddStopTime(stop172, stop_time='18:41:00') # Sadguyène 1 - 117
trip.AddStopTime(stop173, stop_time='18:44:00') # Mosquet Boulaymane - 199
trip.AddStopTime(stop49, stop_time='18:46:00') # Mosquet Elgayed 1 - 137
trip.AddStopTime(stop48, stop_time='18:47:00') # Fadhloun - 34
trip.AddStopTime(stop46, stop_time='18:52:00') # Midoun - 308
trip.AddStopTime(stop47, stop_time='18:54:00') # Hadher bach - 146
trip.AddStopTime(stop51, stop_time='18:57:00') # Mahboubine - 169
trip.AddStopTime(stop132, stop_time='19:00:00') # Elkoucha - 152
trip.AddStopTime(stop131, stop_time='19:01:00') # Latrech - 51
trip.AddStopTime(stop130, stop_time='19:03:00') # Bedouin - 115
trip.AddStopTime(stop129, stop_time='19:04:00') # Elhajjam - 73
trip.AddStopTime(stop128, stop_time='19:06:00') # Bir Bouaziz - 104
trip.AddStopTime(stop127, stop_time='19:09:00') # La poste - 187
trip.AddStopTime(stop126, stop_time='19:10:00') # Bni Maaguel - 83

trip = route.AddTrip(schedule, headsign="Bni Maaguel vers Houmet Souk")
trip.AddStopTime(stop126, stop_time='14:00:00') # Bni Maaguel - 0
trip.AddStopTime(stop127, stop_time='14:01:00') # La poste - 88
trip.AddStopTime(stop128, stop_time='14:04:00') # Bir Bouaziz - 186
trip.AddStopTime(stop129, stop_time='14:06:00') # Elhajjam - 103
trip.AddStopTime(stop130, stop_time='14:07:00') # Bedouin - 80
trip.AddStopTime(stop131, stop_time='14:09:00') # Latrech - 143
trip.AddStopTime(stop132, stop_time='14:10:00') # Elkoucha - 51
trip.AddStopTime(stop51, stop_time='14:12:00') # Mahboubine - 143
trip.AddStopTime(stop47, stop_time='14:15:00') # Hadher bach - 168
trip.AddStopTime(stop46, stop_time='14:16:00') # Midoun - 85
trip.AddStopTime(stop48, stop_time='14:21:00') # Fadhloun - 321
trip.AddStopTime(stop49, stop_time='14:22:00') # Mosquet Elgayed 1 - 34
trip.AddStopTime(stop173, stop_time='14:28:00') # Mosquet Boulaymane - 347
trip.AddStopTime(stop172, stop_time='14:34:00') # Sadguyène 1 - 349
trip.AddStopTime(stop154, stop_time='14:35:00') # Croisement Ibn Sina - 80
trip.AddStopTime(stop153, stop_time='14:37:00') # Elmajen - 106
trip.AddStopTime(stop152, stop_time='14:39:00') # Hanout Salah - 110
trip.AddStopTime(stop151, stop_time='14:41:00') # Elassas - 123
trip.AddStopTime(stop150, stop_time='14:44:00') # Echahben - 206
trip.AddStopTime(stop149, stop_time='14:47:00') # Houassa - 167
trip.AddStopTime(stop148, stop_time='14:48:00') # Souk Ejoumla - 67
trip.AddStopTime(stop11, stop_time='14:51:00') # L'hôpital - 151
trip.AddStopTime(stop10, stop_time='14:55:00') # Houmet Souk - 218


trip = route.AddTrip(schedule, headsign="Bni Maaguel vers Houmet Souk")
trip.AddStopTime(stop126, stop_time='17:30:00') # Bni Maaguel - 0
trip.AddStopTime(stop127, stop_time='17:31:00') # La poste - 88
trip.AddStopTime(stop128, stop_time='17:34:00') # Bir Bouaziz - 186
trip.AddStopTime(stop129, stop_time='17:36:00') # Elhajjam - 103
trip.AddStopTime(stop130, stop_time='17:37:00') # Bedouin - 80
trip.AddStopTime(stop131, stop_time='17:39:00') # Latrech - 143
trip.AddStopTime(stop132, stop_time='17:40:00') # Elkoucha - 51
trip.AddStopTime(stop51, stop_time='17:42:00') # Mahboubine - 143
trip.AddStopTime(stop47, stop_time='17:45:00') # Hadher bach - 168
trip.AddStopTime(stop46, stop_time='17:46:00') # Midoun - 85
trip.AddStopTime(stop48, stop_time='17:51:00') # Fadhloun - 321
trip.AddStopTime(stop49, stop_time='17:52:00') # Mosquet Elgayed 1 - 34
trip.AddStopTime(stop173, stop_time='17:58:00') # Mosquet Boulaymane - 347
trip.AddStopTime(stop172, stop_time='18:04:00') # Sadguyène 1 - 349
trip.AddStopTime(stop154, stop_time='18:05:00') # Croisement Ibn Sina - 80
trip.AddStopTime(stop153, stop_time='18:07:00') # Elmajen - 106
trip.AddStopTime(stop152, stop_time='18:09:00') # Hanout Salah - 110
trip.AddStopTime(stop151, stop_time='18:11:00') # Elassas - 123
trip.AddStopTime(stop150, stop_time='18:14:00') # Echahben - 206
trip.AddStopTime(stop149, stop_time='18:17:00') # Houassa - 167
trip.AddStopTime(stop148, stop_time='18:18:00') # Souk Ejoumla - 67
trip.AddStopTime(stop11, stop_time='18:21:00') # L'hôpital - 151
trip.AddStopTime(stop10, stop_time='18:25:00') # Houmet Souk - 218


route = schedule.AddRoute(short_name="SU414", long_name="Erriadh, Gallala",route_type="Bus")


trip = route.AddTrip(schedule, headsign="Houmet Souk vers Gallala")
trip.AddStopTime(stop10, stop_time='06:00:00') # Houmet Souk - 0
trip.AddStopTime(stop221, stop_time='06:02:00') # Lycée Technique - 123
trip.AddStopTime(stop222, stop_time='06:03:00') # Errahma - 79
trip.AddStopTime(stop147, stop_time='06:05:00') # Essouani - 118
trip.AddStopTime(stop159, stop_time='06:06:00') # Omajen 3 - 83
trip.AddStopTime(stop160, stop_time='06:08:00') # Bir Ben Amor - 94
trip.AddStopTime(stop161, stop_time='06:09:00') # Allamet - 63
trip.AddStopTime(stop179, stop_time='06:12:00') # Erriadh - 151
trip.AddStopTime(stop178, stop_time='06:14:00') # Zenkri - 101
trip.AddStopTime(stop187, stop_time='06:15:00') # Eljenni - 43
trip.AddStopTime(stop188, stop_time='06:16:00') # Ezayat - 60
trip.AddStopTime(stop94, stop_time='06:17:00') # Ben Arbi - 36
trip.AddStopTime(stop93, stop_time='06:18:00') # Allamet Esrandi - 41
trip.AddStopTime(stop95, stop_time='06:19:00') # Ben Aissa - 80
trip.AddStopTime(stop146, stop_time='06:21:00') # Echaouchia - 101
trip.AddStopTime(stop145, stop_time='06:21:00') # Ezitouna - 29
trip.AddStopTime(stop144, stop_time='06:22:00') # Etlat - 50
trip.AddStopTime(stop109, stop_time='06:24:00') # Tilouin - 110
trip.AddStopTime(stop108, stop_time='06:26:00') # Gallala - 102

trip = route.AddTrip(schedule, headsign="Gallala vers Houmet Souk")
trip.AddStopTime(stop108, stop_time='06:30:00') # Gallala - 0
trip.AddStopTime(stop109, stop_time='06:31:00') # Tilouin - 83
trip.AddStopTime(stop144, stop_time='06:33:00') # Etlat - 108
trip.AddStopTime(stop145, stop_time='06:34:00') # Ezitouna - 55
trip.AddStopTime(stop146, stop_time='06:35:00') # Echaouchia - 32
trip.AddStopTime(stop95, stop_time='06:37:00') # Ben Aissa - 99
trip.AddStopTime(stop93, stop_time='06:38:00') # Allamet Esrandi - 79
trip.AddStopTime(stop94, stop_time='06:39:00') # Ben Arbi - 51
trip.AddStopTime(stop188, stop_time='06:40:00') # Ezayat - 36
trip.AddStopTime(stop187, stop_time='06:41:00') # Eljenni - 55
trip.AddStopTime(stop178, stop_time='06:42:00') # Zenkri - 40
trip.AddStopTime(stop179, stop_time='06:44:00') # Erriadh - 98
trip.AddStopTime(stop161, stop_time='06:47:00') # Allamet - 158
trip.AddStopTime(stop160, stop_time='06:48:00') # Bir Ben Amor - 61
trip.AddStopTime(stop159, stop_time='06:50:00') # Omajen 3 - 92
trip.AddStopTime(stop147, stop_time='06:51:00') # Essouani - 83
trip.AddStopTime(stop222, stop_time='06:53:00') # Errahma - 118
trip.AddStopTime(stop221, stop_time='06:54:00') # Lycée Technique - 75
trip.AddStopTime(stop10, stop_time='06:57:00') # Houmet Souk - 159

trip = route.AddTrip(schedule, headsign="Houmet Souk vers Gallala")
trip.AddStopTime(stop10, stop_time='08:00:00') # Houmet Souk - 0
trip.AddStopTime(stop221, stop_time='08:02:00') # Lycée Technique - 123
trip.AddStopTime(stop222, stop_time='08:03:00') # Errahma - 79
trip.AddStopTime(stop147, stop_time='08:05:00') # Essouani - 118
trip.AddStopTime(stop159, stop_time='08:06:00') # Omajen 3 - 83
trip.AddStopTime(stop160, stop_time='08:08:00') # Bir Ben Amor - 94
trip.AddStopTime(stop161, stop_time='08:09:00') # Allamet - 63
trip.AddStopTime(stop179, stop_time='08:12:00') # Erriadh - 151
trip.AddStopTime(stop178, stop_time='08:14:00') # Zenkri - 101
trip.AddStopTime(stop187, stop_time='08:15:00') # Eljenni - 43
trip.AddStopTime(stop188, stop_time='08:16:00') # Ezayat - 60
trip.AddStopTime(stop94, stop_time='08:17:00') # Ben Arbi - 36
trip.AddStopTime(stop93, stop_time='08:18:00') # Allamet Esrandi - 41
trip.AddStopTime(stop95, stop_time='08:19:00') # Ben Aissa - 80
trip.AddStopTime(stop146, stop_time='08:21:00') # Echaouchia - 101
trip.AddStopTime(stop145, stop_time='08:21:00') # Ezitouna - 29
trip.AddStopTime(stop144, stop_time='08:22:00') # Etlat - 50
trip.AddStopTime(stop109, stop_time='08:24:00') # Tilouin - 110
trip.AddStopTime(stop108, stop_time='08:26:00') # Gallala - 102

trip = route.AddTrip(schedule, headsign="Gallala vers Houmet Souk")
trip.AddStopTime(stop108, stop_time='08:30:00') # Gallala - 0
trip.AddStopTime(stop109, stop_time='08:31:00') # Tilouin - 83
trip.AddStopTime(stop144, stop_time='08:33:00') # Etlat - 108
trip.AddStopTime(stop145, stop_time='08:34:00') # Ezitouna - 55
trip.AddStopTime(stop146, stop_time='08:35:00') # Echaouchia - 32
trip.AddStopTime(stop95, stop_time='08:37:00') # Ben Aissa - 99
trip.AddStopTime(stop93, stop_time='08:38:00') # Allamet Esrandi - 79
trip.AddStopTime(stop94, stop_time='08:39:00') # Ben Arbi - 51
trip.AddStopTime(stop188, stop_time='08:40:00') # Ezayat - 36
trip.AddStopTime(stop187, stop_time='08:41:00') # Eljenni - 55
trip.AddStopTime(stop178, stop_time='08:42:00') # Zenkri - 40
trip.AddStopTime(stop179, stop_time='08:44:00') # Erriadh - 98
trip.AddStopTime(stop161, stop_time='08:47:00') # Allamet - 158
trip.AddStopTime(stop160, stop_time='08:48:00') # Bir Ben Amor - 61
trip.AddStopTime(stop159, stop_time='08:50:00') # Omajen 3 - 92
trip.AddStopTime(stop147, stop_time='08:51:00') # Essouani - 83
trip.AddStopTime(stop222, stop_time='08:53:00') # Errahma - 118
trip.AddStopTime(stop221, stop_time='08:54:00') # Lycée Technique - 75
trip.AddStopTime(stop10, stop_time='08:57:00') # Houmet Souk - 159


trip = route.AddTrip(schedule, headsign="Houmet Souk vers Gallala")
trip.AddStopTime(stop10, stop_time='10:15:00') # Houmet Souk - 0
trip.AddStopTime(stop221, stop_time='10:17:00') # Lycée Technique - 123
trip.AddStopTime(stop222, stop_time='10:18:00') # Errahma - 79
trip.AddStopTime(stop147, stop_time='10:20:00') # Essouani - 118
trip.AddStopTime(stop159, stop_time='10:21:00') # Omajen 3 - 83
trip.AddStopTime(stop160, stop_time='10:23:00') # Bir Ben Amor - 94
trip.AddStopTime(stop161, stop_time='10:24:00') # Allamet - 63
trip.AddStopTime(stop179, stop_time='10:27:00') # Erriadh - 151
trip.AddStopTime(stop178, stop_time='10:29:00') # Zenkri - 101
trip.AddStopTime(stop187, stop_time='10:30:00') # Eljenni - 43
trip.AddStopTime(stop188, stop_time='10:31:00') # Ezayat - 60
trip.AddStopTime(stop94, stop_time='10:32:00') # Ben Arbi - 36
trip.AddStopTime(stop93, stop_time='10:33:00') # Allamet Esrandi - 41
trip.AddStopTime(stop95, stop_time='10:34:00') # Ben Aissa - 80
trip.AddStopTime(stop146, stop_time='10:36:00') # Echaouchia - 101
trip.AddStopTime(stop145, stop_time='10:36:00') # Ezitouna - 29
trip.AddStopTime(stop144, stop_time='10:37:00') # Etlat - 50
trip.AddStopTime(stop109, stop_time='10:39:00') # Tilouin - 110
trip.AddStopTime(stop108, stop_time='10:41:00') # Gallala - 102

trip = route.AddTrip(schedule, headsign="Gallala vers Houmet Souk")
trip.AddStopTime(stop108, stop_time='9:10:00') # Gallala - 0
trip.AddStopTime(stop109, stop_time='09:11:00') # Tilouin - 83
trip.AddStopTime(stop144, stop_time='09:13:00') # Etlat - 108
trip.AddStopTime(stop145, stop_time='09:14:00') # Ezitouna - 55
trip.AddStopTime(stop146, stop_time='09:15:00') # Echaouchia - 32
trip.AddStopTime(stop95, stop_time='09:17:00') # Ben Aissa - 99
trip.AddStopTime(stop93, stop_time='09:18:00') # Allamet Esrandi - 79
trip.AddStopTime(stop94, stop_time='09:19:00') # Ben Arbi - 51
trip.AddStopTime(stop188, stop_time='09:20:00') # Ezayat - 36
trip.AddStopTime(stop187, stop_time='09:21:00') # Eljenni - 55
trip.AddStopTime(stop178, stop_time='09:22:00') # Zenkri - 40
trip.AddStopTime(stop179, stop_time='09:24:00') # Erriadh - 98
trip.AddStopTime(stop161, stop_time='09:27:00') # Allamet - 158
trip.AddStopTime(stop160, stop_time='09:28:00') # Bir Ben Amor - 61
trip.AddStopTime(stop159, stop_time='09:30:00') # Omajen 3 - 92
trip.AddStopTime(stop147, stop_time='09:31:00') # Essouani - 83
trip.AddStopTime(stop222, stop_time='09:33:00') # Errahma - 118
trip.AddStopTime(stop221, stop_time='09:34:00') # Lycée Technique - 75
trip.AddStopTime(stop10, stop_time='09:37:00') # Houmet Souk - 159

trip = route.AddTrip(schedule, headsign="Houmet Souk vers Gallala")
trip.AddStopTime(stop10, stop_time='11:15:00') # Houmet Souk - 0
trip.AddStopTime(stop221, stop_time='11:17:00') # Lycée Technique - 123
trip.AddStopTime(stop222, stop_time='11:18:00') # Errahma - 79
trip.AddStopTime(stop147, stop_time='11:20:00') # Essouani - 118
trip.AddStopTime(stop159, stop_time='11:21:00') # Omajen 3 - 83
trip.AddStopTime(stop160, stop_time='11:23:00') # Bir Ben Amor - 94
trip.AddStopTime(stop161, stop_time='11:24:00') # Allamet - 63
trip.AddStopTime(stop179, stop_time='11:27:00') # Erriadh - 151
trip.AddStopTime(stop178, stop_time='11:29:00') # Zenkri - 101
trip.AddStopTime(stop187, stop_time='11:30:00') # Eljenni - 43
trip.AddStopTime(stop188, stop_time='11:31:00') # Ezayat - 60
trip.AddStopTime(stop94, stop_time='11:32:00') # Ben Arbi - 36
trip.AddStopTime(stop93, stop_time='11:33:00') # Allamet Esrandi - 41
trip.AddStopTime(stop95, stop_time='11:34:00') # Ben Aissa - 80
trip.AddStopTime(stop146, stop_time='11:36:00') # Echaouchia - 101
trip.AddStopTime(stop145, stop_time='11:36:00') # Ezitouna - 29
trip.AddStopTime(stop144, stop_time='11:37:00') # Etlat - 50
trip.AddStopTime(stop109, stop_time='11:39:00') # Tilouin - 110
trip.AddStopTime(stop108, stop_time='11:41:00') # Gallala - 102

trip = route.AddTrip(schedule, headsign="Gallala vers Houmet Souk")
trip.AddStopTime(stop108, stop_time='11:10:00') # Gallala - 0
trip.AddStopTime(stop109, stop_time='11:11:00') # Tilouin - 83
trip.AddStopTime(stop144, stop_time='11:13:00') # Etlat - 108
trip.AddStopTime(stop145, stop_time='11:14:00') # Ezitouna - 55
trip.AddStopTime(stop146, stop_time='11:15:00') # Echaouchia - 32
trip.AddStopTime(stop95, stop_time='11:17:00') # Ben Aissa - 99
trip.AddStopTime(stop93, stop_time='11:18:00') # Allamet Esrandi - 79
trip.AddStopTime(stop94, stop_time='11:19:00') # Ben Arbi - 51
trip.AddStopTime(stop188, stop_time='11:20:00') # Ezayat - 36
trip.AddStopTime(stop187, stop_time='11:21:00') # Eljenni - 55
trip.AddStopTime(stop178, stop_time='11:22:00') # Zenkri - 40
trip.AddStopTime(stop179, stop_time='11:24:00') # Erriadh - 98
trip.AddStopTime(stop161, stop_time='11:27:00') # Allamet - 158
trip.AddStopTime(stop160, stop_time='11:28:00') # Bir Ben Amor - 61
trip.AddStopTime(stop159, stop_time='11:30:00') # Omajen 3 - 92
trip.AddStopTime(stop147, stop_time='11:31:00') # Essouani - 83
trip.AddStopTime(stop222, stop_time='11:33:00') # Errahma - 118
trip.AddStopTime(stop221, stop_time='11:34:00') # Lycée Technique - 75
trip.AddStopTime(stop10, stop_time='11:37:00') # Houmet Souk - 159

trip = route.AddTrip(schedule, headsign="Houmet Souk vers Gallala")
trip.AddStopTime(stop10, stop_time='12:45:00') # Houmet Souk - 0
trip.AddStopTime(stop221, stop_time='12:47:00') # Lycée Technique - 123
trip.AddStopTime(stop222, stop_time='12:48:00') # Errahma - 79
trip.AddStopTime(stop147, stop_time='12:50:00') # Essouani - 118
trip.AddStopTime(stop159, stop_time='12:51:00') # Omajen 3 - 83
trip.AddStopTime(stop160, stop_time='12:53:00') # Bir Ben Amor - 94
trip.AddStopTime(stop161, stop_time='12:54:00') # Allamet - 63
trip.AddStopTime(stop179, stop_time='12:57:00') # Erriadh - 151
trip.AddStopTime(stop178, stop_time='12:59:00') # Zenkri - 101
trip.AddStopTime(stop187, stop_time='13:00:00') # Eljenni - 43
trip.AddStopTime(stop188, stop_time='13:01:00') # Ezayat - 60
trip.AddStopTime(stop94, stop_time='13:02:00') # Ben Arbi - 36
trip.AddStopTime(stop93, stop_time='13:03:00') # Allamet Esrandi - 41
trip.AddStopTime(stop95, stop_time='13:04:00') # Ben Aissa - 80
trip.AddStopTime(stop146, stop_time='13:06:00') # Echaouchia - 101
trip.AddStopTime(stop145, stop_time='13:06:00') # Ezitouna - 29
trip.AddStopTime(stop144, stop_time='13:07:00') # Etlat - 50
trip.AddStopTime(stop109, stop_time='13:09:00') # Tilouin - 110
trip.AddStopTime(stop108, stop_time='13:11:00') # Gallala - 102

trip = route.AddTrip(schedule, headsign="Gallala vers Houmet Souk")
trip.AddStopTime(stop108, stop_time='13:05:00') # Gallala - 0
trip.AddStopTime(stop109, stop_time='13:06:00') # Tilouin - 83
trip.AddStopTime(stop144, stop_time='13:08:00') # Etlat - 108
trip.AddStopTime(stop145, stop_time='13:09:00') # Ezitouna - 55
trip.AddStopTime(stop146, stop_time='13:10:00') # Echaouchia - 32
trip.AddStopTime(stop95, stop_time='13:12:00') # Ben Aissa - 99
trip.AddStopTime(stop93, stop_time='13:13:00') # Allamet Esrandi - 79
trip.AddStopTime(stop94, stop_time='13:14:00') # Ben Arbi - 51
trip.AddStopTime(stop188, stop_time='13:15:00') # Ezayat - 36
trip.AddStopTime(stop187, stop_time='13:16:00') # Eljenni - 55
trip.AddStopTime(stop178, stop_time='13:17:00') # Zenkri - 40
trip.AddStopTime(stop179, stop_time='13:19:00') # Erriadh - 98
trip.AddStopTime(stop161, stop_time='13:22:00') # Allamet - 158
trip.AddStopTime(stop160, stop_time='13:23:00') # Bir Ben Amor - 61
trip.AddStopTime(stop159, stop_time='13:25:00') # Omajen 3 - 92
trip.AddStopTime(stop147, stop_time='13:26:00') # Essouani - 83
trip.AddStopTime(stop222, stop_time='13:28:00') # Errahma - 118
trip.AddStopTime(stop221, stop_time='13:29:00') # Lycée Technique - 75
trip.AddStopTime(stop10, stop_time='13:32:00') # Houmet Souk - 159


trip = route.AddTrip(schedule, headsign="Houmet Souk vers Gallala")
trip.AddStopTime(stop10, stop_time='13:30:00') # Houmet Souk - 0
trip.AddStopTime(stop221, stop_time='13:32:00') # Lycée Technique - 123
trip.AddStopTime(stop222, stop_time='13:33:00') # Errahma - 79
trip.AddStopTime(stop147, stop_time='13:35:00') # Essouani - 118
trip.AddStopTime(stop159, stop_time='13:36:00') # Omajen 3 - 83
trip.AddStopTime(stop160, stop_time='13:38:00') # Bir Ben Amor - 94
trip.AddStopTime(stop161, stop_time='13:39:00') # Allamet - 63
trip.AddStopTime(stop179, stop_time='13:42:00') # Erriadh - 151
trip.AddStopTime(stop178, stop_time='13:44:00') # Zenkri - 101
trip.AddStopTime(stop187, stop_time='13:45:00') # Eljenni - 43
trip.AddStopTime(stop188, stop_time='13:46:00') # Ezayat - 60
trip.AddStopTime(stop94, stop_time='13:47:00') # Ben Arbi - 36
trip.AddStopTime(stop93, stop_time='13:48:00') # Allamet Esrandi - 41
trip.AddStopTime(stop95, stop_time='13:49:00') # Ben Aissa - 80
trip.AddStopTime(stop146, stop_time='13:51:00') # Echaouchia - 101
trip.AddStopTime(stop145, stop_time='13:51:00') # Ezitouna - 29
trip.AddStopTime(stop144, stop_time='13:52:00') # Etlat - 50
trip.AddStopTime(stop109, stop_time='13:54:00') # Tilouin - 110
trip.AddStopTime(stop108, stop_time='13:56:00') # Gallala - 102

trip = route.AddTrip(schedule, headsign="Gallala vers Houmet Souk")
trip.AddStopTime(stop108, stop_time='14:00:00') # Gallala - 0
trip.AddStopTime(stop109, stop_time='14:01:00') # Tilouin - 83
trip.AddStopTime(stop144, stop_time='14:03:00') # Etlat - 108
trip.AddStopTime(stop145, stop_time='14:04:00') # Ezitouna - 55
trip.AddStopTime(stop146, stop_time='14:05:00') # Echaouchia - 32
trip.AddStopTime(stop95, stop_time='14:07:00') # Ben Aissa - 99
trip.AddStopTime(stop93, stop_time='14:08:00') # Allamet Esrandi - 79
trip.AddStopTime(stop94, stop_time='14:09:00') # Ben Arbi - 51
trip.AddStopTime(stop188, stop_time='14:10:00') # Ezayat - 36
trip.AddStopTime(stop187, stop_time='14:11:00') # Eljenni - 55
trip.AddStopTime(stop178, stop_time='14:12:00') # Zenkri - 40
trip.AddStopTime(stop179, stop_time='14:14:00') # Erriadh - 98
trip.AddStopTime(stop161, stop_time='14:17:00') # Allamet - 158
trip.AddStopTime(stop160, stop_time='14:18:00') # Bir Ben Amor - 61
trip.AddStopTime(stop159, stop_time='14:20:00') # Omajen 3 - 92
trip.AddStopTime(stop147, stop_time='14:21:00') # Essouani - 83
trip.AddStopTime(stop222, stop_time='14:23:00') # Errahma - 118
trip.AddStopTime(stop221, stop_time='14:24:00') # Lycée Technique - 75
trip.AddStopTime(stop10, stop_time='14:27:00') # Houmet Souk - 159


trip = route.AddTrip(schedule, headsign="Houmet Souk vers Gallala")
trip.AddStopTime(stop10, stop_time='16:45:00') # Houmet Souk - 0
trip.AddStopTime(stop221, stop_time='16:47:00') # Lycée Technique - 123
trip.AddStopTime(stop222, stop_time='16:48:00') # Errahma - 79
trip.AddStopTime(stop147, stop_time='16:50:00') # Essouani - 118
trip.AddStopTime(stop159, stop_time='16:51:00') # Omajen 3 - 83
trip.AddStopTime(stop160, stop_time='16:53:00') # Bir Ben Amor - 94
trip.AddStopTime(stop161, stop_time='16:54:00') # Allamet - 63
trip.AddStopTime(stop179, stop_time='16:57:00') # Erriadh - 151
trip.AddStopTime(stop178, stop_time='16:59:00') # Zenkri - 101
trip.AddStopTime(stop187, stop_time='17:00:00') # Eljenni - 43
trip.AddStopTime(stop188, stop_time='17:01:00') # Ezayat - 60
trip.AddStopTime(stop94, stop_time='17:02:00') # Ben Arbi - 36
trip.AddStopTime(stop93, stop_time='17:03:00') # Allamet Esrandi - 41
trip.AddStopTime(stop95, stop_time='17:04:00') # Ben Aissa - 80
trip.AddStopTime(stop146, stop_time='17:06:00') # Echaouchia - 101
trip.AddStopTime(stop145, stop_time='17:06:00') # Ezitouna - 29
trip.AddStopTime(stop144, stop_time='17:07:00') # Etlat - 50
trip.AddStopTime(stop109, stop_time='17:09:00') # Tilouin - 110
trip.AddStopTime(stop108, stop_time='17:11:00') # Gallala - 102

trip = route.AddTrip(schedule, headsign="Gallala vers Houmet Souk")
trip.AddStopTime(stop108, stop_time='16:45:00') # Gallala - 0
trip.AddStopTime(stop109, stop_time='16:46:00') # Tilouin - 83
trip.AddStopTime(stop144, stop_time='16:48:00') # Etlat - 108
trip.AddStopTime(stop145, stop_time='16:49:00') # Ezitouna - 55
trip.AddStopTime(stop146, stop_time='16:50:00') # Echaouchia - 32
trip.AddStopTime(stop95, stop_time='16:52:00') # Ben Aissa - 99
trip.AddStopTime(stop93, stop_time='16:53:00') # Allamet Esrandi - 79
trip.AddStopTime(stop94, stop_time='16:54:00') # Ben Arbi - 51
trip.AddStopTime(stop188, stop_time='16:55:00') # Ezayat - 36
trip.AddStopTime(stop187, stop_time='16:56:00') # Eljenni - 55
trip.AddStopTime(stop178, stop_time='16:57:00') # Zenkri - 40
trip.AddStopTime(stop179, stop_time='16:59:00') # Erriadh - 98
trip.AddStopTime(stop161, stop_time='17:02:00') # Allamet - 158
trip.AddStopTime(stop160, stop_time='17:03:00') # Bir Ben Amor - 61
trip.AddStopTime(stop159, stop_time='17:05:00') # Omajen 3 - 92
trip.AddStopTime(stop147, stop_time='17:06:00') # Essouani - 83
trip.AddStopTime(stop222, stop_time='17:08:00') # Errahma - 118
trip.AddStopTime(stop221, stop_time='17:09:00') # Lycée Technique - 75
trip.AddStopTime(stop10, stop_time='17:12:00') # Houmet Souk - 159

trip = route.AddTrip(schedule, headsign="Houmet Souk vers Gallala")
trip.AddStopTime(stop10, stop_time='17:15:00') # Houmet Souk - 0
trip.AddStopTime(stop221, stop_time='17:17:00') # Lycée Technique - 123
trip.AddStopTime(stop222, stop_time='17:18:00') # Errahma - 79
trip.AddStopTime(stop147, stop_time='17:20:00') # Essouani - 118
trip.AddStopTime(stop159, stop_time='17:21:00') # Omajen 3 - 83
trip.AddStopTime(stop160, stop_time='17:23:00') # Bir Ben Amor - 94
trip.AddStopTime(stop161, stop_time='17:24:00') # Allamet - 63
trip.AddStopTime(stop179, stop_time='17:27:00') # Erriadh - 151
trip.AddStopTime(stop178, stop_time='17:29:00') # Zenkri - 101
trip.AddStopTime(stop187, stop_time='17:30:00') # Eljenni - 43
trip.AddStopTime(stop188, stop_time='17:31:00') # Ezayat - 60
trip.AddStopTime(stop94, stop_time='17:32:00') # Ben Arbi - 36
trip.AddStopTime(stop93, stop_time='17:33:00') # Allamet Esrandi - 41
trip.AddStopTime(stop95, stop_time='17:34:00') # Ben Aissa - 80
trip.AddStopTime(stop146, stop_time='17:36:00') # Echaouchia - 101
trip.AddStopTime(stop145, stop_time='17:36:00') # Ezitouna - 29
trip.AddStopTime(stop144, stop_time='17:37:00') # Etlat - 50
trip.AddStopTime(stop109, stop_time='17:39:00') # Tilouin - 110
trip.AddStopTime(stop108, stop_time='17:41:00') # Gallala - 102

trip = route.AddTrip(schedule, headsign="Gallala vers Houmet Souk")
trip.AddStopTime(stop108, stop_time='17:45:00') # Gallala - 0
trip.AddStopTime(stop109, stop_time='17:46:00') # Tilouin - 83
trip.AddStopTime(stop144, stop_time='17:48:00') # Etlat - 108
trip.AddStopTime(stop145, stop_time='17:49:00') # Ezitouna - 55
trip.AddStopTime(stop146, stop_time='17:50:00') # Echaouchia - 32
trip.AddStopTime(stop95, stop_time='17:52:00') # Ben Aissa - 99
trip.AddStopTime(stop93, stop_time='17:53:00') # Allamet Esrandi - 79
trip.AddStopTime(stop94, stop_time='17:54:00') # Ben Arbi - 51
trip.AddStopTime(stop188, stop_time='17:55:00') # Ezayat - 36
trip.AddStopTime(stop187, stop_time='17:56:00') # Eljenni - 55
trip.AddStopTime(stop178, stop_time='17:57:00') # Zenkri - 40
trip.AddStopTime(stop179, stop_time='17:59:00') # Erriadh - 98
trip.AddStopTime(stop161, stop_time='18:02:00') # Allamet - 158
trip.AddStopTime(stop160, stop_time='18:03:00') # Bir Ben Amor - 61
trip.AddStopTime(stop159, stop_time='18:05:00') # Omajen 3 - 92
trip.AddStopTime(stop147, stop_time='18:06:00') # Essouani - 83
trip.AddStopTime(stop222, stop_time='18:08:00') # Errahma - 118
trip.AddStopTime(stop221, stop_time='18:09:00') # Lycée Technique - 75
trip.AddStopTime(stop10, stop_time='18:12:00') # Houmet Souk - 159

trip = route.AddTrip(schedule, headsign="Houmet Souk vers Gallala")
trip.AddStopTime(stop10, stop_time='18:15:00') # Houmet Souk - 0
trip.AddStopTime(stop221, stop_time='18:17:00') # Lycée Technique - 123
trip.AddStopTime(stop222, stop_time='18:18:00') # Errahma - 79
trip.AddStopTime(stop147, stop_time='18:20:00') # Essouani - 118
trip.AddStopTime(stop159, stop_time='18:21:00') # Omajen 3 - 83
trip.AddStopTime(stop160, stop_time='18:23:00') # Bir Ben Amor - 94
trip.AddStopTime(stop161, stop_time='18:24:00') # Allamet - 63
trip.AddStopTime(stop179, stop_time='18:27:00') # Erriadh - 151
trip.AddStopTime(stop178, stop_time='18:29:00') # Zenkri - 101
trip.AddStopTime(stop187, stop_time='18:30:00') # Eljenni - 43
trip.AddStopTime(stop188, stop_time='18:31:00') # Ezayat - 60
trip.AddStopTime(stop94, stop_time='18:32:00') # Ben Arbi - 36
trip.AddStopTime(stop93, stop_time='18:33:00') # Allamet Esrandi - 41
trip.AddStopTime(stop95, stop_time='18:34:00') # Ben Aissa - 80
trip.AddStopTime(stop146, stop_time='18:36:00') # Echaouchia - 101
trip.AddStopTime(stop145, stop_time='18:36:00') # Ezitouna - 29
trip.AddStopTime(stop144, stop_time='18:37:00') # Etlat - 50
trip.AddStopTime(stop109, stop_time='18:39:00') # Tilouin - 110
trip.AddStopTime(stop108, stop_time='18:41:00') # Gallala - 102

trip = route.AddTrip(schedule, headsign="Gallala vers Houmet Souk")
trip.AddStopTime(stop108, stop_time='18:45:00') # Gallala - 0
trip.AddStopTime(stop109, stop_time='18:46:00') # Tilouin - 83
trip.AddStopTime(stop144, stop_time='18:48:00') # Etlat - 108
trip.AddStopTime(stop145, stop_time='18:49:00') # Ezitouna - 55
trip.AddStopTime(stop146, stop_time='18:50:00') # Echaouchia - 32
trip.AddStopTime(stop95, stop_time='18:52:00') # Ben Aissa - 99
trip.AddStopTime(stop93, stop_time='18:53:00') # Allamet Esrandi - 79
trip.AddStopTime(stop94, stop_time='18:54:00') # Ben Arbi - 51
trip.AddStopTime(stop188, stop_time='18:55:00') # Ezayat - 36
trip.AddStopTime(stop187, stop_time='18:56:00') # Eljenni - 55
trip.AddStopTime(stop178, stop_time='18:57:00') # Zenkri - 40
trip.AddStopTime(stop179, stop_time='18:59:00') # Erriadh - 98
trip.AddStopTime(stop161, stop_time='19:02:00') # Allamet - 158
trip.AddStopTime(stop160, stop_time='19:03:00') # Bir Ben Amor - 61
trip.AddStopTime(stop159, stop_time='19:05:00') # Omajen 3 - 92
trip.AddStopTime(stop147, stop_time='19:06:00') # Essouani - 83
trip.AddStopTime(stop222, stop_time='19:08:00') # Errahma - 118
trip.AddStopTime(stop221, stop_time='19:09:00') # Lycée Technique - 75
trip.AddStopTime(stop10, stop_time='19:12:00') # Houmet Souk - 159


route = schedule.AddRoute(short_name="SU415", long_name="Houmet Souk,L'aéroport",
                          route_type="Bus")

trip = route.AddTrip(schedule, headsign="Houmet Souk vers L'aéroport")
trip.AddStopTime(stop10, stop_time='07:10:00') # Houmet Souk - 0
trip.AddStopTime(stop9, stop_time='07:14:00') # Bir mgalas - 247
trip.AddStopTime(stop8, stop_time='07:15:00') # Elhimaya - 34
trip.AddStopTime(stop3, stop_time='07:17:00') # Mosquet Kébir - 94
trip.AddStopTime(stop2, stop_time='07:19:00') # Mellita 1 - 102
trip.AddStopTime(stop1, stop_time='07:21:00') # Mellita 2 - 120
trip.AddStopTime(stop6, stop_time='07:22:00') # Margane 1 - 84
trip.AddStopTime(stop7, stop_time='07:23:00') # Margane 2 - 46
trip.AddStopTime(stop4, stop_time='07:27:00') # Essouissi - 244
trip.AddStopTime(stop5, stop_time='07:28:00') # L'aéroport - 75

trip = route.AddTrip(schedule, headsign="L'aéroport vers Houmet Souk")
trip.AddStopTime(stop5, stop_time='07:30:00') # L'aéroport - 0
trip.AddStopTime(stop4, stop_time='07:32:00') # Essouissi - 101
trip.AddStopTime(stop7, stop_time='07:35:00') # Margane 2 - 207
trip.AddStopTime(stop6, stop_time='07:36:00') # Margane 1 - 46
trip.AddStopTime(stop1, stop_time='07:38:00') # Mellita 2 - 128
trip.AddStopTime(stop2, stop_time='07:40:00') # Mellita 1 - 130
trip.AddStopTime(stop3, stop_time='07:42:00') # Mosquet Kébir - 106
trip.AddStopTime(stop8, stop_time='07:44:00') # Elhimaya - 100
trip.AddStopTime(stop9, stop_time='07:45:00') # Bir mgalas - 35
trip.AddStopTime(stop10, stop_time='07:48:00') # Houmet Souk - 204

trip = route.AddTrip(schedule, headsign="Houmet Souk vers L'aéroport")
trip.AddStopTime(stop10, stop_time='12:15:00') # Houmet Souk - 0
trip.AddStopTime(stop9, stop_time='12:19:00') # Bir mgalas - 247
trip.AddStopTime(stop8, stop_time='12:20:00') # Elhimaya - 34
trip.AddStopTime(stop3, stop_time='12:22:00') # Mosquet Kébir - 94
trip.AddStopTime(stop2, stop_time='12:24:00') # Mellita 1 - 102
trip.AddStopTime(stop1, stop_time='12:26:00') # Mellita 2 - 120
trip.AddStopTime(stop6, stop_time='12:27:00') # Margane 1 - 84
trip.AddStopTime(stop7, stop_time='12:28:00') # Margane 2 - 46
trip.AddStopTime(stop4, stop_time='12:32:00') # Essouissi - 244
trip.AddStopTime(stop5, stop_time='12:33:00') # L'aéroport - 75

trip = route.AddTrip(schedule, headsign="L'aéroport vers Houmet Souk")
trip.AddStopTime(stop5, stop_time='13:00:00') # L'aéroport - 0
trip.AddStopTime(stop4, stop_time='13:02:00') # Essouissi - 101
trip.AddStopTime(stop7, stop_time='13:05:00') # Margane 2 - 207
trip.AddStopTime(stop6, stop_time='13:06:00') # Margane 1 - 46
trip.AddStopTime(stop1, stop_time='13:08:00') # Mellita 2 - 128
trip.AddStopTime(stop2, stop_time='13:10:00') # Mellita 1 - 130
trip.AddStopTime(stop3, stop_time='13:12:00') # Mosquet Kébir - 106
trip.AddStopTime(stop8, stop_time='13:14:00') # Elhimaya - 100
trip.AddStopTime(stop9, stop_time='13:15:00') # Bir mgalas - 35
trip.AddStopTime(stop10, stop_time='13:18:00') # Houmet Souk - 204

trip = route.AddTrip(schedule, headsign="Houmet Souk vers L'aéroport")
trip.AddStopTime(stop10, stop_time='18:15:00') # Houmet Souk - 0
trip.AddStopTime(stop9, stop_time='18:19:00') # Bir mgalas - 247
trip.AddStopTime(stop8, stop_time='18:20:00') # Elhimaya - 34
trip.AddStopTime(stop3, stop_time='18:22:00') # Mosquet Kébir - 94
trip.AddStopTime(stop2, stop_time='18:24:00') # Mellita 1 - 102
trip.AddStopTime(stop1, stop_time='18:26:00') # Mellita 2 - 120
trip.AddStopTime(stop6, stop_time='18:27:00') # Margane 1 - 84
trip.AddStopTime(stop7, stop_time='18:28:00') # Margane 2 - 46
trip.AddStopTime(stop4, stop_time='18:32:00') # Essouissi - 244
trip.AddStopTime(stop5, stop_time='18:33:00') # L'aéroport - 75

trip = route.AddTrip(schedule, headsign="L'aéroport vers Houmet Souk")
trip.AddStopTime(stop5, stop_time='18:30:00') # L'aéroport - 0
trip.AddStopTime(stop4, stop_time='18:32:00') # Essouissi - 101
trip.AddStopTime(stop7, stop_time='18:35:00') # Margane 2 - 207
trip.AddStopTime(stop6, stop_time='18:36:00') # Margane 1 - 46
trip.AddStopTime(stop1, stop_time='18:38:00') # Mellita 2 - 128
trip.AddStopTime(stop2, stop_time='18:40:00') # Mellita 1 - 130
trip.AddStopTime(stop3, stop_time='18:42:00') # Mosquet Kébir - 106
trip.AddStopTime(stop8, stop_time='18:44:00') # Elhimaya - 100
trip.AddStopTime(stop9, stop_time='18:45:00') # Bir mgalas - 35
trip.AddStopTime(stop10, stop_time='18:48:00') # Houmet Souk - 204

route = schedule.AddRoute(short_name="SU416", long_name="Houmet Souk, Sedwikech, Elkantara",
                          route_type="Bus")

trip = route.AddTrip(schedule, headsign="Houmet Souk vers Elkantara")
trip.AddStopTime(stop10, stop_time='06:00:00') # Houmet Souk - 0
trip.AddStopTime(stop221, stop_time='06:02:00') # Lycée Technique - 123
trip.AddStopTime(stop222, stop_time='06:03:00') # Errahma - 79
trip.AddStopTime(stop147, stop_time='06:05:00') # Essouani - 118
trip.AddStopTime(stop159, stop_time='06:06:00') # Omajen 3 - 83
trip.AddStopTime(stop160, stop_time='06:08:00') # Bir Ben Amor - 94
trip.AddStopTime(stop161, stop_time='06:09:00') # Allamet - 63
trip.AddStopTime(stop174, stop_time='06:10:00') # Ben Moussa - 72
trip.AddStopTime(stop175, stop_time='06:10:00') # Mosbah - 26
trip.AddStopTime(stop90, stop_time='06:12:00') # Elmay - 145
trip.AddStopTime(stop91, stop_time='06:15:00') # Elmaabri - 165
trip.AddStopTime(stop215, stop_time='06:16:00') # Echhoud - 59
trip.AddStopTime(stop216, stop_time='06:17:00') # Robana - 78
trip.AddStopTime(stop217, stop_time='06:19:00') # Chnib - 108
trip.AddStopTime(stop218, stop_time='06:20:00') # Krouna - 55
trip.AddStopTime(stop219, stop_time='06:21:00') # Angar Hmida - 43
trip.AddStopTime(stop119, stop_time='06:22:00') # Dar Echabeb - 73
trip.AddStopTime(stop118, stop_time='06:23:00') # Sedwikech - 44
trip.AddStopTime(stop143, stop_time='06:26:00') # Oued Ajmi - 177
trip.AddStopTime(stop142, stop_time='06:27:00') # Elmhamid - 35
trip.AddStopTime(stop141, stop_time='06:30:00') # Elkantara - 181

trip = route.AddTrip(schedule, headsign="Elkantara vers Houmet Souk")
trip.AddStopTime(stop141, stop_time='06:30:00') # Elkantara - 0
trip.AddStopTime(stop142, stop_time='06:33:00') # Elmhamid - 187
trip.AddStopTime(stop143, stop_time='06:34:00') # Oued Ajmi - 35
trip.AddStopTime(stop118, stop_time='06:37:00') # Sedwikech - 168
trip.AddStopTime(stop119, stop_time='06:38:00') # Dar Echabeb - 45
trip.AddStopTime(stop219, stop_time='06:39:00') # Angar Hmida - 75
trip.AddStopTime(stop218, stop_time='06:40:00') # Krouna - 42
trip.AddStopTime(stop217, stop_time='06:41:00') # Chnib - 54
trip.AddStopTime(stop216, stop_time='06:43:00') # Robana - 101
trip.AddStopTime(stop215, stop_time='06:45:00') # Echhoud - 106
trip.AddStopTime(stop91, stop_time='06:46:00') # Elmaabri - 60
trip.AddStopTime(stop90, stop_time='06:49:00') # Elmay - 157
trip.AddStopTime(stop175, stop_time='06:51:00') # Mosbah - 121
trip.AddStopTime(stop174, stop_time='06:51:00') # Ben Moussa - 26
trip.AddStopTime(stop161, stop_time='06:52:00') # Allamet - 72
trip.AddStopTime(stop160, stop_time='06:53:00') # Bir Ben Amor - 61
trip.AddStopTime(stop159, stop_time='06:55:00') # Omajen 3 - 92
trip.AddStopTime(stop147, stop_time='06:56:00') # Essouani - 83
trip.AddStopTime(stop222, stop_time='06:58:00') # Errahma - 118
trip.AddStopTime(stop221, stop_time='06:59:00') # Lycée Technique - 75
trip.AddStopTime(stop10, stop_time='07:02:00') # Houmet Souk - 159

trip = route.AddTrip(schedule, headsign="Houmet Souk vers Elkantara")
trip.AddStopTime(stop10, stop_time='07:25:00') # Houmet Souk - 0
trip.AddStopTime(stop221, stop_time='07:27:00') # Lycée Technique - 123
trip.AddStopTime(stop222, stop_time='07:28:00') # Errahma - 79
trip.AddStopTime(stop147, stop_time='07:30:00') # Essouani - 118
trip.AddStopTime(stop159, stop_time='07:31:00') # Omajen 3 - 83
trip.AddStopTime(stop160, stop_time='07:33:00') # Bir Ben Amor - 94
trip.AddStopTime(stop161, stop_time='07:34:00') # Allamet - 63
trip.AddStopTime(stop174, stop_time='07:35:00') # Ben Moussa - 72
trip.AddStopTime(stop175, stop_time='07:35:00') # Mosbah - 26
trip.AddStopTime(stop90, stop_time='07:37:00') # Elmay - 145
trip.AddStopTime(stop91, stop_time='07:40:00') # Elmaabri - 165
trip.AddStopTime(stop215, stop_time='07:41:00') # Echhoud - 59
trip.AddStopTime(stop216, stop_time='07:42:00') # Robana - 78
trip.AddStopTime(stop217, stop_time='07:44:00') # Chnib - 108
trip.AddStopTime(stop218, stop_time='07:45:00') # Krouna - 55
trip.AddStopTime(stop219, stop_time='07:46:00') # Angar Hmida - 43
trip.AddStopTime(stop119, stop_time='07:47:00') # Dar Echabeb - 73
trip.AddStopTime(stop118, stop_time='07:48:00') # Sedwikech - 44
trip.AddStopTime(stop143, stop_time='07:51:00') # Oued Ajmi - 177
trip.AddStopTime(stop142, stop_time='07:52:00') # Elmhamid - 35
trip.AddStopTime(stop141, stop_time='07:55:00') # Elkantara - 181

trip = route.AddTrip(schedule, headsign="Elkantara vers Houmet Souk")
trip.AddStopTime(stop141, stop_time='08:10:00') # Elkantara - 0
trip.AddStopTime(stop142, stop_time='08:13:00') # Elmhamid - 187
trip.AddStopTime(stop143, stop_time='08:14:00') # Oued Ajmi - 35
trip.AddStopTime(stop118, stop_time='08:17:00') # Sedwikech - 168
trip.AddStopTime(stop119, stop_time='08:18:00') # Dar Echabeb - 45
trip.AddStopTime(stop219, stop_time='08:19:00') # Angar Hmida - 75
trip.AddStopTime(stop218, stop_time='08:20:00') # Krouna - 42
trip.AddStopTime(stop217, stop_time='08:21:00') # Chnib - 54
trip.AddStopTime(stop216, stop_time='08:23:00') # Robana - 101
trip.AddStopTime(stop215, stop_time='08:25:00') # Echhoud - 106
trip.AddStopTime(stop91, stop_time='08:26:00') # Elmaabri - 60
trip.AddStopTime(stop90, stop_time='08:29:00') # Elmay - 157
trip.AddStopTime(stop175, stop_time='08:31:00') # Mosbah - 121
trip.AddStopTime(stop174, stop_time='08:31:00') # Ben Moussa - 26
trip.AddStopTime(stop161, stop_time='08:32:00') # Allamet - 72
trip.AddStopTime(stop160, stop_time='08:33:00') # Bir Ben Amor - 61
trip.AddStopTime(stop159, stop_time='08:35:00') # Omajen 3 - 92
trip.AddStopTime(stop147, stop_time='08:36:00') # Essouani - 83
trip.AddStopTime(stop222, stop_time='08:38:00') # Errahma - 118
trip.AddStopTime(stop221, stop_time='08:39:00') # Lycée Technique - 75
trip.AddStopTime(stop10, stop_time='08:42:00') # Houmet Souk - 159

trip = route.AddTrip(schedule, headsign="Houmet Souk vers Elkantara")
trip.AddStopTime(stop10, stop_time='08:30:00') # Houmet Souk - 0
trip.AddStopTime(stop221, stop_time='08:32:00') # Lycée Technique - 123
trip.AddStopTime(stop222, stop_time='08:33:00') # Errahma - 79
trip.AddStopTime(stop147, stop_time='08:35:00') # Essouani - 118
trip.AddStopTime(stop159, stop_time='08:36:00') # Omajen 3 - 83
trip.AddStopTime(stop160, stop_time='08:38:00') # Bir Ben Amor - 94
trip.AddStopTime(stop161, stop_time='08:39:00') # Allamet - 63
trip.AddStopTime(stop174, stop_time='08:40:00') # Ben Moussa - 72
trip.AddStopTime(stop175, stop_time='08:40:00') # Mosbah - 26
trip.AddStopTime(stop90, stop_time='08:42:00') # Elmay - 145
trip.AddStopTime(stop91, stop_time='08:45:00') # Elmaabri - 165
trip.AddStopTime(stop215, stop_time='08:46:00') # Echhoud - 59
trip.AddStopTime(stop216, stop_time='08:47:00') # Robana - 78
trip.AddStopTime(stop217, stop_time='08:49:00') # Chnib - 108
trip.AddStopTime(stop218, stop_time='08:50:00') # Krouna - 55
trip.AddStopTime(stop219, stop_time='08:51:00') # Angar Hmida - 43
trip.AddStopTime(stop119, stop_time='08:52:00') # Dar Echabeb - 73
trip.AddStopTime(stop118, stop_time='08:53:00') # Sedwikech - 44
trip.AddStopTime(stop143, stop_time='08:56:00') # Oued Ajmi - 177
trip.AddStopTime(stop142, stop_time='08:57:00') # Elmhamid - 35
trip.AddStopTime(stop141, stop_time='09:00:00') # Elkantara - 181

trip = route.AddTrip(schedule, headsign="Elkantara vers Houmet Souk")
trip.AddStopTime(stop141, stop_time='09:00:00') # Elkantara - 0
trip.AddStopTime(stop142, stop_time='09:03:00') # Elmhamid - 187
trip.AddStopTime(stop143, stop_time='09:04:00') # Oued Ajmi - 35
trip.AddStopTime(stop118, stop_time='09:07:00') # Sedwikech - 168
trip.AddStopTime(stop119, stop_time='09:08:00') # Dar Echabeb - 45
trip.AddStopTime(stop219, stop_time='09:09:00') # Angar Hmida - 75
trip.AddStopTime(stop218, stop_time='09:10:00') # Krouna - 42
trip.AddStopTime(stop217, stop_time='09:11:00') # Chnib - 54
trip.AddStopTime(stop216, stop_time='09:13:00') # Robana - 101
trip.AddStopTime(stop215, stop_time='09:15:00') # Echhoud - 106
trip.AddStopTime(stop91, stop_time='09:16:00') # Elmaabri - 60
trip.AddStopTime(stop90, stop_time='09:19:00') # Elmay - 157
trip.AddStopTime(stop175, stop_time='09:21:00') # Mosbah - 121
trip.AddStopTime(stop174, stop_time='09:21:00') # Ben Moussa - 26
trip.AddStopTime(stop161, stop_time='09:22:00') # Allamet - 72
trip.AddStopTime(stop160, stop_time='09:23:00') # Bir Ben Amor - 61
trip.AddStopTime(stop159, stop_time='09:25:00') # Omajen 3 - 92
trip.AddStopTime(stop147, stop_time='09:26:00') # Essouani - 83
trip.AddStopTime(stop222, stop_time='09:28:00') # Errahma - 118
trip.AddStopTime(stop221, stop_time='09:29:00') # Lycée Technique - 75
trip.AddStopTime(stop10, stop_time='09:32:00') # Houmet Souk - 159

trip = route.AddTrip(schedule, headsign="Houmet Souk vers Elkantara")
trip.AddStopTime(stop10, stop_time='10:30:00') # Houmet Souk - 0
trip.AddStopTime(stop221, stop_time='10:32:00') # Lycée Technique - 123
trip.AddStopTime(stop222, stop_time='10:33:00') # Errahma - 79
trip.AddStopTime(stop147, stop_time='10:35:00') # Essouani - 118
trip.AddStopTime(stop159, stop_time='10:36:00') # Omajen 3 - 83
trip.AddStopTime(stop160, stop_time='10:38:00') # Bir Ben Amor - 94
trip.AddStopTime(stop161, stop_time='10:39:00') # Allamet - 63
trip.AddStopTime(stop174, stop_time='10:40:00') # Ben Moussa - 72
trip.AddStopTime(stop175, stop_time='10:40:00') # Mosbah - 26
trip.AddStopTime(stop90, stop_time='10:42:00') # Elmay - 145
trip.AddStopTime(stop91, stop_time='10:45:00') # Elmaabri - 165
trip.AddStopTime(stop215, stop_time='10:46:00') # Echhoud - 59
trip.AddStopTime(stop216, stop_time='10:47:00') # Robana - 78
trip.AddStopTime(stop217, stop_time='10:49:00') # Chnib - 108
trip.AddStopTime(stop218, stop_time='10:50:00') # Krouna - 55
trip.AddStopTime(stop219, stop_time='10:51:00') # Angar Hmida - 43
trip.AddStopTime(stop119, stop_time='10:52:00') # Dar Echabeb - 73
trip.AddStopTime(stop118, stop_time='10:53:00') # Sedwikech - 44
trip.AddStopTime(stop143, stop_time='10:56:00') # Oued Ajmi - 177
trip.AddStopTime(stop142, stop_time='10:57:00') # Elmhamid - 35
trip.AddStopTime(stop141, stop_time='11:00:00') # Elkantara - 181

trip = route.AddTrip(schedule, headsign="Elkantara vers Houmet Souk")
trip.AddStopTime(stop141, stop_time='11:00:00') # Elkantara - 0
trip.AddStopTime(stop142, stop_time='11:03:00') # Elmhamid - 187
trip.AddStopTime(stop143, stop_time='11:04:00') # Oued Ajmi - 35
trip.AddStopTime(stop118, stop_time='11:07:00') # Sedwikech - 168
trip.AddStopTime(stop119, stop_time='11:08:00') # Dar Echabeb - 45
trip.AddStopTime(stop219, stop_time='11:09:00') # Angar Hmida - 75
trip.AddStopTime(stop218, stop_time='11:10:00') # Krouna - 42
trip.AddStopTime(stop217, stop_time='11:11:00') # Chnib - 54
trip.AddStopTime(stop216, stop_time='11:13:00') # Robana - 101
trip.AddStopTime(stop215, stop_time='11:15:00') # Echhoud - 106
trip.AddStopTime(stop91, stop_time='11:16:00') # Elmaabri - 60
trip.AddStopTime(stop90, stop_time='11:19:00') # Elmay - 157
trip.AddStopTime(stop175, stop_time='11:21:00') # Mosbah - 121
trip.AddStopTime(stop174, stop_time='11:21:00') # Ben Moussa - 26
trip.AddStopTime(stop161, stop_time='11:22:00') # Allamet - 72
trip.AddStopTime(stop160, stop_time='11:23:00') # Bir Ben Amor - 61
trip.AddStopTime(stop159, stop_time='11:25:00') # Omajen 3 - 92
trip.AddStopTime(stop147, stop_time='11:26:00') # Essouani - 83
trip.AddStopTime(stop222, stop_time='11:28:00') # Errahma - 118
trip.AddStopTime(stop221, stop_time='11:29:00') # Lycée Technique - 75
trip.AddStopTime(stop10, stop_time='11:32:00') # Houmet Souk - 159


trip = route.AddTrip(schedule, headsign="Houmet Souk vers Elkantara")
trip.AddStopTime(stop10, stop_time='12:15:00') # Houmet Souk - 0
trip.AddStopTime(stop221, stop_time='12:17:00') # Lycée Technique - 123
trip.AddStopTime(stop222, stop_time='12:18:00') # Errahma - 79
trip.AddStopTime(stop147, stop_time='12:20:00') # Essouani - 118
trip.AddStopTime(stop159, stop_time='12:21:00') # Omajen 3 - 83
trip.AddStopTime(stop160, stop_time='12:23:00') # Bir Ben Amor - 94
trip.AddStopTime(stop161, stop_time='12:24:00') # Allamet - 63
trip.AddStopTime(stop174, stop_time='12:25:00') # Ben Moussa - 72
trip.AddStopTime(stop175, stop_time='12:25:00') # Mosbah - 26
trip.AddStopTime(stop90, stop_time='12:27:00') # Elmay - 145
trip.AddStopTime(stop91, stop_time='12:30:00') # Elmaabri - 165
trip.AddStopTime(stop215, stop_time='12:31:00') # Echhoud - 59
trip.AddStopTime(stop216, stop_time='12:32:00') # Robana - 78
trip.AddStopTime(stop217, stop_time='12:34:00') # Chnib - 108
trip.AddStopTime(stop218, stop_time='12:35:00') # Krouna - 55
trip.AddStopTime(stop219, stop_time='12:36:00') # Angar Hmida - 43
trip.AddStopTime(stop119, stop_time='12:37:00') # Dar Echabeb - 73
trip.AddStopTime(stop118, stop_time='12:38:00') # Sedwikech - 44
trip.AddStopTime(stop143, stop_time='12:41:00') # Oued Ajmi - 177
trip.AddStopTime(stop142, stop_time='12:42:00') # Elmhamid - 35
trip.AddStopTime(stop141, stop_time='12:45:00') # Elkantara - 181

trip = route.AddTrip(schedule, headsign="Elkantara vers Houmet Souk")
trip.AddStopTime(stop141, stop_time='12:50:00') # Elkantara - 0
trip.AddStopTime(stop142, stop_time='12:53:00') # Elmhamid - 187
trip.AddStopTime(stop143, stop_time='12:54:00') # Oued Ajmi - 35
trip.AddStopTime(stop118, stop_time='12:57:00') # Sedwikech - 168
trip.AddStopTime(stop119, stop_time='12:58:00') # Dar Echabeb - 45
trip.AddStopTime(stop219, stop_time='12:59:00') # Angar Hmida - 75
trip.AddStopTime(stop218, stop_time='13:00:00') # Krouna - 42
trip.AddStopTime(stop217, stop_time='13:01:00') # Chnib - 54
trip.AddStopTime(stop216, stop_time='13:03:00') # Robana - 101
trip.AddStopTime(stop215, stop_time='13:05:00') # Echhoud - 106
trip.AddStopTime(stop91, stop_time='13:06:00') # Elmaabri - 60
trip.AddStopTime(stop90, stop_time='13:09:00') # Elmay - 157
trip.AddStopTime(stop175, stop_time='13:11:00') # Mosbah - 121
trip.AddStopTime(stop174, stop_time='13:11:00') # Ben Moussa - 26
trip.AddStopTime(stop161, stop_time='13:12:00') # Allamet - 72
trip.AddStopTime(stop160, stop_time='13:13:00') # Bir Ben Amor - 61
trip.AddStopTime(stop159, stop_time='13:15:00') # Omajen 3 - 92
trip.AddStopTime(stop147, stop_time='13:16:00') # Essouani - 83
trip.AddStopTime(stop222, stop_time='13:18:00') # Errahma - 118
trip.AddStopTime(stop221, stop_time='13:19:00') # Lycée Technique - 75
trip.AddStopTime(stop10, stop_time='13:22:00') # Houmet Souk - 159

trip = route.AddTrip(schedule, headsign="Houmet Souk vers Elkantara")
trip.AddStopTime(stop10, stop_time='13:00:00') # Houmet Souk - 0
trip.AddStopTime(stop221, stop_time='13:02:00') # Lycée Technique - 123
trip.AddStopTime(stop222, stop_time='13:03:00') # Errahma - 79
trip.AddStopTime(stop147, stop_time='13:05:00') # Essouani - 118
trip.AddStopTime(stop159, stop_time='13:06:00') # Omajen 3 - 83
trip.AddStopTime(stop160, stop_time='13:08:00') # Bir Ben Amor - 94
trip.AddStopTime(stop161, stop_time='13:09:00') # Allamet - 63
trip.AddStopTime(stop174, stop_time='13:10:00') # Ben Moussa - 72
trip.AddStopTime(stop175, stop_time='13:10:00') # Mosbah - 26
trip.AddStopTime(stop90, stop_time='13:12:00') # Elmay - 145
trip.AddStopTime(stop91, stop_time='13:15:00') # Elmaabri - 165
trip.AddStopTime(stop215, stop_time='13:16:00') # Echhoud - 59
trip.AddStopTime(stop216, stop_time='13:17:00') # Robana - 78
trip.AddStopTime(stop217, stop_time='13:19:00') # Chnib - 108
trip.AddStopTime(stop218, stop_time='13:20:00') # Krouna - 55
trip.AddStopTime(stop219, stop_time='13:21:00') # Angar Hmida - 43
trip.AddStopTime(stop119, stop_time='13:22:00') # Dar Echabeb - 73
trip.AddStopTime(stop118, stop_time='13:23:00') # Sedwikech - 44
trip.AddStopTime(stop143, stop_time='13:26:00') # Oued Ajmi - 177
trip.AddStopTime(stop142, stop_time='13:27:00') # Elmhamid - 35
trip.AddStopTime(stop141, stop_time='13:30:00') # Elkantara - 181

trip = route.AddTrip(schedule, headsign="Elkantara vers Houmet Souk")
trip.AddStopTime(stop141, stop_time='13:15:00') # Elkantara - 0
trip.AddStopTime(stop142, stop_time='13:18:00') # Elmhamid - 187
trip.AddStopTime(stop143, stop_time='13:19:00') # Oued Ajmi - 35
trip.AddStopTime(stop118, stop_time='13:22:00') # Sedwikech - 168
trip.AddStopTime(stop119, stop_time='13:23:00') # Dar Echabeb - 45
trip.AddStopTime(stop219, stop_time='13:24:00') # Angar Hmida - 75
trip.AddStopTime(stop218, stop_time='13:25:00') # Krouna - 42
trip.AddStopTime(stop217, stop_time='13:26:00') # Chnib - 54
trip.AddStopTime(stop216, stop_time='13:28:00') # Robana - 101
trip.AddStopTime(stop215, stop_time='13:30:00') # Echhoud - 106
trip.AddStopTime(stop91, stop_time='13:31:00') # Elmaabri - 60
trip.AddStopTime(stop90, stop_time='13:34:00') # Elmay - 157
trip.AddStopTime(stop175, stop_time='13:36:00') # Mosbah - 121
trip.AddStopTime(stop174, stop_time='13:36:00') # Ben Moussa - 26
trip.AddStopTime(stop161, stop_time='13:37:00') # Allamet - 72
trip.AddStopTime(stop160, stop_time='13:38:00') # Bir Ben Amor - 61
trip.AddStopTime(stop159, stop_time='13:40:00') # Omajen 3 - 92
trip.AddStopTime(stop147, stop_time='13:41:00') # Essouani - 83
trip.AddStopTime(stop222, stop_time='13:43:00') # Errahma - 118
trip.AddStopTime(stop221, stop_time='13:44:00') # Lycée Technique - 75
trip.AddStopTime(stop10, stop_time='13:47:00') # Houmet Souk - 159

trip = route.AddTrip(schedule, headsign="Houmet Souk vers Elkantara")
trip.AddStopTime(stop10, stop_time='14:30:00') # Houmet Souk - 0
trip.AddStopTime(stop221, stop_time='14:32:00') # Lycée Technique - 123
trip.AddStopTime(stop222, stop_time='14:33:00') # Errahma - 79
trip.AddStopTime(stop147, stop_time='14:35:00') # Essouani - 118
trip.AddStopTime(stop159, stop_time='14:36:00') # Omajen 3 - 83
trip.AddStopTime(stop160, stop_time='14:38:00') # Bir Ben Amor - 94
trip.AddStopTime(stop161, stop_time='14:39:00') # Allamet - 63
trip.AddStopTime(stop174, stop_time='14:40:00') # Ben Moussa - 72
trip.AddStopTime(stop175, stop_time='14:40:00') # Mosbah - 26
trip.AddStopTime(stop90, stop_time='14:42:00') # Elmay - 145
trip.AddStopTime(stop91, stop_time='14:45:00') # Elmaabri - 165
trip.AddStopTime(stop215, stop_time='14:46:00') # Echhoud - 59
trip.AddStopTime(stop216, stop_time='14:47:00') # Robana - 78
trip.AddStopTime(stop217, stop_time='14:49:00') # Chnib - 108
trip.AddStopTime(stop218, stop_time='14:50:00') # Krouna - 55
trip.AddStopTime(stop219, stop_time='14:51:00') # Angar Hmida - 43
trip.AddStopTime(stop119, stop_time='14:52:00') # Dar Echabeb - 73
trip.AddStopTime(stop118, stop_time='14:53:00') # Sedwikech - 44
trip.AddStopTime(stop143, stop_time='14:56:00') # Oued Ajmi - 177
trip.AddStopTime(stop142, stop_time='14:57:00') # Elmhamid - 35
trip.AddStopTime(stop141, stop_time='15:00:00') # Elkantara - 181

trip = route.AddTrip(schedule, headsign="Elkantara vers Houmet Souk")
trip.AddStopTime(stop141, stop_time='14:30:00') # Elkantara - 0
trip.AddStopTime(stop142, stop_time='14:33:00') # Elmhamid - 187
trip.AddStopTime(stop143, stop_time='14:34:00') # Oued Ajmi - 35
trip.AddStopTime(stop118, stop_time='14:37:00') # Sedwikech - 168
trip.AddStopTime(stop119, stop_time='14:38:00') # Dar Echabeb - 45
trip.AddStopTime(stop219, stop_time='14:39:00') # Angar Hmida - 75
trip.AddStopTime(stop218, stop_time='14:40:00') # Krouna - 42
trip.AddStopTime(stop217, stop_time='14:41:00') # Chnib - 54
trip.AddStopTime(stop216, stop_time='14:43:00') # Robana - 101
trip.AddStopTime(stop215, stop_time='14:45:00') # Echhoud - 106
trip.AddStopTime(stop91, stop_time='14:46:00') # Elmaabri - 60
trip.AddStopTime(stop90, stop_time='14:49:00') # Elmay - 157
trip.AddStopTime(stop175, stop_time='14:51:00') # Mosbah - 121
trip.AddStopTime(stop174, stop_time='14:51:00') # Ben Moussa - 26
trip.AddStopTime(stop161, stop_time='14:52:00') # Allamet - 72
trip.AddStopTime(stop160, stop_time='14:53:00') # Bir Ben Amor - 61
trip.AddStopTime(stop159, stop_time='14:55:00') # Omajen 3 - 92
trip.AddStopTime(stop147, stop_time='14:56:00') # Essouani - 83
trip.AddStopTime(stop222, stop_time='14:58:00') # Errahma - 118
trip.AddStopTime(stop221, stop_time='14:59:00') # Lycée Technique - 75
trip.AddStopTime(stop10, stop_time='15:02:00') # Houmet Souk - 159

trip = route.AddTrip(schedule, headsign="Houmet Souk vers Elkantara")
trip.AddStopTime(stop10, stop_time='15:30:00') # Houmet Souk - 0
trip.AddStopTime(stop221, stop_time='15:32:00') # Lycée Technique - 123
trip.AddStopTime(stop222, stop_time='15:33:00') # Errahma - 79
trip.AddStopTime(stop147, stop_time='15:35:00') # Essouani - 118
trip.AddStopTime(stop159, stop_time='15:36:00') # Omajen 3 - 83
trip.AddStopTime(stop160, stop_time='15:38:00') # Bir Ben Amor - 94
trip.AddStopTime(stop161, stop_time='15:39:00') # Allamet - 63
trip.AddStopTime(stop174, stop_time='15:40:00') # Ben Moussa - 72
trip.AddStopTime(stop175, stop_time='15:40:00') # Mosbah - 26
trip.AddStopTime(stop90, stop_time='15:42:00') # Elmay - 145
trip.AddStopTime(stop91, stop_time='15:45:00') # Elmaabri - 165
trip.AddStopTime(stop215, stop_time='15:46:00') # Echhoud - 59
trip.AddStopTime(stop216, stop_time='15:47:00') # Robana - 78
trip.AddStopTime(stop217, stop_time='15:49:00') # Chnib - 108
trip.AddStopTime(stop218, stop_time='15:50:00') # Krouna - 55
trip.AddStopTime(stop219, stop_time='15:51:00') # Angar Hmida - 43
trip.AddStopTime(stop119, stop_time='15:52:00') # Dar Echabeb - 73
trip.AddStopTime(stop118, stop_time='15:53:00') # Sedwikech - 44
trip.AddStopTime(stop143, stop_time='15:56:00') # Oued Ajmi - 177
trip.AddStopTime(stop142, stop_time='15:57:00') # Elmhamid - 35
trip.AddStopTime(stop141, stop_time='16:00:00') # Elkantara - 181

trip = route.AddTrip(schedule, headsign="Elkantara vers Houmet Souk")
trip.AddStopTime(stop141, stop_time='17:50:00') # Elkantara - 0
trip.AddStopTime(stop142, stop_time='17:53:00') # Elmhamid - 187
trip.AddStopTime(stop143, stop_time='17:54:00') # Oued Ajmi - 35
trip.AddStopTime(stop118, stop_time='17:57:00') # Sedwikech - 168
trip.AddStopTime(stop119, stop_time='17:58:00') # Dar Echabeb - 45
trip.AddStopTime(stop219, stop_time='17:59:00') # Angar Hmida - 75
trip.AddStopTime(stop218, stop_time='18:00:00') # Krouna - 42
trip.AddStopTime(stop217, stop_time='18:01:00') # Chnib - 54
trip.AddStopTime(stop216, stop_time='18:03:00') # Robana - 101
trip.AddStopTime(stop215, stop_time='18:05:00') # Echhoud - 106
trip.AddStopTime(stop91, stop_time='18:06:00') # Elmaabri - 60
trip.AddStopTime(stop90, stop_time='18:09:00') # Elmay - 157
trip.AddStopTime(stop175, stop_time='18:11:00') # Mosbah - 121
trip.AddStopTime(stop174, stop_time='18:11:00') # Ben Moussa - 26
trip.AddStopTime(stop161, stop_time='18:12:00') # Allamet - 72
trip.AddStopTime(stop160, stop_time='18:13:00') # Bir Ben Amor - 61
trip.AddStopTime(stop159, stop_time='18:15:00') # Omajen 3 - 92
trip.AddStopTime(stop147, stop_time='18:16:00') # Essouani - 83
trip.AddStopTime(stop222, stop_time='18:18:00') # Errahma - 118
trip.AddStopTime(stop221, stop_time='18:19:00') # Lycée Technique - 75
trip.AddStopTime(stop10, stop_time='18:22:00') # Houmet Souk - 159

trip = route.AddTrip(schedule, headsign="Houmet Souk vers Elkantara")
trip.AddStopTime(stop10, stop_time='17:15:00') # Houmet Souk - 0
trip.AddStopTime(stop221, stop_time='17:17:00') # Lycée Technique - 123
trip.AddStopTime(stop222, stop_time='17:18:00') # Errahma - 79
trip.AddStopTime(stop147, stop_time='17:20:00') # Essouani - 118
trip.AddStopTime(stop159, stop_time='17:21:00') # Omajen 3 - 83
trip.AddStopTime(stop160, stop_time='17:23:00') # Bir Ben Amor - 94
trip.AddStopTime(stop161, stop_time='17:24:00') # Allamet - 63
trip.AddStopTime(stop174, stop_time='17:25:00') # Ben Moussa - 72
trip.AddStopTime(stop175, stop_time='17:25:00') # Mosbah - 26
trip.AddStopTime(stop90, stop_time='17:27:00') # Elmay - 145
trip.AddStopTime(stop91, stop_time='17:30:00') # Elmaabri - 165
trip.AddStopTime(stop215, stop_time='17:31:00') # Echhoud - 59
trip.AddStopTime(stop216, stop_time='17:32:00') # Robana - 78
trip.AddStopTime(stop217, stop_time='17:34:00') # Chnib - 108
trip.AddStopTime(stop218, stop_time='17:35:00') # Krouna - 55
trip.AddStopTime(stop219, stop_time='17:36:00') # Angar Hmida - 43
trip.AddStopTime(stop119, stop_time='17:37:00') # Dar Echabeb - 73
trip.AddStopTime(stop118, stop_time='17:38:00') # Sedwikech - 44
trip.AddStopTime(stop143, stop_time='17:41:00') # Oued Ajmi - 177
trip.AddStopTime(stop142, stop_time='17:42:00') # Elmhamid - 35
trip.AddStopTime(stop141, stop_time='17:45:00') # Elkantara - 181

trip = route.AddTrip(schedule, headsign="Elkantara vers Houmet Souk")
trip.AddStopTime(stop141, stop_time='18:45:00') # Elkantara - 0
trip.AddStopTime(stop142, stop_time='18:48:00') # Elmhamid - 187
trip.AddStopTime(stop143, stop_time='18:49:00') # Oued Ajmi - 35
trip.AddStopTime(stop118, stop_time='18:52:00') # Sedwikech - 168
trip.AddStopTime(stop119, stop_time='18:53:00') # Dar Echabeb - 45
trip.AddStopTime(stop219, stop_time='18:54:00') # Angar Hmida - 75
trip.AddStopTime(stop218, stop_time='18:55:00') # Krouna - 42
trip.AddStopTime(stop217, stop_time='18:56:00') # Chnib - 54
trip.AddStopTime(stop216, stop_time='18:58:00') # Robana - 101
trip.AddStopTime(stop215, stop_time='19:00:00') # Echhoud - 106
trip.AddStopTime(stop91, stop_time='19:01:00') # Elmaabri - 60
trip.AddStopTime(stop90, stop_time='19:04:00') # Elmay - 157
trip.AddStopTime(stop175, stop_time='19:06:00') # Mosbah - 121
trip.AddStopTime(stop174, stop_time='19:06:00') # Ben Moussa - 26
trip.AddStopTime(stop161, stop_time='19:07:00') # Allamet - 72
trip.AddStopTime(stop160, stop_time='19:08:00') # Bir Ben Amor - 61
trip.AddStopTime(stop159, stop_time='19:10:00') # Omajen 3 - 92
trip.AddStopTime(stop147, stop_time='19:11:00') # Essouani - 83
trip.AddStopTime(stop222, stop_time='19:13:00') # Errahma - 118
trip.AddStopTime(stop221, stop_time='19:14:00') # Lycée Technique - 75
trip.AddStopTime(stop10, stop_time='19:17:00') # Houmet Souk - 159

trip = route.AddTrip(schedule, headsign="Houmet Souk vers Elkantara")
trip.AddStopTime(stop10, stop_time='18:15:00') # Houmet Souk - 0
trip.AddStopTime(stop221, stop_time='18:17:00') # Lycée Technique - 123
trip.AddStopTime(stop222, stop_time='18:18:00') # Errahma - 79
trip.AddStopTime(stop147, stop_time='18:20:00') # Essouani - 118
trip.AddStopTime(stop159, stop_time='18:21:00') # Omajen 3 - 83
trip.AddStopTime(stop160, stop_time='18:23:00') # Bir Ben Amor - 94
trip.AddStopTime(stop161, stop_time='18:24:00') # Allamet - 63
trip.AddStopTime(stop174, stop_time='18:25:00') # Ben Moussa - 72
trip.AddStopTime(stop175, stop_time='18:25:00') # Mosbah - 26
trip.AddStopTime(stop90, stop_time='18:27:00') # Elmay - 145
trip.AddStopTime(stop91, stop_time='18:30:00') # Elmaabri - 165
trip.AddStopTime(stop215, stop_time='18:31:00') # Echhoud - 59
trip.AddStopTime(stop216, stop_time='18:32:00') # Robana - 78
trip.AddStopTime(stop217, stop_time='18:34:00') # Chnib - 108
trip.AddStopTime(stop218, stop_time='18:35:00') # Krouna - 55
trip.AddStopTime(stop219, stop_time='18:36:00') # Angar Hmida - 43
trip.AddStopTime(stop119, stop_time='18:37:00') # Dar Echabeb - 73
trip.AddStopTime(stop118, stop_time='18:38:00') # Sedwikech - 44
trip.AddStopTime(stop143, stop_time='18:41:00') # Oued Ajmi - 177
trip.AddStopTime(stop142, stop_time='18:42:00') # Elmhamid - 35
trip.AddStopTime(stop141, stop_time='18:45:00') # Elkantara - 181


route = schedule.AddRoute(short_name="SU417", long_name="Houmet Souk, Walagh 2, Gachayin",
                          route_type="Bus")

trip = route.AddTrip(schedule, headsign="Houmet Souk vers Gachayin")
trip.AddStopTime(stop10, stop_time='06:30:00') # Houmet Souk - 0
trip.AddStopTime(stop221, stop_time='06:32:00') # Lycée Technique - 123
trip.AddStopTime(stop147, stop_time='06:35:00') # Essouani - 197
trip.AddStopTime(stop159, stop_time='06:36:00') # Omajen 3 - 83
trip.AddStopTime(stop160, stop_time='06:38:00') # Bir Ben Amor - 94
trip.AddStopTime(stop162, stop_time='06:40:00') # Walagh 1 - 132
trip.AddStopTime(stop163, stop_time='06:41:00') # Walagh 2 - 31
trip.AddStopTime(stop164, stop_time='06:42:00') # Elbkalti - 59
trip.AddStopTime(stop165, stop_time='06:43:00') # Bakir - 72
trip.AddStopTime(stop166, stop_time='06:44:00') # Denguir - 85
trip.AddStopTime(stop169, stop_time='06:46:00') # Mosquet Elyounsi - 94
trip.AddStopTime(stop168, stop_time='06:47:00') # Gachayin - 46
trip.AddStopTime(stop167, stop_time='06:48:00') # Tinisset - 82

trip = route.AddTrip(schedule, headsign="Tinisset vers Houmet Souk")
trip.AddStopTime(stop167, stop_time='6:45:00') # Tinisset - 0
trip.AddStopTime(stop168, stop_time='06:46:00') # Gachayin - 83
trip.AddStopTime(stop169, stop_time='06:47:00') # Mosquet Elyounsi - 46
trip.AddStopTime(stop166, stop_time='06:49:00') # Denguir - 94
trip.AddStopTime(stop165, stop_time='06:50:00') # Bakir - 85
trip.AddStopTime(stop164, stop_time='06:51:00') # Elbkalti - 66
trip.AddStopTime(stop163, stop_time='06:52:00') # Walagh 2 - 60
trip.AddStopTime(stop162, stop_time='06:53:00') # Walagh 1 - 31
trip.AddStopTime(stop160, stop_time='06:55:00') # Bir Ben Amor - 133
trip.AddStopTime(stop159, stop_time='06:57:00') # Omajen 3 - 92
trip.AddStopTime(stop147, stop_time='06:58:00') # Essouani - 83
trip.AddStopTime(stop221, stop_time='07:01:00') # Lycée Technique - 193
trip.AddStopTime(stop10, stop_time='07:04:00') # Houmet Souk - 159


trip = route.AddTrip(schedule, headsign="Houmet Souk vers Gachayin")
trip.AddStopTime(stop10, stop_time='08:15:00') # Houmet Souk - 0
trip.AddStopTime(stop221, stop_time='08:17:00') # Lycée Technique - 123
trip.AddStopTime(stop147, stop_time='08:20:00') # Essouani - 197
trip.AddStopTime(stop159, stop_time='08:21:00') # Omajen 3 - 83
trip.AddStopTime(stop160, stop_time='08:23:00') # Bir Ben Amor - 94
trip.AddStopTime(stop162, stop_time='08:25:00') # Walagh 1 - 132
trip.AddStopTime(stop163, stop_time='08:26:00') # Walagh 2 - 31
trip.AddStopTime(stop164, stop_time='08:27:00') # Elbkalti - 59
trip.AddStopTime(stop165, stop_time='08:28:00') # Bakir - 72
trip.AddStopTime(stop166, stop_time='08:29:00') # Denguir - 85
trip.AddStopTime(stop169, stop_time='08:31:00') # Mosquet Elyounsi - 94
trip.AddStopTime(stop168, stop_time='08:32:00') # Gachayin - 46
trip.AddStopTime(stop167, stop_time='08:33:00') # Tinisset - 82

trip = route.AddTrip(schedule, headsign="Tinisset vers Houmet Souk")
trip.AddStopTime(stop167, stop_time='8:30:00') # Tinisset - 0
trip.AddStopTime(stop168, stop_time='08:31:00') # Gachayin - 83
trip.AddStopTime(stop169, stop_time='08:32:00') # Mosquet Elyounsi - 46
trip.AddStopTime(stop166, stop_time='08:34:00') # Denguir - 94
trip.AddStopTime(stop165, stop_time='08:35:00') # Bakir - 85
trip.AddStopTime(stop164, stop_time='08:36:00') # Elbkalti - 66
trip.AddStopTime(stop163, stop_time='08:37:00') # Walagh 2 - 60
trip.AddStopTime(stop162, stop_time='08:38:00') # Walagh 1 - 31
trip.AddStopTime(stop160, stop_time='08:40:00') # Bir Ben Amor - 133
trip.AddStopTime(stop159, stop_time='08:42:00') # Omajen 3 - 92
trip.AddStopTime(stop147, stop_time='08:43:00') # Essouani - 83
trip.AddStopTime(stop221, stop_time='08:46:00') # Lycée Technique - 193
trip.AddStopTime(stop10, stop_time='08:49:00') # Houmet Souk - 159

trip = route.AddTrip(schedule, headsign="Houmet Souk vers Gachayin")
trip.AddStopTime(stop10, stop_time='12:15:00') # Houmet Souk - 0
trip.AddStopTime(stop221, stop_time='12:17:00') # Lycée Technique - 123
trip.AddStopTime(stop147, stop_time='12:20:00') # Essouani - 197
trip.AddStopTime(stop159, stop_time='12:21:00') # Omajen 3 - 83
trip.AddStopTime(stop160, stop_time='12:23:00') # Bir Ben Amor - 94
trip.AddStopTime(stop162, stop_time='12:25:00') # Walagh 1 - 132
trip.AddStopTime(stop163, stop_time='12:26:00') # Walagh 2 - 31
trip.AddStopTime(stop164, stop_time='12:27:00') # Elbkalti - 59
trip.AddStopTime(stop165, stop_time='12:28:00') # Bakir - 72
trip.AddStopTime(stop166, stop_time='12:29:00') # Denguir - 85
trip.AddStopTime(stop169, stop_time='12:31:00') # Mosquet Elyounsi - 94
trip.AddStopTime(stop168, stop_time='12:32:00') # Gachayin - 46
trip.AddStopTime(stop167, stop_time='12:33:00') # Tinisset - 82

trip = route.AddTrip(schedule, headsign="Tinisset vers Houmet Souk")
trip.AddStopTime(stop167, stop_time='13:10:00') # Tinisset - 0
trip.AddStopTime(stop168, stop_time='13:11:00') # Gachayin - 83
trip.AddStopTime(stop169, stop_time='13:12:00') # Mosquet Elyounsi - 46
trip.AddStopTime(stop166, stop_time='13:14:00') # Denguir - 94
trip.AddStopTime(stop165, stop_time='13:15:00') # Bakir - 85
trip.AddStopTime(stop164, stop_time='13:16:00') # Elbkalti - 66
trip.AddStopTime(stop163, stop_time='13:17:00') # Walagh 2 - 60
trip.AddStopTime(stop162, stop_time='13:18:00') # Walagh 1 - 31
trip.AddStopTime(stop160, stop_time='13:20:00') # Bir Ben Amor - 133
trip.AddStopTime(stop159, stop_time='13:22:00') # Omajen 3 - 92
trip.AddStopTime(stop147, stop_time='13:23:00') # Essouani - 83
trip.AddStopTime(stop221, stop_time='13:26:00') # Lycée Technique - 193
trip.AddStopTime(stop10, stop_time='13:29:00') # Houmet Souk - 159

trip = route.AddTrip(schedule, headsign="Houmet Souk vers Gachayin")
trip.AddStopTime(stop10, stop_time='17:15:00') # Houmet Souk - 0
trip.AddStopTime(stop221, stop_time='17:17:00') # Lycée Technique - 123
trip.AddStopTime(stop147, stop_time='17:20:00') # Essouani - 197
trip.AddStopTime(stop159, stop_time='17:21:00') # Omajen 3 - 83
trip.AddStopTime(stop160, stop_time='17:23:00') # Bir Ben Amor - 94
trip.AddStopTime(stop162, stop_time='17:25:00') # Walagh 1 - 132
trip.AddStopTime(stop163, stop_time='17:26:00') # Walagh 2 - 31
trip.AddStopTime(stop164, stop_time='17:27:00') # Elbkalti - 59
trip.AddStopTime(stop165, stop_time='17:28:00') # Bakir - 72
trip.AddStopTime(stop166, stop_time='17:29:00') # Denguir - 85
trip.AddStopTime(stop169, stop_time='17:31:00') # Mosquet Elyounsi - 94
trip.AddStopTime(stop168, stop_time='17:32:00') # Gachayin - 46
trip.AddStopTime(stop167, stop_time='17:33:00') # Tinisset - 82

trip = route.AddTrip(schedule, headsign="Tinisset vers Houmet Souk")
trip.AddStopTime(stop167, stop_time='17:40:00') # Tinisset - 0
trip.AddStopTime(stop168, stop_time='17:41:00') # Gachayin - 83
trip.AddStopTime(stop169, stop_time='17:42:00') # Mosquet Elyounsi - 46
trip.AddStopTime(stop166, stop_time='17:44:00') # Denguir - 94
trip.AddStopTime(stop165, stop_time='17:45:00') # Bakir - 85
trip.AddStopTime(stop164, stop_time='17:46:00') # Elbkalti - 66
trip.AddStopTime(stop163, stop_time='17:47:00') # Walagh 2 - 60
trip.AddStopTime(stop162, stop_time='17:48:00') # Walagh 1 - 31
trip.AddStopTime(stop160, stop_time='17:50:00') # Bir Ben Amor - 133
trip.AddStopTime(stop159, stop_time='17:52:00') # Omajen 3 - 92
trip.AddStopTime(stop147, stop_time='17:53:00') # Essouani - 83
trip.AddStopTime(stop221, stop_time='17:56:00') # Lycée Technique - 193
trip.AddStopTime(stop10, stop_time='17:59:00') # Houmet Souk - 159

trip = route.AddTrip(schedule, headsign="Houmet Souk vers Gachayin")
trip.AddStopTime(stop10, stop_time='18:15:00') # Houmet Souk - 0
trip.AddStopTime(stop221, stop_time='18:17:00') # Lycée Technique - 123
trip.AddStopTime(stop147, stop_time='18:20:00') # Essouani - 197
trip.AddStopTime(stop159, stop_time='18:21:00') # Omajen 3 - 83
trip.AddStopTime(stop160, stop_time='18:23:00') # Bir Ben Amor - 94
trip.AddStopTime(stop162, stop_time='18:25:00') # Walagh 1 - 132
trip.AddStopTime(stop163, stop_time='18:26:00') # Walagh 2 - 31
trip.AddStopTime(stop164, stop_time='18:27:00') # Elbkalti - 59
trip.AddStopTime(stop165, stop_time='18:28:00') # Bakir - 72
trip.AddStopTime(stop166, stop_time='18:29:00') # Denguir - 85
trip.AddStopTime(stop169, stop_time='18:31:00') # Mosquet Elyounsi - 94
trip.AddStopTime(stop168, stop_time='18:32:00') # Gachayin - 46
trip.AddStopTime(stop167, stop_time='18:33:00') # Tinisset - 82

trip = route.AddTrip(schedule, headsign="Tinisset vers Houmet Souk")
trip.AddStopTime(stop167, stop_time='18:40:00') # Tinisset - 0
trip.AddStopTime(stop168, stop_time='18:41:00') # Gachayin - 83
trip.AddStopTime(stop169, stop_time='18:42:00') # Mosquet Elyounsi - 46
trip.AddStopTime(stop166, stop_time='18:44:00') # Denguir - 94
trip.AddStopTime(stop165, stop_time='18:45:00') # Bakir - 85
trip.AddStopTime(stop164, stop_time='18:46:00') # Elbkalti - 66
trip.AddStopTime(stop163, stop_time='18:47:00') # Walagh 2 - 60
trip.AddStopTime(stop162, stop_time='18:48:00') # Walagh 1 - 31
trip.AddStopTime(stop160, stop_time='18:50:00') # Bir Ben Amor - 133
trip.AddStopTime(stop159, stop_time='18:52:00') # Omajen 3 - 92
trip.AddStopTime(stop147, stop_time='18:53:00') # Essouani - 83
trip.AddStopTime(stop221, stop_time='18:56:00') # Lycée Technique - 193
trip.AddStopTime(stop10, stop_time='18:59:00') # Houmet Souk - 159


route = schedule.AddRoute(short_name="SU418", long_name="Houmet Souk, Erriadh, Oued Ezbib",
                          route_type="Bus")

trip = route.AddTrip(schedule, headsign="Houmet Souk vers Oued Ezbib")
trip.AddStopTime(stop10, stop_time='06:15:00') # Houmet Souk - 0
trip.AddStopTime(stop180, stop_time='06:21:00') # Elbassatin - 330
trip.AddStopTime(stop181, stop_time='06:22:00') # Errahba - 86
trip.AddStopTime(stop182, stop_time='06:23:00') # Ejadoui - 87
trip.AddStopTime(stop183, stop_time='06:25:00') # Elmakbara - 93
trip.AddStopTime(stop179, stop_time='06:27:00') # Erriadh - 101
trip.AddStopTime(stop178, stop_time='06:29:00') # Zenkri - 101
trip.AddStopTime(stop187, stop_time='06:30:00') # Eljenni - 43
trip.AddStopTime(stop188, stop_time='06:31:00') # Ezayat - 60
trip.AddStopTime(stop94, stop_time='06:32:00') # Ben Arbi - 36
trip.AddStopTime(stop93, stop_time='06:33:00') # Allamet Esrandi - 41
trip.AddStopTime(stop96, stop_time='06:34:00') # Mosquet Ellil - 35
trip.AddStopTime(stop97, stop_time='06:35:00') # Ben Terdayet - 46
trip.AddStopTime(stop98, stop_time='06:37:00') # Srendi - 123
trip.AddStopTime(stop100, stop_time='06:41:00') # Oued Ezbib - 210

trip = route.AddTrip(schedule, headsign="Oued Ezbib vers Houmet Souk")
trip.AddStopTime(stop100, stop_time='06:45:00') # Oued Ezbib - 0
trip.AddStopTime(stop98, stop_time='06:49:00') # Srendi - 228
trip.AddStopTime(stop97, stop_time='06:51:00') # Ben Terdayet - 118
trip.AddStopTime(stop96, stop_time='06:52:00') # Mosquet Ellil - 50
trip.AddStopTime(stop93, stop_time='06:53:00') # Allamet Esrandi - 44
trip.AddStopTime(stop94, stop_time='06:54:00') # Ben Arbi - 51
trip.AddStopTime(stop188, stop_time='06:55:00') # Ezayat - 36
trip.AddStopTime(stop187, stop_time='06:56:00') # Eljenni - 55
trip.AddStopTime(stop178, stop_time='06:57:00') # Zenkri - 40
trip.AddStopTime(stop179, stop_time='06:59:00') # Erriadh - 98
trip.AddStopTime(stop183, stop_time='07:01:00') # Elmakbara - 93
trip.AddStopTime(stop182, stop_time='07:02:00') # Ejadoui - 87
trip.AddStopTime(stop181, stop_time='07:04:00') # Errahba - 94
trip.AddStopTime(stop180, stop_time='07:05:00') # Elbassatin - 85
trip.AddStopTime(stop10, stop_time='07:11:00') # Houmet Souk - 338


trip = route.AddTrip(schedule, headsign="Houmet Souk vers Oued Ezbib")
trip.AddStopTime(stop10, stop_time='08:00:00') # Houmet Souk - 0
trip.AddStopTime(stop180, stop_time='08:06:00') # Elbassatin - 330
trip.AddStopTime(stop181, stop_time='08:07:00') # Errahba - 86
trip.AddStopTime(stop182, stop_time='08:08:00') # Ejadoui - 87
trip.AddStopTime(stop183, stop_time='08:10:00') # Elmakbara - 93
trip.AddStopTime(stop179, stop_time='08:12:00') # Erriadh - 101
trip.AddStopTime(stop178, stop_time='08:14:00') # Zenkri - 101
trip.AddStopTime(stop187, stop_time='08:15:00') # Eljenni - 43
trip.AddStopTime(stop188, stop_time='08:16:00') # Ezayat - 60
trip.AddStopTime(stop94, stop_time='08:17:00') # Ben Arbi - 36
trip.AddStopTime(stop93, stop_time='08:18:00') # Allamet Esrandi - 41
trip.AddStopTime(stop96, stop_time='08:19:00') # Mosquet Ellil - 35
trip.AddStopTime(stop97, stop_time='08:20:00') # Ben Terdayet - 46
trip.AddStopTime(stop98, stop_time='08:22:00') # Srendi - 123
trip.AddStopTime(stop100, stop_time='08:26:00') # Oued Ezbib - 210

trip = route.AddTrip(schedule, headsign="Oued Ezbib vers Houmet Souk")
trip.AddStopTime(stop100, stop_time='08:15:00') # Oued Ezbib - 0
trip.AddStopTime(stop98, stop_time='08:19:00') # Srendi - 228
trip.AddStopTime(stop97, stop_time='08:21:00') # Ben Terdayet - 118
trip.AddStopTime(stop96, stop_time='08:22:00') # Mosquet Ellil - 50
trip.AddStopTime(stop93, stop_time='08:23:00') # Allamet Esrandi - 44
trip.AddStopTime(stop94, stop_time='08:24:00') # Ben Arbi - 51
trip.AddStopTime(stop188, stop_time='08:25:00') # Ezayat - 36
trip.AddStopTime(stop187, stop_time='08:26:00') # Eljenni - 55
trip.AddStopTime(stop178, stop_time='08:27:00') # Zenkri - 40
trip.AddStopTime(stop179, stop_time='08:29:00') # Erriadh - 98
trip.AddStopTime(stop183, stop_time='08:31:00') # Elmakbara - 93
trip.AddStopTime(stop182, stop_time='08:32:00') # Ejadoui - 87
trip.AddStopTime(stop181, stop_time='08:34:00') # Errahba - 94
trip.AddStopTime(stop180, stop_time='08:35:00') # Elbassatin - 85
trip.AddStopTime(stop10, stop_time='08:41:00') # Houmet Souk - 338

trip = route.AddTrip(schedule, headsign="Houmet Souk vers Oued Ezbib")
trip.AddStopTime(stop10, stop_time='12:15:00') # Houmet Souk - 0
trip.AddStopTime(stop180, stop_time='12:21:00') # Elbassatin - 330
trip.AddStopTime(stop181, stop_time='12:22:00') # Errahba - 86
trip.AddStopTime(stop182, stop_time='12:23:00') # Ejadoui - 87
trip.AddStopTime(stop183, stop_time='12:25:00') # Elmakbara - 93
trip.AddStopTime(stop179, stop_time='12:27:00') # Erriadh - 101
trip.AddStopTime(stop178, stop_time='12:29:00') # Zenkri - 101
trip.AddStopTime(stop187, stop_time='12:30:00') # Eljenni - 43
trip.AddStopTime(stop188, stop_time='12:31:00') # Ezayat - 60
trip.AddStopTime(stop94, stop_time='12:32:00') # Ben Arbi - 36
trip.AddStopTime(stop93, stop_time='12:33:00') # Allamet Esrandi - 41
trip.AddStopTime(stop96, stop_time='12:34:00') # Mosquet Ellil - 35
trip.AddStopTime(stop97, stop_time='12:35:00') # Ben Terdayet - 46
trip.AddStopTime(stop98, stop_time='12:37:00') # Srendi - 123
trip.AddStopTime(stop100, stop_time='12:41:00') # Oued Ezbib - 210

trip = route.AddTrip(schedule, headsign="Oued Ezbib vers Houmet Souk")
trip.AddStopTime(stop100, stop_time='13:10:00') # Oued Ezbib - 0
trip.AddStopTime(stop98, stop_time='13:14:00') # Srendi - 228
trip.AddStopTime(stop97, stop_time='13:16:00') # Ben Terdayet - 118
trip.AddStopTime(stop96, stop_time='13:17:00') # Mosquet Ellil - 50
trip.AddStopTime(stop93, stop_time='13:18:00') # Allamet Esrandi - 44
trip.AddStopTime(stop94, stop_time='13:19:00') # Ben Arbi - 51
trip.AddStopTime(stop188, stop_time='13:20:00') # Ezayat - 36
trip.AddStopTime(stop187, stop_time='13:21:00') # Eljenni - 55
trip.AddStopTime(stop178, stop_time='13:22:00') # Zenkri - 40
trip.AddStopTime(stop179, stop_time='13:24:00') # Erriadh - 98
trip.AddStopTime(stop183, stop_time='13:26:00') # Elmakbara - 93
trip.AddStopTime(stop182, stop_time='13:27:00') # Ejadoui - 87
trip.AddStopTime(stop181, stop_time='13:29:00') # Errahba - 94
trip.AddStopTime(stop180, stop_time='13:30:00') # Elbassatin - 85
trip.AddStopTime(stop10, stop_time='13:36:00') # Houmet Souk - 338

trip = route.AddTrip(schedule, headsign="Houmet Souk vers Oued Ezbib")
trip.AddStopTime(stop10, stop_time='17:15:00') # Houmet Souk - 0
trip.AddStopTime(stop180, stop_time='17:21:00') # Elbassatin - 330
trip.AddStopTime(stop181, stop_time='17:22:00') # Errahba - 86
trip.AddStopTime(stop182, stop_time='17:23:00') # Ejadoui - 87
trip.AddStopTime(stop183, stop_time='17:25:00') # Elmakbara - 93
trip.AddStopTime(stop179, stop_time='17:27:00') # Erriadh - 101
trip.AddStopTime(stop178, stop_time='17:29:00') # Zenkri - 101
trip.AddStopTime(stop187, stop_time='17:30:00') # Eljenni - 43
trip.AddStopTime(stop188, stop_time='17:31:00') # Ezayat - 60
trip.AddStopTime(stop94, stop_time='17:32:00') # Ben Arbi - 36
trip.AddStopTime(stop93, stop_time='17:33:00') # Allamet Esrandi - 41
trip.AddStopTime(stop96, stop_time='17:34:00') # Mosquet Ellil - 35
trip.AddStopTime(stop97, stop_time='17:35:00') # Ben Terdayet - 46
trip.AddStopTime(stop98, stop_time='17:37:00') # Srendi - 123
trip.AddStopTime(stop100, stop_time='17:41:00') # Oued Ezbib - 210

trip = route.AddTrip(schedule, headsign="Oued Ezbib vers Houmet Souk")
trip.AddStopTime(stop100, stop_time='17:40:00') # Oued Ezbib - 0
trip.AddStopTime(stop98, stop_time='17:44:00') # Srendi - 228
trip.AddStopTime(stop97, stop_time='17:46:00') # Ben Terdayet - 118
trip.AddStopTime(stop96, stop_time='17:47:00') # Mosquet Ellil - 50
trip.AddStopTime(stop93, stop_time='17:48:00') # Allamet Esrandi - 44
trip.AddStopTime(stop94, stop_time='17:49:00') # Ben Arbi - 51
trip.AddStopTime(stop188, stop_time='17:50:00') # Ezayat - 36
trip.AddStopTime(stop187, stop_time='17:51:00') # Eljenni - 55
trip.AddStopTime(stop178, stop_time='17:52:00') # Zenkri - 40
trip.AddStopTime(stop179, stop_time='17:54:00') # Erriadh - 98
trip.AddStopTime(stop183, stop_time='17:56:00') # Elmakbara - 93
trip.AddStopTime(stop182, stop_time='17:57:00') # Ejadoui - 87
trip.AddStopTime(stop181, stop_time='17:59:00') # Errahba - 94
trip.AddStopTime(stop180, stop_time='18:00:00') # Elbassatin - 85
trip.AddStopTime(stop10, stop_time='18:06:00') # Houmet Souk - 338


trip = route.AddTrip(schedule, headsign="Houmet Souk vers Oued Ezbib")
trip.AddStopTime(stop10, stop_time='18:15:00') # Houmet Souk - 0
trip.AddStopTime(stop180, stop_time='18:21:00') # Elbassatin - 330
trip.AddStopTime(stop181, stop_time='18:22:00') # Errahba - 86
trip.AddStopTime(stop182, stop_time='18:23:00') # Ejadoui - 87
trip.AddStopTime(stop183, stop_time='18:25:00') # Elmakbara - 93
trip.AddStopTime(stop179, stop_time='18:27:00') # Erriadh - 101
trip.AddStopTime(stop178, stop_time='18:29:00') # Zenkri - 101
trip.AddStopTime(stop187, stop_time='18:30:00') # Eljenni - 43
trip.AddStopTime(stop188, stop_time='18:31:00') # Ezayat - 60
trip.AddStopTime(stop94, stop_time='18:32:00') # Ben Arbi - 36
trip.AddStopTime(stop93, stop_time='18:33:00') # Allamet Esrandi - 41
trip.AddStopTime(stop96, stop_time='18:34:00') # Mosquet Ellil - 35
trip.AddStopTime(stop97, stop_time='18:35:00') # Ben Terdayet - 46
trip.AddStopTime(stop98, stop_time='18:37:00') # Srendi - 123
trip.AddStopTime(stop100, stop_time='18:41:00') # Oued Ezbib - 210

trip = route.AddTrip(schedule, headsign="Oued Ezbib vers Houmet Souk")
trip.AddStopTime(stop100, stop_time='18:40:00') # Oued Ezbib - 0
trip.AddStopTime(stop98, stop_time='18:44:00') # Srendi - 228
trip.AddStopTime(stop97, stop_time='18:46:00') # Ben Terdayet - 118
trip.AddStopTime(stop96, stop_time='18:47:00') # Mosquet Ellil - 50
trip.AddStopTime(stop93, stop_time='18:48:00') # Allamet Esrandi - 44
trip.AddStopTime(stop94, stop_time='18:49:00') # Ben Arbi - 51
trip.AddStopTime(stop188, stop_time='18:50:00') # Ezayat - 36
trip.AddStopTime(stop187, stop_time='18:51:00') # Eljenni - 55
trip.AddStopTime(stop178, stop_time='18:52:00') # Zenkri - 40
trip.AddStopTime(stop179, stop_time='18:54:00') # Erriadh - 98
trip.AddStopTime(stop183, stop_time='18:56:00') # Elmakbara - 93
trip.AddStopTime(stop182, stop_time='18:57:00') # Ejadoui - 87
trip.AddStopTime(stop181, stop_time='18:59:00') # Errahba - 94
trip.AddStopTime(stop180, stop_time='19:00:00') # Elbassatin - 85
trip.AddStopTime(stop10, stop_time='19:06:00') # Houmet Souk - 338


schedule.Validate()
schedule.WriteGoogleTransitFeed('google_transit.zip')