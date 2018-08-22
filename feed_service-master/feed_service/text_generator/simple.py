import os,webbrowser

dir_path = os.path.dirname(os.path.realpath(__file__))
def text_data(downlod_objects):
        path = os.path.join(dir_path + "/climate" + ".txt")
        f= open(path,"w+")
        f.write("UK Maximum Temperature (Degrees C)")
        f.write("\nAreal series, starting from 1910")
        f.write("\nAllowances have been made for topographic, coastal and urban effects where relationships are found to exist.")
        f.write("\nSeasons: Winter=Dec-Feb, Spring=Mar-May, Summer=June-Aug, Autumn=Sept-Nov. (Winter: Year refers to Jan/Feb).")
        f.write("\nMonthly values are ranked and displayed to 1 dp and seasonal/annual values to 2 dp. Where values are equal, rankings are based in order of year descending.Data are provisional from January 2018 and Winter 2018.  Last updated 01/08/2018.")
	f.write("\n\n\n\nYear    JAN    FEB    MAR    APR    MAY    JUN    JUL    AUG    SEP    OCT    NOV    DEC     WIN    SPR    SUM    AUT     ANN")
        for downlod_object in downlod_objects:
            f.write("\n\n\n\n"+str(downlod_object.Year)+"    "+str(downlod_object.Jan)+"    "+str(downlod_object.Feb)+"    "+str(downlod_object.Mar)+"    "+str(downlod_object.Apr)+"    "+str(downlod_object.May)+"    "+str(downlod_object.Jun)+"    "+str(downlod_object.Jul)+"    "+str(downlod_object.Aug)+"    "+str(downlod_object.Sep)+"    "+str(downlod_object.Oct)+"    "+str(downlod_object.Nov)+"    "+str(downlod_object.Dec)+"     "+str(downlod_object.Win)+"    "+str(downlod_object.Spr)+"    "+str(downlod_object.Sum)+"    "+str(downlod_object.Aut)+"     "+str(downlod_object.Ann))
        webbrowser.open('file://' + path)
        return downlod_objects