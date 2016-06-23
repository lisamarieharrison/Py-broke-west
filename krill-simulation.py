import numpy as np
import matplotlib.pyplot as plt
from math import floor


def calc_krill_biomass(survey_area_width, survey_area_length, edsu_width, detected_width, number_of_transects, input_data=None):

    n_cells = (survey_area_length/edsu_width) * (survey_area_width/detected_width)
    if input_data is None:
        edsu = np.random.exponential(2, n_cells)  # random generation from exponential with shape 1.5
    else:
        edsu = np.random.choice(input_data, n_cells)

    edsu.resize(((survey_area_length/edsu_width), (survey_area_width/detected_width)))
    krill_biomass = np.sum(edsu*detected_width*edsu_width)/1e12  # actual biomass in Mt
    calculated_biomass = np.mean(edsu[:, range(0, edsu.shape[1], floor(edsu.shape[1]/number_of_transects))])*survey_area_width*survey_area_length/1e12  # in Mt

    return [krill_biomass, calculated_biomass]


n_runs = 200
krill_biomass = np.zeros(n_runs)
calculated_biomass = np.zeros(n_runs)

example_p = np.genfromtxt('C:/Users/43439535/Documents/Lisa/phd/Mixed models/Data/bw_example_p_3.csv', delimiter=',')

for i in range(0, n_runs):
    run_function = calc_krill_biomass(survey_area_width=565e3, survey_area_length=210e3, detected_width=50, edsu_width=2000, number_of_transects=1)
    krill_biomass[i] = run_function[0]
    calculated_biomass[i] = run_function[1]

plt.hist(krill_biomass - calculated_biomass)
plt.xlabel("True - calculated biomass (Mt) for n = 200 simulations")
plt.ylabel("Frequency")
plt.show()

print("Mean true biomass (Mt) = " + str(round(np.mean(krill_biomass), 2)))  # mean true biomass in Mt
print("Mean difference (Mt) = " + str(round(np.mean(krill_biomass - calculated_biomass), 2)))  # mean true biomass in Mt
print("CV = " + str(round(np.std(krill_biomass - calculated_biomass)/np.mean(krill_biomass), 2)))
