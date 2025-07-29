"""Tests for the activity plot in mibiscreen.visualize module.

@author: Alraune Zech
"""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import pytest
import mibiscreen.data.settings.standard_names as names
from mibiscreen.data.example_data.example_data import example_data
from mibiscreen.visualize.screening_plots import activity_data_prep
from mibiscreen.visualize.screening_plots import activity_plot
from mibiscreen.visualize.screening_plots import contaminants_bar
from mibiscreen.visualize.screening_plots import threshold_ratio_bar


class TestContaminantsBar:
    """Class for testing bar plot of concentrations of mibiscreen."""

    conc_pd = pd.Series(data = [13132.,11695.,4101.,498.,2822],
                        name = names.name_total_contaminants,
                        )

    data = example_data(with_units = False)
    list_contaminants = [names.name_benzene,names.name_toluene,names.name_indane]

    def test_contaminants_bar_01(self):
        """Testing routine contaminants_bar().

        Testing Error message that input data not in required data format.
        """
        with pytest.raises(TypeError):
            contaminants_bar([1,2,3])

    def test_contaminants_bar_02(self):
        """Testing routine contaminants_bar().

        Testing Error message that input data as pd.Series is not enough.
        """
        with pytest.raises(ValueError):
            contaminants_bar(self.conc_pd,[names.name_total_contaminants])

    def test_contaminants_bar_03(self):
        """Testing routine contaminants_bar().

        Testing that routine produces a plot when data is provided as dictionary
        of pca data without dependent variables.
        And standard plot settings.
        """
        fig, ax = contaminants_bar(self.data,
                                   list_contaminants = self.list_contaminants)

        assert isinstance(fig,plt.Figure)
        plt.close(fig)

    def test_contaminants_bar_04(self):
        """Testing routine contaminants_bar().

        Testing that routine produces a plot when data is provided as dictionary
        of pca data without dependent variables.
        And standard plot settings.
        """
        fig, ax = contaminants_bar(self.data,
                                   list_contaminants = self.list_contaminants,
                                   sort = True,
                                   sample_nr = True,
                                   xtick_autorotate = True,
                                   )

        assert isinstance(fig,plt.Figure)
        plt.close(fig)

    def test_contaminants_bar_05(self):
        """Testing routine contaminants_bar().

        Testing keyword list_labels, when not False should be list of
        label names for quantities.
        """
        with pytest.raises(ValueError):
            contaminants_bar(self.data,
                             list_contaminants = self.list_contaminants,
                             list_labels = 'quantity 1',
                             )

    def test_contaminants_bar_06(self):
        """Testing routine contaminants_bar().

        Testing keyword list_labels, when not False should be list of
        label names for quantities.
        """
        with pytest.raises(ValueError):
            contaminants_bar(self.data,
                             list_contaminants = self.list_contaminants,
                             list_labels = ['quantity 1','quantity 2'],
                             )


    def test_contaminants_bar_07(self):
        """Testing routine contaminants_bar().

        Testing keyword list_labels, when not False should be list of
        label names for quantities.
        """
        with pytest.raises(ValueError):
            contaminants_bar(self.data,
                             list_contaminants = self.list_contaminants,
                             list_labels = 'quantity 1',
                             )

    def test_contaminants_bar_08(self):
        """Testing routine contaminants_bar().

        Testing keyword name_sample, when True, the name_sample column
        should be present in the data.
        """
        data_cut = self.data.copy()
        data_cut = data_cut.drop(names.name_sample, axis=1)

        with pytest.raises(ValueError):
            contaminants_bar(data_cut,
                             list_contaminants = self.list_contaminants,
                             name_sample = True,
                             )

    def test_contaminants_bar_09(self,capsys):
        """Testing routine contaminants_bar().

        Testing keyword save_fig. Checks output of Warning that given file path
        does not match for writing figure to file.
        """
        save_fig = '../dir_does_not_exist/file.png'
        out_text = "WARNING: Figure could not be saved. Check provided file path and name: {}\n".format(save_fig)
        contaminants_bar(self.data,
                         self.list_contaminants,
                         save_fig = save_fig)
        out,err=capsys.readouterr()

        assert out==out_text

class TestThresholdRatioBar:
    """Class for testing bar plot of treshold ratios of mibiscreen."""

    df_ratio = pd.DataFrame(data =
                            [[0.0143, 0.0, 	0.007, 0.0],
                            [9, 0.71, 2.26,	21.57],
                            [0.16,0.56, 0.010,2.66],
                            ],
                        columns = ['benzene_thr_ratio','indene_thr_ratio','toluene_thr_ratio','naphthalene_thr_ratio'],
                        )

    list_contaminants = [names.name_benzene,names.name_toluene,names.name_indane]

    def test_threshold_ratio_bar_01(self):
        """Testing routine threshold_ratio_bar().

        Testing that routine produces a plot when data is provided as dictionary
        of data at standard plot settings.
        """
        fig, ax = threshold_ratio_bar(self.df_ratio)

        assert isinstance(fig,plt.Figure)
        plt.close(fig)

    def test_threshold_ratio_bar_02(self):
        """Testing routine threshold_ratio_bar().

        Testing that routine produces a plot when data is provided as dictionary
        of data with specific keyword choices for data preparation.
        """
        fig, ax = threshold_ratio_bar(self.df_ratio,
                                      list_contaminants = ['benzene_thr_ratio','indene_thr_ratio'],
                                      list_samples = [1,2],
                                      )

        assert isinstance(fig,plt.Figure)
        plt.close(fig)

    def test_threshold_ratio_bar_03(self):
        """Testing routine threshold_ratio_bar().

        Testing that routine produces a plot when data is provided as dictionary
        of data with specific keyword choices for data preparation.
        """
        fig, ax = threshold_ratio_bar(self.df_ratio,
                                      list_sort = [3,2,0,1],
                                      nrows = False,
                                      ncols = False,
                                      )

        assert isinstance(fig,plt.Figure)
        plt.close(fig)


    def test_threshold_ratio_bar_04(self):
        """Testing routine threshold_ratio_bar().

        Testing that routine produces a plot when data is provided as dictionary
        of data with specific keyword choices for plot display.
        """
        fig, ax = threshold_ratio_bar(self.df_ratio,
                                      ylabel = 'test_ylabel',
                                      scale = 'log',
                                      unity_line = True,
                                      nrows = False,
                                      ncols = 2,
                                      )

        assert isinstance(fig,plt.Figure)
        plt.close(fig)

    def test_threshold_ratio_bar_05(self):
        """Testing routine threshold_ratio_bar().

        Testing Error message that number of subplot rows/columns does not match
        number of samples to display.
        """
        with pytest.raises(ValueError):
            threshold_ratio_bar(self.df_ratio,
                                ncols = 3,
                                nrows = 2
                                )

    def test_threshold_ratio_bar_06(self):
        """Testing routine threshold_ratio_bar().

        Testing Error message that list of label names for legend too short.
        """
        with pytest.raises(ValueError):
            threshold_ratio_bar(self.df_ratio,
                                list_labels = ['1','2'])


    def test_threshold_ratio_bar_07(self):
        """Testing routine threshold_ratio_bar().

        Testing Error message that list of colors too short.
        """
        with pytest.raises(ValueError):
            threshold_ratio_bar(self.df_ratio,
                                list_colors = ['b','g'])


    def test_threshold_ratio_bar_08(self):
        """Testing routine threshold_ratio_bar().

        Testing Error message that sorting argument not correctly provided.
        """
        with pytest.raises(ValueError):
            threshold_ratio_bar(self.df_ratio,
                                list_sort = [3,2])



    def test_threshold_ratio_bar_09(self,capsys):
       """Testing routine threshold_ratio_bar().

       Testing keyword save_fig. Checks output of Warning that given file path
       does not match for writing figure to file.
       """
       save_fig = '../dir_does_not_exist/file.png'
       out_text = "WARNING: Figure could not be saved. Check provided file path and name: {}\n".format(save_fig)
       threshold_ratio_bar(self.df_ratio,
                           save_fig = save_fig)
       out,err=capsys.readouterr()

       assert out==out_text

class TestActivity:
    """Class for testing activity plot and activity plot prepration of mibiscreen."""

    meta = [41,33,47,20,36]
    conc = [13132.,11695.,4101.,498.,2822]
    traffic = ['red','y','green','green','red']

    meta_pd = pd.Series(data = meta, name = names.name_metabolites_count)
    conc_pd = pd.Series(data = conc, name = names.name_total_contaminants)
    traffic_pd = pd.Series(data = traffic, name = names.name_na_traffic_light)

    data_dict_1 = dict(
        tot_cont = conc_pd,
        meta_count = meta_pd,
        well_color = traffic_pd)

    data_dict_2 = dict(
        tot_cont = np.array(conc),
        meta_count = np.array(meta),
        well_color = np.array(traffic))

    data_dict_3 = dict(
        tot_cont = conc,
        meta_count = meta,
        well_color = traffic)

    def test_activity_data_prep_01(self):
        """Testing routine activity_data_prep().

        Testing that routine produces a dictionary of input data for
        activity plot from DataFrame.

        """
        data_dict = activity_data_prep(pd.concat([self.meta_pd,self.conc_pd,self.traffic_pd],axis = 1))

        assert isinstance(data_dict,dict)


    def test_activity_data_prep_02(self):
        """Testing routine activity_data_prep().

        Testing that routine produces a dictionary of input data for
        activity plot from list of pd.Series provided.

        """
        data_dict = activity_data_prep([self.conc_pd,self.traffic_pd,self.meta_pd])

        assert isinstance(data_dict,dict)

    def test_activity_data_prep_03(self,capsys):
         """Testing routine activity_data_prep().

         Testing that routine produces a dictionary of input data for
         activity plot from list of lists provided.

         Also testing verbosity flag.
         """
         data_dict = activity_data_prep([self.conc,self.traffic,self.meta],verbose=True)
         out,err=capsys.readouterr()

         assert isinstance(data_dict,dict) and len(out)>0

    def test_activity_plot_prep_04(self):
        """Testing routine activity_data_prep().

        Testing Error message that metabolite count data missing.
        """
        with pytest.raises(ValueError):
            activity_data_prep(pd.concat([self.conc_pd,self.traffic_pd],axis = 1))

    def test_activity_plot_prep_05(self):
        """Testing routine activity_data_prep().

        Testing Error message that total contaminants concentration data missing.
        """
        with pytest.raises(ValueError):
            activity_data_prep(pd.concat([self.meta_pd,self.traffic_pd],axis = 1))

    def test_activity_plot_prep_06(self):
        """Testing routine activity_data_prep().

        Testing Error message that NA traffic light data missing.
        """
        with pytest.raises(ValueError):
            activity_data_prep(pd.concat([self.meta_pd,self.conc_pd],axis = 1))


    def test_activity_plot_prep_07(self):
        """Testing routine activity_data_prep().

        Testing Error message that provided lists/arrays of values
        dot no have the same length (are required for plotting).
        """
        with pytest.raises(ValueError):
            activity_data_prep([[1,2,3],[4,5],[6]])

    def test_activity_plot_prep_08(self):
        """Testing routine activity_data_prep().

        Testing Error message that list of pd.series does not contain
        all required quantities.
        """
        test = pd.Series(data = self.traffic, name = 'test')

        with pytest.raises(ValueError):
            activity_data_prep([self.conc_pd,self.traffic_pd,test])


    def test_activity_plot_prep_09(self):
        """Testing routine activity_plot_prep().

        Testing Error message that metabolite count data missing.
        """
        with pytest.raises(ValueError):
            activity_data_prep(['no data',[1,2,2],10.])

    def test_activity_plot_prep_10(self):
        """Testing routine activity_plot_prep().

        Testing Error message that data provided is not in correct format.
        """
        with pytest.raises(ValueError):
            activity_data_prep('no data')

    # data_03 = [np.array(conc),np.array(meta),np.array(traffic)]
    #data_04 = [conc,meta,traffic]


    def test_activity_plot_01(self):
        """Testing routine activity_plot().

        Testing that routine produces a plot when data is provided as dictionary
        of pd.Series.
        """
        fig, ax = activity_plot(self.data_dict_1)

        assert isinstance(fig,plt.Figure)
        plt.close(fig)

    def test_activity_plot_02(self):
        """Testing routine activity_plot().

        Testing that routine produces a plot when data is provided as dictionary
        of np.arrays.
        """
        fig, ax = activity_plot(self.data_dict_2,
                                title_text = 'Activity plot')

        assert isinstance(fig,plt.Figure)
        plt.close(fig)

    def test_activity_plot_03(self):
        """Testing routine activity_plot().

        Testing that routine produces a plot when data is provided as list of lists
        """
        fig, ax = activity_plot(self.data_dict_3)

        assert isinstance(fig,plt.Figure)
        plt.close(fig)


    def test_activity_plot_04(self):
        """Testing routine activity_plot().

        Testing Error message that data is not in required format.
        """
        with pytest.raises(ValueError):
            activity_plot(['test'])

    def test_activity_plot_05(self):
        """Testing routine activity_plot().

        Testing Error message that not sufficient data for a plot.
        """
        data_dict = dict(
            tot_cont = [1],
            meta_count = [2],
            well_color = [3])

        with pytest.raises(ValueError):
            activity_plot(data_dict)

    def test_activity_plot_06(self,capsys):
        """Testing routine activity_plot().

        Testing Error message that given file path does not match for writing
        figure to file.
        """
        save_fig = '../dir_does_not_exist/file.png'
        out_text = "WARNING: Figure could not be saved. Check provided file path and name: {}\n".format(save_fig)
        activity_plot(self.data_dict_1,save_fig = save_fig)
        out,err=capsys.readouterr()

        assert out==out_text

