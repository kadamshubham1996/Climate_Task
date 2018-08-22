


def get_downlod_dict(downlod_object):
    response_dict = { "Region":downlod_object.Region,
                      "Climate_type":downlod_object.Climate_type,
                      "Year":downlod_object.Year,
                      "Jan":downlod_object.Jan,
                      "Feb":downlod_object.Feb,
                      "Mar":downlod_object.Mar,
                      "Apr":downlod_object.Apr,
                      "May":downlod_object.May,
                      "Jun":downlod_object.Jun,
                      "Jul":downlod_object.Jul,
                      "Aug":downlod_object.Aug,
                      "Sep":downlod_object.Sep,
                      "Oct":downlod_object.Oct,
                      "Nov":downlod_object.Nov,
                      "Dec":downlod_object.Dec}
    return response_dict