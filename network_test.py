members = [('pretzel', 7746, 372117617571266561, '143c3b66003752c73162d47aa3032cec', False), ('amy', 4186, 307307235405594625, 'c7a57f9373630b16e031618d261a1912', False), ('Ryno22', 7106, 290995287714168833, '14f23059119befc24fe7ac1986453b6e', False), ('Network Visualizer', 7858, 777435047002767372, 'fa63c5112d99633d569a00b8a6641f9f', True), ('jebramone', 3233, 759152042555605003, '3271cf50bca166765a864e8e067da5b7', False), ('khang nhi', 5694, 243201703044710400, 'd0ba5263e75d30026149af50ef257232', False), ('eunice', 9566, 709872343618420827, 'c6f1e1e4d61d48607ae68de7761ebfa9', False), ('tyler', 9430, 688798838177529880, 'b819117cf3e629e7e1777d185e1fb8ef', False), ('KSM', 1681, 331686449504321556, '8a627a5c414530f375c83cc3ac79b39e', False), ('Shantyman', 8305, 406650046910562305, 'ffd16d66fa2ae7155efbc30be6ecf10b', False), ('Vibe check', 5548, 727683059356532738, 'e1a1835f2038d1a688f263d134d74b04', False), ('estie', 6312, 605891001349046322, '364d7be8306f438cc31c9dd0ba4f89ae', False), ('Nolan', 657, 414691503470804992, '6840b12d3ea85c1446464b0226ffabd4', False), ('Depressobeans', 4340, 422592730598735872, 'c408b575cc4644532e9746a79f95faf9', False), ('Vi-it Ly', 4062, 324360243045728269, 'ce476777dca17f09d4f1a54c4510c942', False), ('x.malaska10', 5671, 333445544024211459, 'c274ab2f0d6aa582c1aa52d0a028ff5e', False), ('ThatAceChaotic', 2345, 290482860991840258, '2ea5a38cdab674b0cbc82468064916e8', False), ('Rythm', 3722, 235088799074484224, '16c197c4c3f0eb808f9bceb6e1075e71', True), ('PluTaniK', 4987, 164598082615508992, '2c1fe3dbbdc18dbf201600b2aebfe81e', False), ('seppy', 5452, 429864500074905601, '8e7d70cf4e5b823ff8720ded62670ea9', False), ('marcocopolo', 3620, 334535898438041600, '8a53767f89049b953ffd8adfc6788393', False), ('M.E.', 8350, 328433751224745985, 'e471fffd60d6422297fd054426928744', False), ('ekam', 4391, 769224915584811028, '3f83be0861c756f36e69dc41aa7125f3', False), ('Chief_Saucin', 7532, 428967503151235074, 'b77b72e0220e4742fa454b654463e768', False), ('TheFlotoOne', 9774, 197807269537120257, '77b14cbb23355be2f1bdc1b87df02a62', False), ('patriciajynne', 8958, 592387887518056496, 'b79ef887039d4e167d8ea2c20214404d', False), ('SoaringFox', 9603, 318759772080046080, 'c54fa3083c75fb7ad7deb678bde95a78', False), ('Bkheang', 836, 318929597699719182, 'edaf2d723b49f52f25acd9ca76bfbcb9', False), ('sebbo', 9348, 482027165509222410, '263a9019921157c361521bb36823d06e', False), ('DeathPanda303', 5544, 140654353722638336, '6d9dcd004a87fd20b99ceef19fdba0ab', False), ('NVTL', 4032, 422125952697368577, 'fe560dc1c3451f94d990f40443bf04bd', False), ('patriciajr', 4166, 768328584468627456, None, False), ('catherine', 15, 400025114386890762, 'c2d0300038cb4ad89ee538e22307a51a', False), ('lewicki', 5532, 247955257122881536, 'f3ea93a05664f6514ee6ac6adcb3584e', False), ('Emily G', 1764, 656821712960356364, 'f819905ea63e0ce9449e38f3fdaab763', False), ('Rou', 843, 187748100473880576, '1231e3a8c12c2e367eda0af7ee757ad6', False), ('enya no. 2', 4137, 769474633233465375, '3f0142f3ba55de862bb4384ae20f33d9', False), ('MEE6', 4876, 159985870458322944, 'b50adff099924dd5e6b72d13f77eb9d7', True), ('Xenarch', 101, 182284531712131072, 'a_ee38050b013ebaec577f5d0a61bbf79c', False), ('ureyfury/imfamassmax', 1327, 363781432243388426, '69a4ca3f26635e9fe1f0118fa756f2d1', False), ('enya', 9247, 535214316895338496, '2bb53d1ac492ea677c434635f82448df', False), ('Groovy', 7254, 234395307759108106, '0e7adc5d634d957b7725021c067bfd87', True), ('AC3FACE', 7854, 193448618957471744, '4a9c556015c3e3e444739f676c33f2ae', False), ('frelee', 9967, 567143550177771543, '01ac9fb4398de40de9ab15001c00cdda', False), ('jackie', 5145, 775568897746141194, None, False), ('Miiyo', 9210, 243287667184238593, '7a41e83069955f20e64fd940197453cb', False), ('blang88', 1988, 719318068219871242, '9d2557b50e6fb20792f28b475c974900', False), ('SmokingSpy', 3839, 249292464744169472, '06c8158f75b831b111d2d12217a01f06', False), ('BelowAverageJoe', 6434, 425814340449337347, '01e3f318149b5b785b39e659ba160fb0', False), ('Nelson', 5113, 689568347129380886, 'e4ee6132142df202f907d0d494399e24', False)]

import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import requests
import numpy as np
from PIL import Image
import os
from io import BytesIO
from tqdm import tqdm
from numpy import sqrt
import random
import matplotlib


name_ind = {}
member_count = 0
bots = []
G = nx.Graph()
imageBaseURL = 'https://cdn.discordapp.com/'

#generate nodes
for ind,(name, disc, id, avatar, bot) in tqdm(enumerate(members)):
    if avatar != None:
        url = f'{imageBaseURL}avatars/{id}/{avatar}.png?size=1024'
        r = requests.get(url, stream=True)
        PFPimg = mpimg.imread(BytesIO(r.content))

    else:
        PFPimg = mpimg.imread('default_avatar.jpg')

    #G.add_node(ind, image=PFPimg, name=name, disc=disc)
    G.add_node(disc, image=PFPimg, name=name)

    #print(nx.get_node_attributes(G,'name')[disc])

    name_ind[name] = ind
    name_ind[ind] = name
    member_count += 1

    if bot:
        bots.append(disc)


#geneate edges
relationshipColorDict = {'Family':'blue', 'SO':'pink', 'Friend':'green'}

#rough draft of discord message inputs

#SmokingSpy,x.malaska10,SO
'''
input_num = int(input('How many inputs?'))

for i in range(input_num):
    edge_input = input('name, name, relationship: ').strip().split(',')
    G.add_edge(name_ind[edge_input[0]], name_ind[edge_input[1]], relationship=relationshipColorDict[edge_input[2]])


'''
for i in range(50):
    #name1 = random.randint(0,member_count-1)
    #name2 = random.randint(0,member_count-1)

    name1 = random.choice(list(G.nodes()))
    name2 = random.choice(list(G.nodes()))

    relationship = random.choice(list(relationshipColorDict.keys()))

    if name1 not in bots and name2 not in bots:
        G.add_edge(name1,name2, relationship=relationship)

# generate graph
pos=nx.kamada_kawai_layout(G)

#matplotlib figure
fig=plt.figure(figsize=(5,5), frameon=False)
ax=plt.subplot(111)
ax.set_aspect('equal')


#Bot Corner
H = G.subgraph(bots)

center = (-0.75,0.75)
side_length = 0.3

bots_pos = nx.circular_layout(H, center = np.array(center), scale=0.1)

for n in G.nodes():
    if n in bots:
        pos[n] = bots_pos[n]

ax.add_patch(matplotlib.patches.Rectangle((center[0]-(side_length/2),center[1]-(side_length/2)),
                                            side_length, side_length, color='grey', alpha=0.5))
font = {'family': 'Roboto Mono',
        'color':  'red',
        'weight': 'bold',
        'size': 20
        }

ax.text(center[0],center[1]+(side_length/2),
        'Bot Corner!', horizontalalignment='center',
        verticalalignment='bottom',
        fontfamily='Lucida Console')

#no go zones
for n in G.nodes():
    if n not in bots:
        bot_zone = (-0.55,0.55)
        legend_zone = (0.41,0.58)
        border_buffer = 0.95
        x,y = pos[n]

        #border patrol
        if x > border_buffer:
            x_dist = abs(x-border_buffer)
            x = x - x_dist

        if x < -border_buffer:
            x_dist = abs(x-border_buffer)
            x = x + x_dist

        if y > border_buffer:
            y_dist = abs(y-border_buffer)
            y = y - y_dist

        if y < -border_buffer:
            y_dist = abs(y-border_buffer)
            y = y + y_dist

        #bot zone
        if x < bot_zone[0] and y > bot_zone[1]:
            #print('Bot Zone: ',n, name_ind[n], pos[n])
            x_dist = abs(x-bot_zone[0])
            y_dist = abs(y-bot_zone[1])

            if x_dist < y_dist:
                x = x + x_dist
            else:
                y = y - y_dist

        #legend zone
        if x > legend_zone[0] and y > legend_zone[1]:
            #print('Legend Zone: ',n, name_ind[n], pos[n])
            x_dist = abs(x-legend_zone[0])
            y_dist = abs(y-legend_zone[1])

            if x_dist < y_dist:
                x = x - x_dist
            else:
                y = y - y_dist

        pos[n] = np.array((x,y))

#plot netowrk edges
edges = G.edges()
colors = [relationshipColorDict[G[u][v]['relationship']] for u,v in edges]
nx.draw_networkx_edges(G,pos,ax=ax, edge_color=colors)
#nx.draw_networkx(G,pos,ax=ax)

#save Graph
df = nx.to_pandas_edgelist(G)
print(df)

#Legend
markers = [plt.Line2D([0,0],[0,0],color=color, marker='o', linestyle='') for color in relationshipColorDict.values()]
plt.legend(markers, relationshipColorDict.keys(), numpoints=1, loc='upper right')

#fuckery to put images on nodes
figlim = 1
plt.xlim(-figlim,figlim)
plt.ylim(-figlim,figlim)

trans = ax.transData.transform
trans2 = fig.transFigure.inverted().transform
imsize = 0.03 # this is the image size
for n in G.nodes():
    (x,y) = pos[n]
    xx,yy = trans((x,y)) # figure coordinates
    xa,ya = trans2((xx,yy)) # axes coordinates
    a = plt.axes([xa-imsize/2.0,ya-imsize/2.0, imsize, imsize])
    a.imshow(G.nodes()[n]['image'])
    a.set_aspect('equal')
    a.axis('off')

ax.axes.xaxis.set_visible(False)
ax.axes.yaxis.set_visible(False)

plt.show()
