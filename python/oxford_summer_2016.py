

eos_public = "root://eospublic.cern.ch/"
amva4np_data = "/eos/experiment/amva4np/data/"
campaign = "oxford_summer_2016/" 
eos_dir = "".join([eos_public,amva4np_data,campaign])
sample_suffix = "_{}_to_{}.root" 

delphes = {}

delphes["QCD_pp_bbbb_13TeV"] = {}

delphes["QCD_pp_bbbb_13TeV"]["dir"] = "".join([
    eos_dir,
    "background/QCD/4b/MG5_pp_bbbb_13TeV_10M/"
])
delphes["QCD_pp_bbbb_13TeV"]["base_name"] = "pp_4b_13TeV_10M_py8"
delphes["QCD_pp_bbbb_13TeV"]["file_name"] = "".join([
    delphes["QCD_pp_bbbb_13TeV"]["dir"],
    "Delphes_output/",
    delphes["QCD_pp_bbbb_13TeV"]["base_name"]+"/",
    delphes["QCD_pp_bbbb_13TeV"]["base_name"]+sample_suffix
])
delphes["QCD_pp_bbbb_13TeV"]["files"] = [
    delphes["QCD_pp_bbbb_13TeV"]["file_name"].format(i*100000,(i+1)*100000) for i in range(100)
]

delphes["pp_hh_bbbb_13TeV"] = {}

delphes["pp_hh_bbbb_13TeV"]["dir"] = "".join([
    eos_dir,
    "signal/non_res_diHiggs/bbbb/"
])
delphes["pp_hh_bbbb_13TeV"]["base_name"] = "MG5_pp_hh_bbbb_13TeV_10M_py8_Forced"
delphes["pp_hh_bbbb_13TeV"]["file_name"] = "".join([
    delphes["pp_hh_bbbb_13TeV"]["dir"],
    "Delphes_output/",
    delphes["pp_hh_bbbb_13TeV"]["base_name"]+"/",
    delphes["pp_hh_bbbb_13TeV"]["base_name"]+sample_suffix
])
delphes["pp_hh_bbbb_13TeV"]["files"] = [
    delphes["pp_hh_bbbb_13TeV"]["file_name"].format(i*100000,(i+1)*100000) for i in range(100)
]

