def proofread(st):
    sentences = st.lower().replace("ie", "ei").split(". ")

    return ". ".join(sentence.capitalize() for sentence in sentences)


# print(proofread("SHe wEnt CaNoIenG."))
# print(proofread("He haD iEght ShOTs of CAffIEne"))
# print(proofread("THe neIghBour's ceiLing FEll on His Head. The WiEght of It crusHed him To thE gROuNd."))
# print(proofread("ThE kiDs enJoYEd the SLiegh RidE."))
# print(proofread("SHE did NOT diegn to GUESS her NIEGHBOUR'S wieght."))
# print(proofread("They had to fIEgn thIEr appreciation for her bIEge tights."))
# print(proofread("Niether of the fencers wanted to forfiet the match. They both expected to sieze victory."))
# print(proofread("Protien intAkE miGHt afFect aNy pOteNtIaL wieght LOSs."))
# print(proofread("MargArEt cAn't eVen concIEve of foRegOing the pARty to finisH her paPEr."))
# print(proofread("IN the wINter, it's NICE to gO for a sliegh rIDe"))
# print(proofread("The mAN's ONly pURpose in lIFe is to decIEve his wIFe."))
# print(proofread("She LifTeD heR ViEL. The ShIeK LooKeD aT hER ExPeCtAnTlY"))
# print(proofread("PetEr Was Not Sure of WHAt he WAs sEIEng. HE had To RIEn in HIs SHock."))
# print(proofread("That is OnE lonG frieghT traiN thAt's Blocking The Railway Crossing."))
# print(proofread(""))
