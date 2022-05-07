import tkinter as tk
import tkinter.ttk as ttk
from pandas.io import clipboard
from tkinter import IntVar, PhotoImage
from artifact_list import *
class Artifact_GeneratorApp:
    def __init__(self, master=None):
        # build ui
        self.main_window = ttk.Frame(master)
        # mainframe
        self.mainframe = ttk.Labelframe(self.main_window)
        # frame1
        self.frame1 = ttk.Labelframe(self.mainframe)
        self.uid_label = ttk.Label(self.frame1)
        self.uid_label.configure(text="UID : ")
        self.uid_label.grid(column="0", row="0")
        self.uid_entry = ttk.Entry(self.frame1)
        self.uid_entry.grid(column="1", pady="5", row="0")
        self.artifact_label = ttk.Label(self.frame1)
        self.artifact_label.configure(text="Artifact ID : ")
        self.artifact_label.grid(column="0", row="1")
        self.artifact_entry = ttk.Entry(self.frame1)
        self.artifact_entry.grid(column="1", pady="5", row="1")
        self.artifactlevel_label = ttk.Label(self.frame1)
        self.artifactlevel_label.configure(text="Artifact Level :")
        self.artifactlevel_label.grid(column="0", padx="5", pady="5", row="3")
        self.spinbox1 = ttk.Spinbox(self.frame1)
        self.spinbox_defaultvalue = tk.IntVar(value=21)
        self.spinbox1.configure(from_=1, increment=1, textvariable=self.spinbox_defaultvalue, to=21,width="5")
        self.spinbox1.grid(column="1", pady="0", row="3")
        # Switch 1
        self.switch = ttk.Checkbutton(self.frame1)
        self.switchvar = IntVar()
        self.switch.configure(text="More Substat Options", style="Switch.TCheckbutton",variable=self.switchvar ,command=self.switchfunction)
        self.switch.grid(row=4, column=0, padx=5, pady=10, sticky="nsew")
        # Switch 2
        self.switch2 = ttk.Checkbutton(self.frame1)
        self.switchvar2 = IntVar()
        self.switch2.configure(text="Advance Substat Upgrade", style="Switch.TCheckbutton",variable=self.switchvar2 ,command=self.switch2function)
        self.switch2.grid(row=5, column=0, padx=5, pady=10, sticky="nsew")
        # Mainframe config and grid
        self.mainframe.configure(borderwidth="0")
        self.mainframe.grid(column="0",ipadx="0",ipady="0",padx="10",pady="10",row="0",sticky="nw",)
        # frame1 config and grid
        self.frame1.configure(height="200", width="200")
        self.frame1.grid(column="0", ipadx="20", ipady="5", padx="10", pady="10", row="0", sticky="nw")
        # frame2 inside mainframe
        self.frame2 = ttk.Labelframe(self.mainframe)
        self.mainstat_label = ttk.Label(self.frame2)
        self.mainstat_label.configure(text="Main Stat :")
        self.mainstat_label.grid(column="0", padx="10", pady="10", row="0")
        self.mainstat_combobox = ttk.Combobox(self.frame2)
        self.mainstat_combobox.configure(values=main_stat_list, state="readonly")
        self.mainstat_combobox.bind("<<ComboboxSelected>>", lambda _: self.mainstat_combobox.selection_clear())
        self.mainstat_combobox.grid(column="1", row="0")
        self.substat1_label = ttk.Label(self.frame2)
        self.substat1_label.configure(text="Sub Stat #1 :")
        self.substat1_label.grid(column="0", padx="10", pady="10", row="1")
        self.substat1_combobox = ttk.Combobox(self.frame2)
        self.substat1_combobox.configure(values=sub_stat_list, postcommand=self.clear_combobox, state="readonly")
        self.substat1_combobox.bind("<<ComboboxSelected>>", lambda _: self.substat1_combobox.selection_clear())
        self.substat1_combobox.grid(column="1", row="1")
        self.substat2_label = ttk.Label(self.frame2)
        self.substat2_label.configure(text="Sub Stat #2 :")
        self.substat2_label.grid(column="0", padx="10", pady="10", row="2")
        self.substat2_combobox = ttk.Combobox(self.frame2)
        self.substat2_combobox.configure(values=sub_stat_list, postcommand=self.clear_combobox, state="readonly")
        self.substat2_combobox.bind("<<ComboboxSelected>>", lambda _: self.substat2_combobox.selection_clear())
        self.substat2_combobox.grid(column="1", row="2")
        self.substat3_label = ttk.Label(self.frame2)
        self.substat3_label.configure(text="Sub Stat #3 :")
        self.substat3_label.grid(column="0", padx="10", pady="10", row="3")
        self.substat3_combobox = ttk.Combobox(self.frame2)
        self.substat3_combobox.configure(values=sub_stat_list, postcommand=self.clear_combobox, state="readonly")
        self.substat3_combobox.bind("<<ComboboxSelected>>", lambda _: self.substat3_combobox.selection_clear())
        self.substat3_combobox.grid(column="1", row="3")
        self.substat4_label = ttk.Label(self.frame2)
        self.substat4_label.configure(text="Sub Stat #4 :")
        self.substat4_label.grid(column="0", padx="10", pady="10", row="4")
        self.substat4_combobox = ttk.Combobox(self.frame2)
        self.substat4_combobox.configure(values=sub_stat_list, postcommand=self.clear_combobox, state="readonly")
        self.substat4_combobox.bind("<<ComboboxSelected>>", lambda _: self.substat4_combobox.selection_clear())
        self.substat4_combobox.grid(column="1", row="4")
        # Sub Plus Section
        self.subplus1_label = ttk.Label(self.frame2)
        self.subplus1_label.configure(text="Sub Stat +4 :")
        self.subplus1_label.grid(column="2", padx="10", pady="10", row="0")
        self.subplus1_combobox = ttk.Combobox(self.frame2)
        self.subplus1_combobox.configure(values="", postcommand=self.get_substats, state="readonly")
        self.subplus1_combobox.bind("<<ComboboxSelected>>", lambda _: self.subplus1_combobox.selection_clear())
        self.subplus1_combobox.grid(column="3", row="0")
        self.subplus2_label = ttk.Label(self.frame2)
        self.subplus2_label.configure(text="Sub Stat +8 :")
        self.subplus2_label.grid(column="2", padx="10", pady="10", row="1")
        self.subplus2_combobox = ttk.Combobox(self.frame2)
        self.subplus2_combobox.configure(values="", postcommand=self.get_substats, state="readonly")
        self.subplus2_combobox.bind("<<ComboboxSelected>>", lambda _: self.subplus2_combobox.selection_clear())
        self.subplus2_combobox.grid(column="3", row="1")
        self.subplus3_label = ttk.Label(self.frame2)
        self.subplus3_label.configure(text="Sub Stat +12 :")
        self.subplus3_label.grid(column="2", padx="10", pady="10", row="2")
        self.subplus3_combobox = ttk.Combobox(self.frame2)
        self.subplus3_combobox.configure(values="", postcommand=self.get_substats, state="readonly")
        self.subplus3_combobox.bind("<<ComboboxSelected>>", lambda _: self.subplus3_combobox.selection_clear())
        self.subplus3_combobox.grid(column="3", row="2")
        self.subplus4_label = ttk.Label(self.frame2)
        self.subplus4_label.configure(text="Sub Stat +16 :")
        self.subplus4_label.grid(column="2", padx="10", pady="10", row="3")
        self.subplus4_combobox = ttk.Combobox(self.frame2)
        self.subplus4_combobox.configure(values="", postcommand=self.get_substats, state="readonly")
        self.subplus4_combobox.bind("<<ComboboxSelected>>", lambda _: self.subplus4_combobox.selection_clear())
        self.subplus4_combobox.grid(column="3", row="3")
        self.subplus5_label = ttk.Label(self.frame2)
        self.subplus5_label.configure(text="Sub Stat +20 :")
        self.subplus5_label.grid(column="2", padx="10", pady="10", row="4")
        self.subplus5_combobox = ttk.Combobox(self.frame2)
        self.subplus5_combobox.configure(values="", postcommand=self.get_substats, state="readonly")
        self.subplus5_combobox.bind("<<ComboboxSelected>>", lambda _: self.subplus5_combobox.selection_clear())
        self.subplus5_combobox.grid(column="3", row="4")
        # frame2 config and grid
        self.frame2.configure(text="Select Artifact Stats and Upgrades",height="0", width="0")
        self.frame2.grid(column="1",ipadx="20",ipady="5",padx="10", pady="10",row="0",sticky="nw")
        # frame3
        self.frame3 = ttk.Labelframe(self.main_window)
        self.final_result = tk.Text(self.frame3)
        self.final_result.configure(height="1", width="100")
        _text_ = "giveart @[UID]"
        self.final_result.insert("0.0", _text_)
        self.final_result.grid(column="0", padx="5", pady="5", row="0")
        # frame4 inside frame3
        self.frame4 = ttk.Labelframe(self.frame3)
        self.enter_button = ttk.Button(self.frame4)
        self.enter_button.configure(text="Submit")
        self.enter_button.grid(column="0", ipadx="0", ipady="0", padx="5", pady="5", row="0", sticky="nw")
        self.enter_button.configure(command=self.enter_function)
        self.copy_button = ttk.Button(self.frame4)
        self.copy_button.configure(text="Copy Result")
        self.copy_button.grid(
            column="1", ipadx="0", ipady="0", padx="5", pady="5", row="0", sticky="nw"
        )
        self.copy_button.configure(command=self.copy_function)
        self.clear_button = ttk.Button(self.frame4)
        self.clear_button.configure(text="Clear")
        self.clear_button.grid(column="2", ipadx="0", ipady="0", padx="5", pady="5", row="0", sticky="nw")
        self.clear_button.configure(command=self.clear_function)

        # frame3 config and grid
        self.frame3.configure(text="Result",height="200", width="200")
        self.frame3.grid( column="0", ipadx="0",ipady="0",padx="10",pady="0",row="2",sticky="nw")
        # frame4 config and grid
        self.frame4.configure(height="200", width="200")
        self.frame4.grid(column="0", padx="10", pady="10", row="2", sticky="nw")

        # IMPORT IMAGES FOR MAINFRAME2 BUTTONS START
        self.gladiator_flower_img = PhotoImage(file="images/gladiator's finale/1.png").subsample(2, 2)
        self.gladiator_feather_img = PhotoImage(file="images/gladiator's finale/2.png").subsample(2, 2)
        self.gladiator_sands_img = PhotoImage(file="images/gladiator's finale/3.png").subsample(2, 2)
        self.gladiator_goblet_img = PhotoImage(file="images/gladiator's finale/4.png").subsample(2, 2)
        self.gladiator_circlet_img = PhotoImage(file="images/gladiator's finale/5.png").subsample(2, 2)
        self.wanderer_flower_img = PhotoImage(file="images/wanderer's troupe/1.png").subsample(2, 2)
        self.wanderer_feather_img = PhotoImage(file="images/wanderer's troupe/2.png").subsample(2, 2)
        self.wanderer_sands_img = PhotoImage(file="images/wanderer's troupe/3.png").subsample(2, 2)
        self.wanderer_goblet_img = PhotoImage(file="images/wanderer's troupe/4.png").subsample(2, 2)
        self.wanderer_circlet_img = PhotoImage(file="images/wanderer's troupe/5.png").subsample(2, 2)
        self.noblesse_flower_img = PhotoImage(file="images/noblesse oblige/1.png").subsample(2, 2)
        self.noblesse_feather_img = PhotoImage(file="images/noblesse oblige/2.png").subsample(2, 2)
        self.noblesse_sands_img = PhotoImage(file="images/noblesse oblige/3.png").subsample(2, 2)
        self.noblesse_goblet_img = PhotoImage(file="images/noblesse oblige/4.png").subsample(2, 2)
        self.noblesse_circlet_img = PhotoImage(file="images/noblesse oblige/5.png").subsample(2, 2)
        self.chivarly_flower_img = PhotoImage(file="images/bloodstained chivalry/1.png").subsample(2, 2)
        self.chivarly_feather_img = PhotoImage(file="images/bloodstained chivalry/2.png").subsample(2, 2)
        self.chivarly_sands_img = PhotoImage(file="images/bloodstained chivalry/3.png").subsample(2, 2)
        self.chivarly_goblet_img = PhotoImage(file="images/bloodstained chivalry/4.png").subsample(2, 2)
        self.chivarly_circlet_img = PhotoImage(file="images/bloodstained chivalry/5.png").subsample(2, 2)
        self.maiden_flower_img = PhotoImage(file="images/maiden beloved/1.png").subsample(2, 2)
        self.maiden_feather_img = PhotoImage(file="images/maiden beloved/2.png").subsample(2, 2)
        self.maiden_sands_img = PhotoImage(file="images/maiden beloved/3.png").subsample(2, 2)
        self.maiden_goblet_img = PhotoImage(file="images/maiden beloved/4.png").subsample(2, 2)
        self.maiden_circlet_img = PhotoImage(file="images/maiden beloved/5.png").subsample(2, 2)
        self.venerer_flower_img = PhotoImage(file="images/viridescent venerer/1.png").subsample(2, 2)
        self.venerer_feather_img = PhotoImage(file="images/viridescent venerer/2.png").subsample(2, 2)
        self.venerer_sands_img = PhotoImage(file="images/viridescent venerer/3.png").subsample(2, 2)
        self.venerer_goblet_img = PhotoImage(file="images/viridescent venerer/4.png").subsample(2, 2)
        self.venerer_circlet_img = PhotoImage(file="images/viridescent venerer/5.png").subsample(2, 2)
        self.petra_flower_img = PhotoImage(file="images/archaic petra/1.png").subsample(2, 2)
        self.petra_feather_img = PhotoImage(file="images/archaic petra/2.png").subsample(2, 2)
        self.petra_sands_img = PhotoImage(file="images/archaic petra/3.png").subsample(2, 2)
        self.petra_goblet_img = PhotoImage(file="images/archaic petra/4.png").subsample(2, 2)
        self.petra_circlet_img = PhotoImage(file="images/archaic petra/5.png").subsample(2, 2)
        self.bolide_flower_img = PhotoImage(file="images/retracing bolide/1.png").subsample(2, 2)
        self.bolide_feather_img = PhotoImage(file="images/retracing bolide/2.png").subsample(2, 2)
        self.bolide_sands_img = PhotoImage(file="images/retracing bolide/3.png").subsample(2, 2)
        self.bolide_goblet_img = PhotoImage(file="images/retracing bolide/4.png").subsample(2, 2)
        self.bolide_circlet_img = PhotoImage(file="images/retracing bolide/5.png").subsample(2, 2)
        self.thundersoother_flower_img = PhotoImage(file="images/thundersoother/1.png").subsample(2, 2)
        self.thundersoother_feather_img = PhotoImage(file="images/thundersoother/2.png").subsample(2, 2)
        self.thundersoother_sands_img = PhotoImage(file="images/thundersoother/3.png").subsample(2, 2)
        self.thundersoother_goblet_img = PhotoImage(file="images/thundersoother/4.png").subsample(2, 2)
        self.thundersoother_circlet_img = PhotoImage(file="images/thundersoother/5.png").subsample(2, 2)
        self.thundering_flower_img = PhotoImage(file="images/thundering fury/1.png").subsample(2, 2)
        self.thundering_feather_img = PhotoImage(file="images/thundering fury/2.png").subsample(2, 2)
        self.thundering_sands_img = PhotoImage(file="images/thundering fury/3.png").subsample(2, 2)
        self.thundering_goblet_img = PhotoImage(file="images/thundering fury/4.png").subsample(2, 2)
        self.thundering_circlet_img = PhotoImage(file="images/thundering fury/5.png").subsample(2, 2)
        self.lavawalker_flower_img = PhotoImage(file="images/lavawalker/1.png").subsample(2, 2)
        self.lavawalker_feather_img = PhotoImage(file="images/lavawalker/2.png").subsample(2, 2)
        self.lavawalker_sands_img = PhotoImage(file="images/lavawalker/3.png").subsample(2, 2)
        self.lavawalker_goblet_img = PhotoImage(file="images/lavawalker/4.png").subsample(2, 2)
        self.lavawalker_circlet_img = PhotoImage(file="images/lavawalker/5.png").subsample(2, 2)
        self.crimson_flower_img = PhotoImage(file="images/crimson witch of flames/1.png").subsample(2, 2)
        self.crimson_feather_img = PhotoImage(file="images/crimson witch of flames/2.png").subsample(2, 2)
        self.crimson_sands_img = PhotoImage(file="images/crimson witch of flames/3.png").subsample(2, 2)
        self.crimson_goblet_img = PhotoImage(file="images/crimson witch of flames/4.png").subsample(2, 2)
        self.crimson_circlet_img = PhotoImage(file="images/crimson witch of flames/5.png").subsample(2, 2)
        self.blizzard_flower_img = PhotoImage(file="images/blizzard strayer/1.png").subsample(2, 2)
        self.blizzard_feather_img = PhotoImage(file="images/blizzard strayer/2.png").subsample(2, 2)
        self.blizzard_sands_img = PhotoImage(file="images/blizzard strayer/3.png").subsample(2, 2)
        self.blizzard_goblet_img = PhotoImage(file="images/blizzard strayer/4.png").subsample(2, 2)
        self.blizzard_circlet_img = PhotoImage(file="images/blizzard strayer/5.png").subsample(2, 2)
        self.hod_flower_img = PhotoImage(file="images/heart of depth/1.png").subsample(2, 2)
        self.hod_feather_img = PhotoImage(file="images/heart of depth/2.png").subsample(2, 2)
        self.hod_sands_img = PhotoImage(file="images/heart of depth/3.png").subsample(2, 2)
        self.hod_goblet_img = PhotoImage(file="images/heart of depth/4.png").subsample(2, 2)
        self.hod_circlet_img = PhotoImage(file="images/heart of depth/5.png").subsample(2, 2)
        self.tenacity_flower_img = PhotoImage(file="images/tenacity of the millelith/1.png").subsample(2, 2)
        self.tenacity_feather_img = PhotoImage(file="images/tenacity of the millelith/2.png").subsample(2, 2)
        self.tenacity_sands_img = PhotoImage(file="images/tenacity of the millelith/3.png").subsample(2, 2)
        self.tenacity_goblet_img = PhotoImage(file="images/tenacity of the millelith/4.png").subsample(2, 2)
        self.tenacity_circlet_img = PhotoImage(file="images/tenacity of the millelith/5.png").subsample(2, 2)
        self.paleflame_flower_img = PhotoImage(file="images/pale flame/1.png").subsample(2, 2)
        self.paleflame_feather_img = PhotoImage(file="images/pale flame/2.png").subsample(2, 2)
        self.paleflame_sands_img = PhotoImage(file="images/pale flame/3.png").subsample(2, 2)
        self.paleflame_goblet_img = PhotoImage(file="images/pale flame/4.png").subsample(2, 2)
        self.paleflame_circlet_img = PhotoImage(file="images/pale flame/5.png").subsample(2, 2)
        self.shimenawa_flower_img = PhotoImage(file="images/shimenawa's reminiscence/1.png").subsample(2, 2)
        self.shimenawa_feather_img = PhotoImage(file="images/shimenawa's reminiscence/2.png").subsample(2, 2)
        self.shimenawa_sands_img = PhotoImage(file="images/shimenawa's reminiscence/3.png").subsample(2, 2)
        self.shimenawa_goblet_img = PhotoImage(file="images/shimenawa's reminiscence/4.png").subsample(2, 2)
        self.shimenawa_circlet_img = PhotoImage(file="images/shimenawa's reminiscence/5.png").subsample(2, 2)
        self.emblem_flower_img = PhotoImage(file="images/emblem of severed fate/1.png").subsample(2, 2)
        self.emblem_feather_img = PhotoImage(file="images/emblem of severed fate/2.png").subsample(2, 2)
        self.emblem_sands_img = PhotoImage(file="images/emblem of severed fate/3.png").subsample(2, 2)
        self.emblem_goblet_img = PhotoImage(file="images/emblem of severed fate/4.png").subsample(2, 2)
        self.emblem_circlet_img = PhotoImage(file="images/emblem of severed fate/5.png").subsample(2, 2)
        self.husk_flower_img = PhotoImage(file="images/husk of opulent dreams/1.png").subsample(2, 2)
        self.husk_feather_img = PhotoImage(file="images/husk of opulent dreams/2.png").subsample(2, 2)
        self.husk_sands_img = PhotoImage(file="images/husk of opulent dreams/3.png").subsample(2, 2)
        self.husk_goblet_img = PhotoImage(file="images/husk of opulent dreams/4.png").subsample(2, 2)
        self.husk_circlet_img = PhotoImage(file="images/husk of opulent dreams/5.png").subsample(2, 2)
        self.oceanclam_flower_img = PhotoImage(file="images/ocean-hued clam/1.png").subsample(2, 2)
        self.oceanclam_feather_img = PhotoImage(file="images/ocean-hued clam/2.png").subsample(2, 2)
        self.oceanclam_sands_img = PhotoImage(file="images/ocean-hued clam/3.png").subsample(2, 2)
        self.oceanclam_goblet_img = PhotoImage(file="images/ocean-hued clam/4.png").subsample(2, 2)
        self.oceanclam_circlet_img = PhotoImage(file="images/ocean-hued clam/5.png").subsample(2, 2)
        self.vermillion_flower_img = PhotoImage(file="images/vermillion hereafter/1.png").subsample(2, 2)
        self.vermillion_feather_img = PhotoImage(file="images/vermillion hereafter/2.png").subsample(2, 2)
        self.vermillion_sands_img = PhotoImage(file="images/vermillion hereafter/3.png").subsample(2, 2)
        self.vermillion_goblet_img = PhotoImage(file="images/vermillion hereafter/4.png").subsample(2, 2)
        self.vermillion_circlet_img = PhotoImage(file="images/vermillion hereafter/5.png").subsample(2, 2)
        self.echoes_flower_img = PhotoImage(file="images/echoes of an offering/1.png").subsample(2, 2)
        self.echoes_feather_img = PhotoImage(file="images/echoes of an offering/2.png").subsample(2, 2)
        self.echoes_sands_img = PhotoImage(file="images/echoes of an offering/3.png").subsample(2, 2)
        self.echoes_goblet_img = PhotoImage(file="images/echoes of an offering/4.png").subsample(2, 2)
        self.echoes_circlet_img = PhotoImage(file="images/echoes of an offering/5.png").subsample(2, 2)
        # IMPORT IMAGES FOR MAINFRAME2 BUTTONS END

        # MAINFRAME2
        self.mainframe2 = ttk.Labelframe(self.main_window)
        # Gladiator's finale Frame
        self.gladiator_frame = ttk.Labelframe(self.mainframe2)
        self.gladiator_button1 = ttk.Button(self.gladiator_frame)
        self.gladiator_button1.configure(image=self.gladiator_flower_img,command=self.gladiator_click1)
        self.gladiator_button1.grid(column="0", row="0", pady=2, padx=2)
        self.gladiator_button2 = ttk.Button(self.gladiator_frame)
        self.gladiator_button2.configure(image=self.gladiator_feather_img,command=self.gladiator_click2)
        self.gladiator_button2.grid(column="1", row="0", pady=2, padx=2)
        self.gladiator_button3 = ttk.Button(self.gladiator_frame)
        self.gladiator_button3.configure(image=self.gladiator_sands_img,command=self.gladiator_click3)
        self.gladiator_button3.grid(column="2", row="0", pady=2, padx=2)
        self.gladiator_button4 = ttk.Button(self.gladiator_frame)
        self.gladiator_button4.configure(image=self.gladiator_goblet_img,command=self.gladiator_click4)
        self.gladiator_button4.grid(column="3", row="0", pady=2, padx=2)
        self.gladiator_button5 = ttk.Button(self.gladiator_frame)
        self.gladiator_button5.configure(image=self.gladiator_circlet_img,command=self.gladiator_click5)
        self.gladiator_button5.grid(column="4", row="0", pady=2, padx=2)
        self.gladiator_frame.configure(height="200", text="Gladiator's Finale", width="200")
        self.gladiator_frame.grid(column="0", ipadx="5", ipady="5", padx="5", pady="5", row="0")
        # Wanderer's Troupe Frame
        self.wanderer_frame = ttk.Labelframe(self.mainframe2)
        self.wanderer_button1 = ttk.Button(self.wanderer_frame)
        self.wanderer_button1.configure(image=self.wanderer_flower_img,command=self.wanderer_click1)
        self.wanderer_button1.grid(column="0", row="0", pady=2, padx=2)
        self.wanderer_button2 = ttk.Button(self.wanderer_frame)
        self.wanderer_button2.configure(image=self.wanderer_feather_img,command=self.wanderer_click2)
        self.wanderer_button2.grid(column="1", row="0", pady=2, padx=2)
        self.wanderer_button3 = ttk.Button(self.wanderer_frame)
        self.wanderer_button3.configure(image=self.wanderer_sands_img,command=self.wanderer_click3)
        self.wanderer_button3.grid(column="2", row="0", pady=2, padx=2)
        self.wanderer_button4 = ttk.Button(self.wanderer_frame)
        self.wanderer_button4.configure(image=self.wanderer_goblet_img,command=self.wanderer_click4)
        self.wanderer_button4.grid(column="3", row="0", pady=2, padx=2)
        self.wanderer_button5 = ttk.Button(self.wanderer_frame)
        self.wanderer_button5.configure(image=self.wanderer_circlet_img,command=self.wanderer_click5)
        self.wanderer_button5.grid(column="4", row="0", pady=2, padx=2)
        self.wanderer_frame.configure(height="200", text="Wanderer's Troupe", width="200")
        self.wanderer_frame.grid( column="0", ipadx="5", ipady="5", padx="5", pady="5", row="1")
        # Noblesse Oblige Frame
        self.noblesse_frame = ttk.Labelframe(self.mainframe2)
        self.noblesse_button1 = ttk.Button(self.noblesse_frame)
        self.noblesse_button1.configure(image=self.noblesse_flower_img,command=self.noblesse_click1)
        self.noblesse_button1.grid(column="0", padx="2", pady="2", row="0")
        self.noblesse_button2 = ttk.Button(self.noblesse_frame)
        self.noblesse_button2.configure(image=self.noblesse_feather_img,command=self.noblesse_click2)
        self.noblesse_button2.grid(column="1", padx="2", pady="2", row="0")
        self.noblesse_button3 = ttk.Button(self.noblesse_frame)
        self.noblesse_button3.configure(image=self.noblesse_sands_img,command=self.noblesse_click3)
        self.noblesse_button3.grid(column="2", padx="2", pady="2", row="0")
        self.noblesse_button4 = ttk.Button(self.noblesse_frame)
        self.noblesse_button4.configure(image=self.noblesse_goblet_img,command=self.noblesse_click4)
        self.noblesse_button4.grid(column="3", padx="2", pady="2", row="0")
        self.noblesse_button5 = ttk.Button(self.noblesse_frame)
        self.noblesse_button5.configure(image=self.noblesse_circlet_img,command=self.noblesse_click5)
        self.noblesse_button5.grid(column="4", padx="2", pady="2", row="0")
        self.noblesse_frame.configure(height="200", text="Noblesse Oblige", width="200")
        self.noblesse_frame.grid( column="0", ipadx="5", ipady="5", padx="5", pady="5", row="2")
        # Bloodstained Chivalry Frame
        self.chivarly_frame = ttk.Labelframe(self.mainframe2)
        self.chivarly_button1 = ttk.Button(self.chivarly_frame)
        self.chivarly_button1.configure(image=self.chivarly_flower_img,command=self.chivarly_click1)
        self.chivarly_button1.grid(column="0", padx="2", pady="2", row="0")
        self.chivarly_button2 = ttk.Button(self.chivarly_frame)
        self.chivarly_button2.configure(image=self.chivarly_feather_img,command=self.chivarly_click2)
        self.chivarly_button2.grid(column="1", padx="2", pady="2", row="0")
        self.chivarly_button3 = ttk.Button(self.chivarly_frame)
        self.chivarly_button3.configure(image=self.chivarly_sands_img,command=self.chivarly_click3)
        self.chivarly_button3.grid(column="2", padx="2", pady="2", row="0")
        self.chivarly_button4 = ttk.Button(self.chivarly_frame)
        self.chivarly_button4.configure(image=self.chivarly_goblet_img,command=self.chivarly_click4)
        self.chivarly_button4.grid(column="3", padx="2", pady="2", row="0")
        self.chivarly_button5 = ttk.Button(self.chivarly_frame)
        self.chivarly_button5.configure(image=self.chivarly_circlet_img,command=self.chivarly_click5)
        self.chivarly_button5.grid(column="4", padx="2", pady="2", row="0")
        self.chivarly_frame.configure(height="200", text="Bloodstained Chivalry", width="200")
        self.chivarly_frame.grid(column="0", ipadx="5", ipady="5", padx="5", pady="5", row="3")
        # Maiden Beloved Frame
        self.maiden_frame = ttk.Labelframe(self.mainframe2)
        self.maiden_button1 = ttk.Button(self.maiden_frame)
        self.maiden_button1.configure(image=self.maiden_flower_img,command=self.maiden_click1)
        self.maiden_button1.grid(column="0", padx="2", pady="2", row="0")
        self.maiden_button2 = ttk.Button(self.maiden_frame)
        self.maiden_button2.configure(image=self.maiden_feather_img,command=self.maiden_click2)
        self.maiden_button2.grid(column="1", padx="2", pady="2", row="0")
        self.maiden_button3 = ttk.Button(self.maiden_frame)
        self.maiden_button3.configure(image=self.maiden_sands_img,command=self.maiden_click3)
        self.maiden_button3.grid(column="2", padx="2", pady="2", row="0")
        self.maiden_button4 = ttk.Button(self.maiden_frame)
        self.maiden_button4.configure(image=self.maiden_goblet_img,command=self.maiden_click4)
        self.maiden_button4.grid(column="3", padx="2", pady="2", row="0")
        self.maiden_button5 = ttk.Button(self.maiden_frame)
        self.maiden_button5.configure(image=self.maiden_circlet_img,command=self.maiden_click5)
        self.maiden_button5.grid(column="4", padx="2", pady="2", row="0")
        self.maiden_frame.configure(height="200", text="Maiden Beloved", width="200")
        self.maiden_frame.grid(column="0", ipadx="5", ipady="5", padx="5", pady="5", row="4")
        # Viridescent Venerer Frame
        self.venerer_frame = ttk.Labelframe(self.mainframe2)
        self.venerer_button1 = ttk.Button(self.venerer_frame)
        self.venerer_button1.configure(image=self.venerer_flower_img,command=self.venerer_click1)
        self.venerer_button1.grid(column="0", padx="2", pady="2", row="0")
        self.venerer_button2 = ttk.Button(self.venerer_frame)
        self.venerer_button2.configure(image=self.venerer_feather_img,command=self.venerer_click2)
        self.venerer_button2.grid(column="1", padx="2", pady="2", row="0")
        self.venerer_button3 = ttk.Button(self.venerer_frame)
        self.venerer_button3.configure(image=self.venerer_sands_img,command=self.venerer_click3)
        self.venerer_button3.grid(column="2", padx="2", pady="2", row="0")
        self.venerer_button4 = ttk.Button(self.venerer_frame)
        self.venerer_button4.configure(image=self.venerer_goblet_img,command=self.venerer_click4)
        self.venerer_button4.grid(column="3", padx="2", pady="2", row="0")
        self.venerer_button5 = ttk.Button(self.venerer_frame)
        self.venerer_button5.configure(image=self.venerer_circlet_img,command=self.venerer_click5)
        self.venerer_button5.grid(column="4", padx="2", pady="2", row="0")
        self.venerer_frame.configure(height="200", text="Viridescent Venerer", width="200")
        self.venerer_frame.grid(column="1", ipadx="5", ipady="5", padx="5", pady="5", row="0")
        # Archaic Petra Frame
        self.petra_frame = ttk.Labelframe(self.mainframe2)
        self.petra_button1 = ttk.Button(self.petra_frame)
        self.petra_button1.configure(image=self.petra_flower_img,command=self.petra_click1)
        self.petra_button1.grid(column="0", padx="2", pady="2", row="0")
        self.petra_button2 = ttk.Button(self.petra_frame)
        self.petra_button2.configure(image=self.petra_feather_img,command=self.petra_click2)
        self.petra_button2.grid(column="1", padx="2", pady="2", row="0")
        self.petra_button3 = ttk.Button(self.petra_frame)
        self.petra_button3.configure(image=self.petra_sands_img,command=self.petra_click3)
        self.petra_button3.grid(column="2", padx="2", pady="2", row="0")
        self.petra_button4 = ttk.Button(self.petra_frame)
        self.petra_button4.configure(image=self.petra_goblet_img,command=self.petra_click4)
        self.petra_button4.grid(column="3", padx="2", pady="2", row="0")
        self.petra_button5 = ttk.Button(self.petra_frame)
        self.petra_button5.configure(image=self.petra_circlet_img,command=self.petra_click5)
        self.petra_button5.grid(column="4", padx="2", pady="2", row="0")
        self.petra_frame.configure(height="200", text="Archaic Petra", width="200")
        self.petra_frame.grid(column="1", ipadx="5", ipady="5", padx="5", pady="5", row="1")
        # Retracing Bolide Frame
        self.bolide_frame = ttk.Labelframe(self.mainframe2)
        self.bolide_button1 = ttk.Button(self.bolide_frame)
        self.bolide_button1.configure(image=self.bolide_flower_img,command=self.bolide_click1)
        self.bolide_button1.grid(column="0", padx="2", pady="2", row="0")
        self.bolide_button2 = ttk.Button(self.bolide_frame)
        self.bolide_button2.configure(image=self.bolide_feather_img,command=self.bolide_click2)
        self.bolide_button2.grid(column="1", padx="2", pady="2", row="0")
        self.bolide_button3 = ttk.Button(self.bolide_frame)
        self.bolide_button3.configure(image=self.bolide_sands_img,command=self.bolide_click3)
        self.bolide_button3.grid(column="2", padx="2", pady="2", row="0")
        self.bolide_button4 = ttk.Button(self.bolide_frame)
        self.bolide_button4.configure(image=self.bolide_goblet_img,command=self.bolide_click4)
        self.bolide_button4.grid(column="3", padx="2", pady="2", row="0")
        self.bolide_button5 = ttk.Button(self.bolide_frame)
        self.bolide_button5.configure(image=self.bolide_circlet_img,command=self.bolide_click5)
        self.bolide_button5.grid(column="4", padx="2", pady="2", row="0")
        self.bolide_frame.configure(height="200", text="Retracing Bolide", width="200")
        self.bolide_frame.grid(column="1", ipadx="5", ipady="5", padx="5", pady="5", row="2")
        # Thundersoother Frame
        self.thundersoother_frame = ttk.Labelframe(self.mainframe2)
        self.thundersoother_button1 = ttk.Button(self.thundersoother_frame)
        self.thundersoother_button1.configure(image=self.thundersoother_flower_img,command=self.thundersoother_click1)
        self.thundersoother_button1.grid(column="0", padx="2", pady="2", row="0")
        self.thundersoother_button2 = ttk.Button(self.thundersoother_frame)
        self.thundersoother_button2.configure(image=self.thundersoother_feather_img,command=self.thundersoother_click2)
        self.thundersoother_button2.grid(column="1", padx="2", pady="2", row="0")
        self.thundersoother_button3 = ttk.Button(self.thundersoother_frame)
        self.thundersoother_button3.configure(image=self.thundersoother_sands_img,command=self.thundersoother_click3)
        self.thundersoother_button3.grid(column="2", padx="2", pady="2", row="0")
        self.thundersoother_button4 = ttk.Button(self.thundersoother_frame)
        self.thundersoother_button4.configure(image=self.thundersoother_goblet_img,command=self.thundersoother_click4)
        self.thundersoother_button4.grid(column="3", padx="2", pady="2", row="0")
        self.thundersoother_button5 = ttk.Button(self.thundersoother_frame)
        self.thundersoother_button5.configure(image=self.thundersoother_circlet_img,command=self.thundersoother_click5)
        self.thundersoother_button5.grid(column="4", padx="2", pady="2", row="0")
        self.thundersoother_frame.configure(height="200", text="Thundersoother", width="200")
        self.thundersoother_frame.grid(column="1", ipadx="5", ipady="5", padx="5", pady="5", row="3")
        # Thundering Fury Frame
        self.thundering_fury_frame = ttk.Labelframe(self.mainframe2)
        self.thundering_button1 = ttk.Button(self.thundering_fury_frame)
        self.thundering_button1.configure(image=self.thundering_flower_img,command=self.thundering_click1)
        self.thundering_button1.grid(column="0", padx="2", pady="2", row="0")
        self.thundering_button2 = ttk.Button(self.thundering_fury_frame)
        self.thundering_button2.configure(image=self.thundering_feather_img,command=self.thundering_click2)
        self.thundering_button2.grid(column="1", padx="2", pady="2", row="0")
        self.thundering_button3 = ttk.Button(self.thundering_fury_frame)
        self.thundering_button3.configure(image=self.thundering_sands_img,command=self.thundering_click3)
        self.thundering_button3.grid(column="2", padx="2", pady="2", row="0")
        self.thundering_button4 = ttk.Button(self.thundering_fury_frame)
        self.thundering_button4.configure(image=self.thundering_goblet_img,command=self.thundering_click4)
        self.thundering_button4.grid(column="3", padx="2", pady="2", row="0")
        self.thundering_button5 = ttk.Button(self.thundering_fury_frame)
        self.thundering_button5.configure(image=self.thundering_circlet_img,command=self.thundering_click5)
        self.thundering_button5.grid(column="4", padx="2", pady="2", row="0")
        self.thundering_fury_frame.configure(height="200", text="Thundering Fury", width="200")
        self.thundering_fury_frame.grid(column="1", ipadx="5", ipady="5", padx="5", pady="5", row="4")
        # Lava Walker Frame
        self.lavawalker_frame = ttk.Labelframe(self.mainframe2)
        self.lavawalker_button1 = ttk.Button(self.lavawalker_frame)
        self.lavawalker_button1.configure(image=self.lavawalker_flower_img,command=self.lavawalker_click1)
        self.lavawalker_button1.grid(column="0", padx="2", pady="2", row="0")
        self.lavawalker_button2 = ttk.Button(self.lavawalker_frame)
        self.lavawalker_button2.configure(image=self.lavawalker_feather_img,command=self.lavawalker_click2)
        self.lavawalker_button2.grid(column="1", padx="2", pady="2", row="0")
        self.lavawalker_button3 = ttk.Button(self.lavawalker_frame)
        self.lavawalker_button3.configure(image=self.lavawalker_sands_img,command=self.lavawalker_click3)
        self.lavawalker_button3.grid(column="2", padx="2", pady="2", row="0")
        self.lavawalker_button4 = ttk.Button(self.lavawalker_frame)
        self.lavawalker_button4.configure(image=self.lavawalker_goblet_img,command=self.lavawalker_click4)
        self.lavawalker_button4.grid(column="3", padx="2", pady="2", row="0")
        self.lavawalker_button5 = ttk.Button(self.lavawalker_frame)
        self.lavawalker_button5.configure(image=self.lavawalker_circlet_img,command=self.lavawalker_click5)
        self.lavawalker_button5.grid(column="4", padx="2", pady="2", row="0")
        self.lavawalker_frame.configure(height="200", text="Lavawalker", width="200")
        self.lavawalker_frame.grid(column="2", ipadx="5", ipady="5", padx="5", pady="5", row="0")
        # Crimson Witch of Flames Frame
        self.crimson_witch_frame = ttk.Labelframe(self.mainframe2)
        self.crimson_button1 = ttk.Button(self.crimson_witch_frame)
        self.crimson_button1.configure(image=self.crimson_flower_img,command=self.crimson_click1)
        self.crimson_button1.grid(column="0", padx="2", pady="2", row="0")
        self.crimson_button2 = ttk.Button(self.crimson_witch_frame)
        self.crimson_button2.configure(image=self.crimson_feather_img,command=self.crimson_click2)
        self.crimson_button2.grid(column="1", padx="2", pady="2", row="0")
        self.crimson_button3 = ttk.Button(self.crimson_witch_frame)
        self.crimson_button3.configure(image=self.crimson_sands_img,command=self.crimson_click3)
        self.crimson_button3.grid(column="2", padx="2", pady="2", row="0")
        self.crimson_button4 = ttk.Button(self.crimson_witch_frame)
        self.crimson_button4.configure(image=self.crimson_goblet_img,command=self.crimson_click4)
        self.crimson_button4.grid(column="3", padx="2", pady="2", row="0")
        self.crimson_button5 = ttk.Button(self.crimson_witch_frame)
        self.crimson_button5.configure(image=self.crimson_circlet_img,command=self.crimson_click5)
        self.crimson_button5.grid(column="4", padx="2", pady="2", row="0")
        self.crimson_witch_frame.configure(height="200", text="Crimson Witch of Flames", width="200")
        self.crimson_witch_frame.grid(column="2", ipadx="5", ipady="5", padx="5", pady="5", row="1")
        # Blizzard Strayer Frame
        self.blizzard_frame = ttk.Labelframe(self.mainframe2)
        self.blizzard_button1 = ttk.Button(self.blizzard_frame)
        self.blizzard_button1.configure(image=self.blizzard_flower_img,command=self.blizzard_click1)
        self.blizzard_button1.grid(column="0", padx="2", pady="2", row="0")
        self.blizzard_button2 = ttk.Button(self.blizzard_frame)
        self.blizzard_button2.configure(image=self.blizzard_feather_img,command=self.blizzard_click2)
        self.blizzard_button2.grid(column="1", padx="2", pady="2", row="0")
        self.blizzard_button3 = ttk.Button(self.blizzard_frame)
        self.blizzard_button3.configure(image=self.blizzard_sands_img,command=self.blizzard_click3)
        self.blizzard_button3.grid(column="2", padx="2", pady="2", row="0")
        self.blizzard_button4 = ttk.Button(self.blizzard_frame)
        self.blizzard_button4.configure(image=self.blizzard_goblet_img,command=self.blizzard_click4)
        self.blizzard_button4.grid(column="3", padx="2", pady="2", row="0")
        self.blizzard_button5 = ttk.Button(self.blizzard_frame)
        self.blizzard_button5.configure(image=self.blizzard_circlet_img,command=self.blizzard_click5)
        self.blizzard_button5.grid(column="4", padx="2", pady="2", row="0")
        self.blizzard_frame.configure(height="200", text="Blizzard Strayer", width="200")
        self.blizzard_frame.grid(column="2", ipadx="5", ipady="5", padx="5", pady="5", row="2")
        # Heart of Depth Frame
        self.heart_of_depth_frame = ttk.Labelframe(self.mainframe2)
        self.hod_button1 = ttk.Button(self.heart_of_depth_frame)
        self.hod_button1.configure(image=self.hod_flower_img,command=self.hod_click1)
        self.hod_button1.grid(column="0", padx="2", pady="2", row="0")
        self.hod_button2 = ttk.Button(self.heart_of_depth_frame)
        self.hod_button2.configure(image=self.hod_feather_img,command=self.hod_click2)
        self.hod_button2.grid(column="1", padx="2", pady="2", row="0")
        self.hod_button3 = ttk.Button(self.heart_of_depth_frame)
        self.hod_button3.configure(image=self.hod_sands_img,command=self.hod_click3)
        self.hod_button3.grid(column="2", padx="2", pady="2", row="0")
        self.hod_button4 = ttk.Button(self.heart_of_depth_frame)
        self.hod_button4.configure(image=self.hod_goblet_img,command=self.hod_click4)
        self.hod_button4.grid(column="3", padx="2", pady="2", row="0")
        self.hod_button5 = ttk.Button(self.heart_of_depth_frame)
        self.hod_button5.configure(image=self.hod_circlet_img,command=self.hod_click5)
        self.hod_button5.grid(column="4", padx="2", pady="2", row="0")
        self.heart_of_depth_frame.configure(height="200", text="Heart of Depth", width="200")
        self.heart_of_depth_frame.grid(column="2", ipadx="5", ipady="5", padx="5", pady="5", row="3")
        # Tenacity of the Millelith Frame
        self.tenacity_frame = ttk.Labelframe(self.mainframe2)
        self.tenacity_button1 = ttk.Button(self.tenacity_frame)
        self.tenacity_button1.configure(image=self.tenacity_flower_img,command=self.tenacity_click1)
        self.tenacity_button1.grid(column="0", padx="2", pady="2", row="0")
        self.tenacity_button2 = ttk.Button(self.tenacity_frame)
        self.tenacity_button2.configure(image=self.tenacity_feather_img,command=self.tenacity_click2)
        self.tenacity_button2.grid(column="1", padx="2", pady="2", row="0")
        self.tenacity_button3 = ttk.Button(self.tenacity_frame)
        self.tenacity_button3.configure(image=self.tenacity_sands_img,command=self.tenacity_click3)
        self.tenacity_button3.grid(column="2", padx="2", pady="2", row="0")
        self.tenacity_button4 = ttk.Button(self.tenacity_frame)
        self.tenacity_button4.configure(image=self.tenacity_goblet_img,command=self.tenacity_click4)
        self.tenacity_button4.grid(column="3", padx="2", pady="2", row="0")
        self.tenacity_button5 = ttk.Button(self.tenacity_frame)
        self.tenacity_button5.configure(image=self.tenacity_circlet_img,command=self.tenacity_click5)
        self.tenacity_button5.grid(column="4", padx="2", pady="2", row="0")
        self.tenacity_frame.configure(height="200", text="Tenacity of the Millelith", width="200")
        self.tenacity_frame.grid(column="2", ipadx="5", ipady="5", padx="5", pady="5", row="4")
        # Pale Flame Frame
        self.pale_flame_frame = ttk.Labelframe(self.mainframe2)
        self.pale_flame_button1 = ttk.Button(self.pale_flame_frame)
        self.pale_flame_button1.configure(image=self.paleflame_flower_img,command=self.paleflame_click1)
        self.pale_flame_button1.grid(column="0", padx="2", pady="2", row="0")
        self.pale_flame_button2 = ttk.Button(self.pale_flame_frame)
        self.pale_flame_button2.configure(image=self.paleflame_feather_img,command=self.paleflame_click2)
        self.pale_flame_button2.grid(column="1", padx="2", pady="2", row="0")
        self.pale_flame_button3 = ttk.Button(self.pale_flame_frame)
        self.pale_flame_button3.configure(image=self.paleflame_sands_img,command=self.paleflame_click3)
        self.pale_flame_button3.grid(column="2", padx="2", pady="2", row="0")
        self.pale_flame_button4 = ttk.Button(self.pale_flame_frame)
        self.pale_flame_button4.configure(image=self.paleflame_goblet_img,command=self.paleflame_click4)
        self.pale_flame_button4.grid(column="3", padx="2", pady="2", row="0")
        self.pale_flame_button5 = ttk.Button(self.pale_flame_frame)
        self.pale_flame_button5.configure(image=self.paleflame_circlet_img,command=self.paleflame_click5)
        self.pale_flame_button5.grid(column="4", padx="2", pady="2", row="0")
        self.pale_flame_frame.configure(height="200", text="Pale Flame", width="200")
        self.pale_flame_frame.grid(column="3", ipadx="5", ipady="5", padx="5", pady="5", row="0")
        # Shimenawa's Reminiscence Frame
        self.shimenawa_frame = ttk.Labelframe(self.mainframe2)
        self.shimenawa_button1 = ttk.Button(self.shimenawa_frame)
        self.shimenawa_button1.configure(image=self.shimenawa_flower_img,command=self.shimenawa_click1)
        self.shimenawa_button1.grid(column="0", padx="2", pady="2", row="0")
        self.shimenawa_button2 = ttk.Button(self.shimenawa_frame)
        self.shimenawa_button2.configure(image=self.shimenawa_feather_img,command=self.shimenawa_click2)
        self.shimenawa_button2.grid(column="1", padx="2", pady="2", row="0")
        self.shimenawa_button3 = ttk.Button(self.shimenawa_frame)
        self.shimenawa_button3.configure(image=self.shimenawa_sands_img,command=self.shimenawa_click3)
        self.shimenawa_button3.grid(column="2", padx="2", pady="2", row="0")
        self.shimenawa_button4 = ttk.Button(self.shimenawa_frame)
        self.shimenawa_button4.configure(image=self.shimenawa_goblet_img,command=self.shimenawa_click4)
        self.shimenawa_button4.grid(column="3", padx="2", pady="2", row="0")
        self.shimenawa_button5 = ttk.Button(self.shimenawa_frame)
        self.shimenawa_button5.configure(image=self.shimenawa_circlet_img,command=self.shimenawa_click5)
        self.shimenawa_button5.grid(column="4", padx="2", pady="2", row="0")
        self.shimenawa_frame.configure(height="200", text="Shimenawas Reminiscence", width="200")
        self.shimenawa_frame.grid(column="3", ipadx="5", ipady="5", padx="5", pady="5", row="1")
        # Emblem of Severed Fate Frame
        self.emblem_frame = ttk.Labelframe(self.mainframe2)
        self.emblem_button1 = ttk.Button(self.emblem_frame)
        self.emblem_button1.configure(image=self.emblem_flower_img,command=self.emblem_click1)
        self.emblem_button1.grid(column="0", padx="2", pady="2", row="0")
        self.emblem_button2 = ttk.Button(self.emblem_frame)
        self.emblem_button2.configure(image=self.emblem_feather_img,command=self.emblem_click2)
        self.emblem_button2.grid(column="1", padx="2", pady="2", row="0")
        self.emblem_button3 = ttk.Button(self.emblem_frame)
        self.emblem_button3.configure(image=self.emblem_sands_img,command=self.emblem_click3)
        self.emblem_button3.grid(column="2", padx="2", pady="2", row="0")
        self.emblem_button4 = ttk.Button(self.emblem_frame)
        self.emblem_button4.configure(image=self.emblem_goblet_img,command=self.emblem_click4)
        self.emblem_button4.grid(column="3", padx="2", pady="2", row="0")
        self.emblem_button5 = ttk.Button(self.emblem_frame)
        self.emblem_button5.configure(image=self.emblem_circlet_img,command=self.emblem_click5)
        self.emblem_button5.grid(column="4", padx="2", pady="2", row="0")
        self.emblem_frame.configure(height="200", text="Emblem of Severed Fate", width="200")
        self.emblem_frame.grid(column="3", ipadx="5", ipady="5", padx="5", pady="5", row="2")
        # Husk of Opulent Dreams Frame
        self.husk_frame = ttk.Labelframe(self.mainframe2)
        self.husk_button1 = ttk.Button(self.husk_frame)
        self.husk_button1.configure(image=self.husk_flower_img,command=self.husk_click1)
        self.husk_button1.grid(column="0", padx="2", pady="2", row="0")
        self.husk_button2 = ttk.Button(self.husk_frame)
        self.husk_button2.configure(image=self.husk_feather_img,command=self.husk_click2)
        self.husk_button2.grid(column="1", padx="2", pady="2", row="0")
        self.husk_button3 = ttk.Button(self.husk_frame)
        self.husk_button3.configure(image=self.husk_sands_img,command=self.husk_click3)
        self.husk_button3.grid(column="2", padx="2", pady="2", row="0")
        self.husk_button4 = ttk.Button(self.husk_frame)
        self.husk_button4.configure(image=self.husk_goblet_img,command=self.husk_click4)
        self.husk_button4.grid(column="3", padx="2", pady="2", row="0")
        self.husk_button5 = ttk.Button(self.husk_frame)
        self.husk_button5.configure(image=self.husk_circlet_img,command=self.husk_click5)
        self.husk_button5.grid(column="4", padx="2", pady="2", row="0")
        self.husk_frame.configure(height="200", text="Husk of Opulent Dreams", width="200")
        self.husk_frame.grid(column="3", ipadx="5", ipady="5", padx="5", pady="5", row="3")
        # Ocean-Hued Clam Frame
        self.ocean_clam_frame = ttk.Labelframe(self.mainframe2)
        self.ocean_clam_button1 = ttk.Button(self.ocean_clam_frame)
        self.ocean_clam_button1.configure(image=self.oceanclam_flower_img,command=self.oceanclam_click1)
        self.ocean_clam_button1.grid(column="0", padx="2", pady="2", row="0")
        self.ocean_clam_button2 = ttk.Button(self.ocean_clam_frame)
        self.ocean_clam_button2.configure(image=self.oceanclam_feather_img,command=self.oceanclam_click2)
        self.ocean_clam_button2.grid(column="1", padx="2", pady="2", row="0")
        self.ocean_clam_button3 = ttk.Button(self.ocean_clam_frame)
        self.ocean_clam_button3.configure(image=self.oceanclam_sands_img,command=self.oceanclam_click3)
        self.ocean_clam_button3.grid(column="2", padx="2", pady="2", row="0")
        self.ocean_clam_button4 = ttk.Button(self.ocean_clam_frame)
        self.ocean_clam_button4.configure(image=self.oceanclam_goblet_img,command=self.oceanclam_click4)
        self.ocean_clam_button4.grid(column="3", padx="2", pady="2", row="0")
        self.ocean_clam_button5 = ttk.Button(self.ocean_clam_frame)
        self.ocean_clam_button5.configure(image=self.oceanclam_circlet_img,command=self.oceanclam_click5)
        self.ocean_clam_button5.grid(column="4", padx="2", pady="2", row="0")
        self.ocean_clam_frame.configure(height="200", text="Ocean-Hued Clam", width="200")
        self.ocean_clam_frame.grid(column="3", ipadx="5", ipady="5", padx="5", pady="5", row="4")
        # Vermillion Hereafter Frame
        self.vermillion_frame = ttk.Labelframe(self.mainframe2)
        self.vermillion_button1 = ttk.Button(self.vermillion_frame)
        self.vermillion_button1.configure(image=self.vermillion_flower_img,command=self.vermillion_click1)
        self.vermillion_button1.grid(column="0", padx="2", pady="2", row="0")
        self.vermillion_button2 = ttk.Button(self.vermillion_frame)
        self.vermillion_button2.configure(image=self.vermillion_feather_img,command=self.vermillion_click2)
        self.vermillion_button2.grid(column="1", padx="2", pady="2", row="0")
        self.vermillion_button3 = ttk.Button(self.vermillion_frame)
        self.vermillion_button3.configure(image=self.vermillion_sands_img,command=self.vermillion_click3)
        self.vermillion_button3.grid(column="2", padx="2", pady="2", row="0")
        self.vermillion_button4 = ttk.Button(self.vermillion_frame)
        self.vermillion_button4.configure(image=self.vermillion_goblet_img,command=self.vermillion_click4)
        self.vermillion_button4.grid(column="3", padx="2", pady="2", row="0")
        self.vermillion_button5 = ttk.Button(self.vermillion_frame)
        self.vermillion_button5.configure(image=self.vermillion_circlet_img,command=self.vermillion_click5)
        self.vermillion_button5.grid(column="4", padx="2", pady="2", row="0")
        self.vermillion_frame.configure(height="200", text="Vermillion Hereafter", width="200")
        self.vermillion_frame.grid(column="1", ipadx="5", ipady="5", padx="5", pady="5", row="5")
        # Echoes of an Offering Frame
        self.echoes_offering_frame = ttk.Labelframe(self.mainframe2)
        self.echoes_button1 = ttk.Button(self.echoes_offering_frame)
        self.echoes_button1.configure(image=self.echoes_flower_img,command=self.echoes_click1)
        self.echoes_button1.grid(column="0", padx="2", pady="2", row="0")
        self.echoes_button2 = ttk.Button(self.echoes_offering_frame)
        self.echoes_button2.configure(image=self.echoes_feather_img,command=self.echoes_click2)
        self.echoes_button2.grid(column="1", padx="2", pady="2", row="0")
        self.echoes_button3 = ttk.Button(self.echoes_offering_frame)
        self.echoes_button3.configure(image=self.echoes_sands_img,command=self.echoes_click3)
        self.echoes_button3.grid(column="2", padx="2", pady="2", row="0")
        self.echoes_button4 = ttk.Button(self.echoes_offering_frame)
        self.echoes_button4.configure(image=self.echoes_goblet_img,command=self.echoes_click4)
        self.echoes_button4.grid(column="3", padx="2", pady="2", row="0")
        self.echoes_button5 = ttk.Button(self.echoes_offering_frame)
        self.echoes_button5.configure(image=self.echoes_circlet_img,command=self.echoes_click5)
        self.echoes_button5.grid(column="4", padx="2", pady="2", row="0")
        self.echoes_offering_frame.configure(height="200", text="Echoes of an Offering", width="200")
        self.echoes_offering_frame.grid(column="2", ipadx="5", ipady="5", padx="5", pady="5", row="5")

        # Mainframe2 config and grid
        self.mainframe2.configure(height="200", text="Select Artifact", width="200")
        self.mainframe2.grid(column="0", padx="10", pady="10", row="4", sticky="nw")
        # MAINFRAME2 END
        # main_window config and grid
        self.main_window.configure(height="600", width="600")
        self.main_window.grid(column="0", row="0")
        # Main widget
        self.mainwindow = self.main_window

    def run(self):
        self.mainwindow.mainloop()

    def enter_function(self):
        listvar = [
            str(self.mainstat_combobox.get()),
            str(self.substat1_combobox.get()),
            str(self.substat2_combobox.get()),
            str(self.substat3_combobox.get()),
            str(self.substat4_combobox.get()),
            str(self.subplus1_combobox.get()),
            str(self.subplus2_combobox.get()),
            str(self.subplus3_combobox.get()),
            str(self.subplus4_combobox.get()),
            str(self.subplus5_combobox.get()),
        ]
        stats_final_translation = ""
        for line in listvar:
            line = line.rstrip()
            if not line:
                continue
            for stat_name, stat_id in stat_translation.items():
                if stat_name in line:
                    line = line.replace(stat_name, str(stat_id))
                    stats_final_translation = stats_final_translation + " " + line
        final_command_result = f"giveart @{self.uid_entry.get()} {self.artifact_entry.get()}{stats_final_translation} {self.spinbox1.get()}"
        self.final_result.delete("1.0","end")
        self.final_result.insert("0.0",final_command_result)

    def clear_function(self):
        self.artifact_entry.delete(0,'end')
        self.mainstat_combobox.set("")
        self.substat1_combobox.set("")
        self.substat2_combobox.set("")
        self.substat3_combobox.set("")
        self.substat4_combobox.set("")
        self.subplus1_combobox.set("")
        self.subplus2_combobox.set("")
        self.subplus3_combobox.set("")
        self.subplus4_combobox.set("")
        self.subplus5_combobox.set("")

    def copy_function(self):
        clipboard.copy(str(self.final_result.get("0.0","end")))
        self.main_window.bell()

    def get_substats(self): # Function that updates Subplus1-5 Comboboxes list based on what the user select on substat1-4 comboboxes
        # Get Substat1-4 combobox selected value
        self.get_substat1 = self.substat1_combobox.get()
        self.get_substat2 = self.substat2_combobox.get()
        self.get_substat3 = self.substat3_combobox.get()
        self.get_substat4 = self.substat4_combobox.get()
        self.subplus1_combobox["values"] = [self.get_substat1, self.get_substat2, self.get_substat3, self.get_substat4]
        self.subplus2_combobox["values"] = [self.get_substat1, self.get_substat2, self.get_substat3, self.get_substat4]
        self.subplus3_combobox["values"] = [self.get_substat1, self.get_substat2, self.get_substat3, self.get_substat4]
        self.subplus4_combobox["values"] = [self.get_substat1, self.get_substat2, self.get_substat3, self.get_substat4]
        self.subplus5_combobox["values"] = [self.get_substat1, self.get_substat2, self.get_substat3, self.get_substat4]

    def get_substats_disabled(self):
        pass

    def clear_combobox(self): # clear subplus1-5 comboboxes function
        self.subplus1_combobox.set("")
        self.subplus2_combobox.set("")
        self.subplus3_combobox.set("")
        self.subplus4_combobox.set("")
        self.subplus5_combobox.set("")

    def switchfunction(self): # More Substat Options Switch
        if self.switchvar.get() == 1: # ON
            self.substat1_combobox["values"] = sub_stat_list2
            self.substat2_combobox["values"] = sub_stat_list2
            self.substat3_combobox["values"] = sub_stat_list2
            self.substat4_combobox["values"] = sub_stat_list2
        else: # OFF
            self.substat1_combobox["values"] = sub_stat_list
            self.substat2_combobox["values"] = sub_stat_list
            self.substat3_combobox["values"] = sub_stat_list
            self.substat4_combobox["values"] = sub_stat_list

    def switch2function(self): # Advance Substat Upgrade Switch
        if self.switchvar2.get() == 1: # ON
            self.subplus1_combobox["postcommand"] = self.get_substats_disabled
            self.subplus2_combobox["postcommand"] = self.get_substats_disabled
            self.subplus3_combobox["postcommand"] = self.get_substats_disabled
            self.subplus4_combobox["postcommand"] = self.get_substats_disabled
            self.subplus5_combobox["postcommand"] = self.get_substats_disabled
            self.subplus1_combobox["values"] = sub_stat_list2
            self.subplus2_combobox["values"] = sub_stat_list2
            self.subplus3_combobox["values"] = sub_stat_list2
            self.subplus4_combobox["values"] = sub_stat_list2
            self.subplus5_combobox["values"] = sub_stat_list2
        else:  # OFF
            self.subplus1_combobox["postcommand"] = self.get_substats
            self.subplus2_combobox["postcommand"] = self.get_substats
            self.subplus3_combobox["postcommand"] = self.get_substats
            self.subplus4_combobox["postcommand"] = self.get_substats
            self.subplus5_combobox["postcommand"] = self.get_substats

    # Artifact Buttons List
    def gladiator_click1(self):
        self.artifact_entry.delete(0,"end")
        self.artifact_entry.insert(0,23414)

    def gladiator_click2(self):
        self.artifact_entry.delete(0,"end")
        self.artifact_entry.insert(0,23412)

    def gladiator_click3(self):
        self.artifact_entry.delete(0, "end")
        self.artifact_entry.insert(0, 23415)

    def gladiator_click4(self):
        self.artifact_entry.delete(0, "end")
        self.artifact_entry.insert(0, 23411)

    def gladiator_click5(self):
        self.artifact_entry.delete(0, "end")
        self.artifact_entry.insert(0, 23413)

    def wanderer_click1(self):
        self.artifact_entry.delete(0, "end")
        self.artifact_entry.insert(0, 23394)

    def wanderer_click2(self):
        self.artifact_entry.delete(0, "end")
        self.artifact_entry.insert(0, 23392)

    def wanderer_click3(self):
        self.artifact_entry.delete(0, "end")
        self.artifact_entry.insert(0, 23395)

    def wanderer_click4(self):
        self.artifact_entry.delete(0, "end")
        self.artifact_entry.insert(0, 23391)

    def wanderer_click5(self):
        self.artifact_entry.delete(0, "end")
        self.artifact_entry.insert(0, 23393)

    def noblesse_click1(self):
        self.artifact_entry.delete(0, "end")
        self.artifact_entry.insert(0, 23354)

    def noblesse_click2(self):
        self.artifact_entry.delete(0, "end")
        self.artifact_entry.insert(0, 23352)

    def noblesse_click3(self):
        self.artifact_entry.delete(0, "end")
        self.artifact_entry.insert(0, 23355)

    def noblesse_click4(self):
        self.artifact_entry.delete(0, "end")
        self.artifact_entry.insert(0, 23351)

    def noblesse_click5(self):
        self.artifact_entry.delete(0, "end")
        self.artifact_entry.insert(0, 23353)

    def chivarly_click1(self):
        self.artifact_entry.delete(0, "end")
        self.artifact_entry.insert(0, 23344)

    def chivarly_click2(self):
        self.artifact_entry.delete(0, "end")
        self.artifact_entry.insert(0, 23342)

    def chivarly_click3(self):
        self.artifact_entry.delete(0, "end")
        self.artifact_entry.insert(0, 23345)

    def chivarly_click4(self):
        self.artifact_entry.delete(0, "end")
        self.artifact_entry.insert(0, 23341)

    def chivarly_click5(self):
        self.artifact_entry.delete(0, "end")
        self.artifact_entry.insert(0, 23343)

    def maiden_click1(self):
        self.artifact_entry.delete(0, "end")
        self.artifact_entry.insert(0, 23424)

    def maiden_click2(self):
        self.artifact_entry.delete(0, "end")
        self.artifact_entry.insert(0, 23422)

    def maiden_click3(self):
        self.artifact_entry.delete(0, "end")
        self.artifact_entry.insert(0, 23425)

    def maiden_click4(self):
        self.artifact_entry.delete(0, "end")
        self.artifact_entry.insert(0, 23421)

    def maiden_click5(self):
        self.artifact_entry.delete(0, "end")
        self.artifact_entry.insert(0, 23423)

    def venerer_click1(self):
        self.artifact_entry.delete(0, "end")
        self.artifact_entry.insert(0, 23404)

    def venerer_click2(self):
        self.artifact_entry.delete(0, "end")
        self.artifact_entry.insert(0, 23402)

    def venerer_click3(self):
        self.artifact_entry.delete(0, "end")
        self.artifact_entry.insert(0, 23405)

    def venerer_click4(self):
        self.artifact_entry.delete(0, "end")
        self.artifact_entry.insert(0, 23401)

    def venerer_click5(self):
        self.artifact_entry.delete(0, "end")
        self.artifact_entry.insert(0, 23403)

    def petra_click1(self):
        self.artifact_entry.delete(0, "end")
        self.artifact_entry.insert(0, 23494)

    def petra_click2(self):
        self.artifact_entry.delete(0, "end")
        self.artifact_entry.insert(0, 23492)

    def petra_click3(self):
        self.artifact_entry.delete(0, "end")
        self.artifact_entry.insert(0, 23495)

    def petra_click4(self):
        self.artifact_entry.delete(0, "end")
        self.artifact_entry.insert(0, 23491)

    def petra_click5(self):
        self.artifact_entry.delete(0, "end")
        self.artifact_entry.insert(0, 23493)

    def bolide_click1(self):
        self.artifact_entry.delete(0, "end")
        self.artifact_entry.insert(0, 23504)

    def bolide_click2(self):
        self.artifact_entry.delete(0, "end")
        self.artifact_entry.insert(0, 23502)

    def bolide_click3(self):
        self.artifact_entry.delete(0, "end")
        self.artifact_entry.insert(0, 23505)

    def bolide_click4(self):
        self.artifact_entry.delete(0, "end")
        self.artifact_entry.insert(0, 23501)

    def bolide_click5(self):
        self.artifact_entry.delete(0, "end")
        self.artifact_entry.insert(0, 23503)

    def thundersoother_click1(self):
        self.artifact_entry.delete(0, "end")
        self.artifact_entry.insert(0, 23444)

    def thundersoother_click2(self):
        self.artifact_entry.delete(0, "end")
        self.artifact_entry.insert(0, 23442)

    def thundersoother_click3(self):
        self.artifact_entry.delete(0, "end")
        self.artifact_entry.insert(0, 23445)

    def thundersoother_click4(self):
        self.artifact_entry.delete(0, "end")
        self.artifact_entry.insert(0, 23441)

    def thundersoother_click5(self):
        self.artifact_entry.delete(0, "end")
        self.artifact_entry.insert(0, 23443)

    def thundering_click1(self):
        self.artifact_entry.delete(0, "end")
        self.artifact_entry.insert(0, 23374)

    def thundering_click2(self):
        self.artifact_entry.delete(0, "end")
        self.artifact_entry.insert(0, 23372)

    def thundering_click3(self):
        self.artifact_entry.delete(0, "end")
        self.artifact_entry.insert(0, 23375)

    def thundering_click4(self):
        self.artifact_entry.delete(0, "end")
        self.artifact_entry.insert(0, 23371)

    def thundering_click5(self):
        self.artifact_entry.delete(0, "end")
        self.artifact_entry.insert(0, 23373)

    def lavawalker_click1(self):
        self.artifact_entry.delete(0, "end")
        self.artifact_entry.insert(0, 23434)

    def lavawalker_click2(self):
        self.artifact_entry.delete(0, "end")
        self.artifact_entry.insert(0, 23432)

    def lavawalker_click3(self):
        self.artifact_entry.delete(0, "end")
        self.artifact_entry.insert(0, 23435)

    def lavawalker_click4(self):
        self.artifact_entry.delete(0, "end")
        self.artifact_entry.insert(0, 23431)

    def lavawalker_click5(self):
        self.artifact_entry.delete(0, "end")
        self.artifact_entry.insert(0, 23433)

    def crimson_click1(self):
        self.artifact_entry.delete(0, "end")
        self.artifact_entry.insert(0, 23364)

    def crimson_click2(self):
        self.artifact_entry.delete(0, "end")
        self.artifact_entry.insert(0, 23362)

    def crimson_click3(self):
        self.artifact_entry.delete(0, "end")
        self.artifact_entry.insert(0, 23365)

    def crimson_click4(self):
        self.artifact_entry.delete(0, "end")
        self.artifact_entry.insert(0, 23361)

    def crimson_click5(self):
        self.artifact_entry.delete(0, "end")
        self.artifact_entry.insert(0, 23363)

    def blizzard_click1(self):
        self.artifact_entry.delete(0, "end")
        self.artifact_entry.insert(0, 23454)

    def blizzard_click2(self):
        self.artifact_entry.delete(0, "end")
        self.artifact_entry.insert(0, 23452)

    def blizzard_click3(self):
        self.artifact_entry.delete(0, "end")
        self.artifact_entry.insert(0, 23455)

    def blizzard_click4(self):
        self.artifact_entry.delete(0, "end")
        self.artifact_entry.insert(0, 23451)

    def blizzard_click5(self):
        self.artifact_entry.delete(0, "end")
        self.artifact_entry.insert(0, 23453)

    def hod_click1(self):
        self.artifact_entry.delete(0, "end")
        self.artifact_entry.insert(0, 23534)

    def hod_click2(self):
        self.artifact_entry.delete(0, "end")
        self.artifact_entry.insert(0, 23532)

    def hod_click3(self):
        self.artifact_entry.delete(0, "end")
        self.artifact_entry.insert(0, 23535)

    def hod_click4(self):
        self.artifact_entry.delete(0, "end")
        self.artifact_entry.insert(0, 23531)

    def hod_click5(self):
        self.artifact_entry.delete(0, "end")
        self.artifact_entry.insert(0, 23533)

    def tenacity_click1(self):
        self.artifact_entry.delete(0, "end")
        self.artifact_entry.insert(0, 23544)

    def tenacity_click2(self):
        self.artifact_entry.delete(0, "end")
        self.artifact_entry.insert(0, 23542)

    def tenacity_click3(self):
        self.artifact_entry.delete(0, "end")
        self.artifact_entry.insert(0, 23545)

    def tenacity_click4(self):
        self.artifact_entry.delete(0, "end")
        self.artifact_entry.insert(0, 23541)

    def tenacity_click5(self):
        self.artifact_entry.delete(0, "end")
        self.artifact_entry.insert(0, 23543)

    def paleflame_click1(self):
        self.artifact_entry.delete(0, "end")
        self.artifact_entry.insert(0, 23554)

    def paleflame_click2(self):
        self.artifact_entry.delete(0, "end")
        self.artifact_entry.insert(0, 23552)

    def paleflame_click3(self):
        self.artifact_entry.delete(0, "end")
        self.artifact_entry.insert(0, 23555)

    def paleflame_click4(self):
        self.artifact_entry.delete(0, "end")
        self.artifact_entry.insert(0, 23551)

    def paleflame_click5(self):
        self.artifact_entry.delete(0, "end")
        self.artifact_entry.insert(0, 23553)

    def shimenawa_click1(self):
        self.artifact_entry.delete(0, "end")
        self.artifact_entry.insert(0, 23564)

    def shimenawa_click2(self):
        self.artifact_entry.delete(0, "end")
        self.artifact_entry.insert(0, 23562)

    def shimenawa_click3(self):
        self.artifact_entry.delete(0, "end")
        self.artifact_entry.insert(0, 23565)

    def shimenawa_click4(self):
        self.artifact_entry.delete(0, "end")
        self.artifact_entry.insert(0, 23561)

    def shimenawa_click5(self):
        self.artifact_entry.delete(0, "end")
        self.artifact_entry.insert(0, 23563)

    def emblem_click1(self):
        self.artifact_entry.delete(0, "end")
        self.artifact_entry.insert(0, 23574)

    def emblem_click2(self):
        self.artifact_entry.delete(0, "end")
        self.artifact_entry.insert(0, 23572)

    def emblem_click3(self):
        self.artifact_entry.delete(0, "end")
        self.artifact_entry.insert(0, 23575)

    def emblem_click4(self):
        self.artifact_entry.delete(0, "end")
        self.artifact_entry.insert(0, 23571)

    def emblem_click5(self):
        self.artifact_entry.delete(0, "end")
        self.artifact_entry.insert(0, 23573)

    def husk_click1(self):
        self.artifact_entry.delete(0, "end")
        self.artifact_entry.insert(0, 23584)

    def husk_click2(self):
        self.artifact_entry.delete(0, "end")
        self.artifact_entry.insert(0, 23582)

    def husk_click3(self):
        self.artifact_entry.delete(0, "end")
        self.artifact_entry.insert(0, 23585)

    def husk_click4(self):
        self.artifact_entry.delete(0, "end")
        self.artifact_entry.insert(0, 23581)

    def husk_click5(self):
        self.artifact_entry.delete(0, "end")
        self.artifact_entry.insert(0, 23583)

    def oceanclam_click1(self):
        self.artifact_entry.delete(0, "end")
        self.artifact_entry.insert(0, 23594)

    def oceanclam_click2(self):
        self.artifact_entry.delete(0, "end")
        self.artifact_entry.insert(0, 23592)

    def oceanclam_click3(self):
        self.artifact_entry.delete(0, "end")
        self.artifact_entry.insert(0, 23595)

    def oceanclam_click4(self):
        self.artifact_entry.delete(0, "end")
        self.artifact_entry.insert(0, 23591)

    def oceanclam_click5(self):
        self.artifact_entry.delete(0, "end")
        self.artifact_entry.insert(0, 23593)

    def vermillion_click1(self):
        self.artifact_entry.delete(0, "end")
        self.artifact_entry.insert(0, 23604)

    def vermillion_click2(self):
        self.artifact_entry.delete(0, "end")
        self.artifact_entry.insert(0, 23602)

    def vermillion_click3(self):
        self.artifact_entry.delete(0, "end")
        self.artifact_entry.insert(0, 23605)

    def vermillion_click4(self):
        self.artifact_entry.delete(0, "end")
        self.artifact_entry.insert(0, 23601)

    def vermillion_click5(self):
        self.artifact_entry.delete(0, "end")
        self.artifact_entry.insert(0, 23603)

    def echoes_click1(self):
        self.artifact_entry.delete(0, "end")
        self.artifact_entry.insert(0, 23614)

    def echoes_click2(self):
        self.artifact_entry.delete(0, "end")
        self.artifact_entry.insert(0, 23612)

    def echoes_click3(self):
        self.artifact_entry.delete(0, "end")
        self.artifact_entry.insert(0, 23615)

    def echoes_click4(self):
        self.artifact_entry.delete(0, "end")
        self.artifact_entry.insert(0, 23611)

    def echoes_click5(self):
        self.artifact_entry.delete(0, "end")
        self.artifact_entry.insert(0, 23613)

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Artifact Command Generator by Keithy")
    root.iconbitmap("images/icon.ico")
    root.tk.call("source", "theme.tcl")
    root.tk.call("set_theme", "dark")
    root.resizable(False,False)
    app = Artifact_GeneratorApp(root)
    app.run()









