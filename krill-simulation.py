import numpy as np
import matplotlib.pyplot as plt

def calc_krill_biomass(survey_area_width, survey_area_length, edsu_width, detected_width):

    n_cells = (survey_area_length/detected_width) * (survey_area_width/edsu_width)
    edsu = np.zeros(n_cells)
    edsu[np.random.choice(range(0, int(n_cells)), size=n_cells*0.95, replace=False)] = np.hstack([np.random.exponential(5, n_cells*0.75), np.random.exponential(100, n_cells*0.2)])
    edsu.resize(((survey_area_length/detected_width), (survey_area_width/edsu_width)))

    krill_biomass = np.sum(edsu*detected_width*edsu_width)/1e12  # actual biomass in Mt

    calculated_biomass = np.mean(edsu[0])*survey_area_width*survey_area_length/1e12  # in Mt

    return [krill_biomass, calculated_biomass]


n_runs = 200
krill_biomass = np.zeros(n_runs)
calculated_biomass = np.zeros(n_runs)
for i in range(0, n_runs):
    run_function = calc_krill_biomass(survey_area_width=565e3, survey_area_length=110e3, detected_width=50, edsu_width=2000)
    krill_biomass[i] = run_function[0]
    calculated_biomass[i] = run_function[1]

plt.hist(krill_biomass - calculated_biomass)
plt.show()

plt.hist(krill_biomass - distribution_biomass)
plt.show()

print np.mean(krill_biomass)