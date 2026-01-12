from library_system.member import Member

def test_member():
    member = Member("User", "M1")
    assert member.member_id == "M1"
