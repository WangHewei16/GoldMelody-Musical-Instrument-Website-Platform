from models.post import PostModel
from models.auth import UserModel, RoleModel, Permission
from exts import db
import random


# def init_boards():
#     board_names = ['้ข็ด๐น', 'ๅฐๆ็ด๐ป', 'ๅไป๐ธ', 'ๆ้ฃ็ด๐ช', 'ๅถไปไนๅจ']
#     for index, board_name in enumerate(board_names):
#         board = BoardModel(name=board_name, priority=len(board_names)-index)
#         db.session.add(board)
#     db.session.commit()
#     print("ๆฟๅๅๅงๅๆๅ๏ผ")


# 0b001
# 0b010
# 0b011 = ob001 | ob010
# 1|0=1,1|1=1,0|0=0

def init_roles():
    # ่ฟ่ฅ
    operator_role = RoleModel(name="่ฟ่ฅ", desc="่ด่ดฃ็ฎก็ๅธๅญๅ่ฏ่ฎบ",
                         permissions=Permission.POST | Permission.COMMENT | Permission.USER)
    # ็ฎก็ๅ
    admin_role = RoleModel(name="็ฎก็ๅ", desc="่ด่ดฃๆดไธช็ฝ็ซ็็ฎก็",
                      permissions=Permission.POST | Permission.COMMENT | Permission.USER | Permission.STAFF)
    # ๅผๅ่๏ผๆ้ๆฏๆๅคง็๏ผ
    developer_role = RoleModel(name="ๅผๅ่", desc="่ด่ดฃ็ฝ็ซ็ๅผๅ", permissions=Permission.ALL_PERMISSION)

    db.session.add_all([operator_role, admin_role, developer_role])
    db.session.commit()
    print("่ง่ฒๆทปๅ ๆๅ๏ผ")


def init_developor():
    role = RoleModel.query.filter_by(name="ๅผๅ่").first()
    user = UserModel(username="hynever", email="hynever@qq.com", password='111111', is_staff=True, role=role)
    db.session.add(user)
    db.session.commit()
    print('ๅผๅ่่ง่ฒไธ็็จๆทๅๅปบๆๅ๏ผ')


def bind_roles():
    user1 = UserModel.query.filter_by(email="hynever@qq.com").first()
    user2 = UserModel.query.filter_by(email="abc@qq.com").first()
    user3 = UserModel.query.filter_by(email="ccc@qq.com").first()

    role1 = RoleModel.query.filter_by(name="ๅผๅ่").first()
    role2 = RoleModel.query.filter_by(name="่ฟ่ฅ").first()
    role3 = RoleModel.query.filter_by(name="็ฎก็ๅ").first()

    user1.role = role1
    user2.role = role2
    user3.role = role3

    db.session.commit()
    print("็จๆทๅ่ง่ฒ็ปๅฎๆๅ๏ผ")


# def create_test_posts():
#     boards = list(BoardModel.query.all())
#     board_count = len(boards)
#     for x in range(99):
#         title = "ๆๆฏๆ ้ข%d"%x
#         content = "ๆๆฏๅๅฎน%d"%x
#         author = UserModel.query.first()
#         index = random.randint(0, board_count-1)
#         board = boards[index]
#         post_model = PostModel(title=title, content=content, author=author,board=board)
#         db.session.add(post_model)
#     db.session.commit()
#     print("ๆต่ฏๅธๅญๆทปๅ ๆๅ")
