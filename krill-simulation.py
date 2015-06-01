import numpy as np

def calc_krill_biomass(survey_area_width, survey_area_length, edsu_width, detected_width):

    edsu = np.random.exponential(20, n_cells)
    edsu.resize([(survey_area_length/edsu_width), (survey_area_width/detected_width)])

    krill_biomass = np.sum(edsu*detected_width*edsu_width)/1000/1000  # actual biomass in Mt

    calculated_biomass = np.mean(edsu[0])*survey_area_width*survey_area_length/1000/1000  # in Mt

    return [krill_biomass, calculated_biomass]

