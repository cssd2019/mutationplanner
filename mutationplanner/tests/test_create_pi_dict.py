import pkg_resources
from mutationplanner.create_pi_dict import create_pi_dict


def test_create_pi_dict():
    expected = {'aaaaaaaa': [- 4.3231, - 5.252],
                'aaaaaaca': [- 3.1298, - 3.5631]
                }
    data_path = pkg_resources.resource_filename('mutationplanner', 'data/test_octamers.txt')
    print(data_path)
    result = create_pi_dict(data_path)
    assert result == expected

def test_path():
    data_path = pkg_resources.resource_filename('mutationplanner', 'data/test_octamers.txt')
    assert data_path == "/Users/adnaniazi/Desktop/collab_workshop/mutationplanner-package/mutationplanner/data/test_octamers.txt"
