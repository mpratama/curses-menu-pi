from cursesmenu import CursesMenu
from cursesmenu.items import *
from scriptku import menucurse

#Top Level Menu
toplv_menu = CursesMenu("Menu Raspberry Legend! - written by Pratama", "pilih satu")

#Youtube Menu
yt_menu = CursesMenu("Utility utk download youtube video", "pilih salah satu")

toplv_yt_item = SubmenuItem("Youtube Video Downloader", yt_menu, menu=toplv_menu)
yt1 = FunctionItem("Download single youtube video", menucurse.yt1)
yt_edit_links = FunctionItem("Edit list download", menucurse.yt_edit_links)
yt_bulk = FunctionItem("Bulk download youtube videos", menucurse.yt_bulk)

#Bulk rename menu
bulk_rename_item = FunctionItem("Bulk rename - WARNING(DANGEROUS TOOLS, USE AT YOUR OWN RISK)", menucurse.bulk_rename)

#Top Level Menu Append
toplv_menu.append_item(toplv_yt_item)
toplv_menu.append_item(bulk_rename_item)

#Youtube Menu Append
yt_menu.append_item(yt1)
yt_menu.append_item(yt_edit_links)
yt_menu.append_item(yt_bulk)

#Show the Top Level Menu
toplv_menu.show()
