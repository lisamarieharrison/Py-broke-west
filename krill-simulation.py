import numpy as np
import matplotlib.pyplot as plt


def calc_krill_biomass(survey_area_width, survey_area_length, edsu_width, detected_width):

    n_cells = (survey_area_length/detected_width) * (survey_area_width/edsu_width)
    # edsu = np.zeros(n_cells)
    # for i in range(1, int(n_cells/50)):
    #     segment_choice = np.random.randint(0, 300)
    #     edsu[(i*50-50):(i*50)] = example_p[segment_choice:(segment_choice+50)]
    edsu = np.random.choice(example_p, n_cells)
    edsu.resize(((survey_area_length/detected_width), (survey_area_width/edsu_width)))

    krill_biomass = np.sum(edsu*detected_width*edsu_width)/1e12  # actual biomass in Mt

    calculated_biomass = np.mean(edsu[0])*survey_area_width*survey_area_length/1e12  # in Mt

    return [krill_biomass, calculated_biomass]


n_runs = 200
krill_biomass = np.zeros(n_runs)
calculated_biomass = np.zeros(n_runs)

example_p = np.genfromtxt('C:/Users/Lisa/Documents/phd/southern ocean/BROKE-West/bw_example_p_3.csv', delimiter=',')

for i in range(0, n_runs):
    run_function = calc_krill_biomass(survey_area_width=565e3, survey_area_length=210e3, detected_width=50, edsu_width=2000)
    krill_biomass[i] = run_function[0]
    calculated_biomass[i] = run_function[1]

plt.hist(krill_biomass - calculated_biomass)
plt.show()

print np.mean(krill_biomass) # mean true biomass in Mt

print np.std(krill_biomass - calculated_biomass)/np.mean(krill_biomass) * 100