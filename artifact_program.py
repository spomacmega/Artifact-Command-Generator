import tkinter as tk
import tkinter.ttk as ttk
from pandas.io import clipboard
from tkinter import IntVar, PhotoImage
from artifact_program_data import *
import ttkbootstrap as ttk
from ttkbootstrap.constants import *

class Artifact_GeneratorApp:
    def __init__(self, master=None):

        # IMPORT IMAGES FOR mainframe2_five_star_artifacts Labelframe BUTTONS START
        self.gladiator_flower_img = PhotoImage(file="images/gladiator's finale/1.png")
        self.gladiator_feather_img = PhotoImage(file="images/gladiator's finale/2.png")
        self.gladiator_sands_img = PhotoImage(file="images/gladiator's finale/3.png")
        self.gladiator_goblet_img = PhotoImage(file="images/gladiator's finale/4.png")
        self.gladiator_circlet_img = PhotoImage(file="images/gladiator's finale/5.png")
        self.wanderer_flower_img = PhotoImage(file="images/wanderer's troupe/1.png")
        self.wanderer_feather_img = PhotoImage(file="images/wanderer's troupe/2.png")
        self.wanderer_sands_img = PhotoImage(file="images/wanderer's troupe/3.png")
        self.wanderer_goblet_img = PhotoImage(file="images/wanderer's troupe/4.png")
        self.wanderer_circlet_img = PhotoImage(file="images/wanderer's troupe/5.png")
        self.noblesse_flower_img = PhotoImage(file="images/noblesse oblige/1.png")
        self.noblesse_feather_img = PhotoImage(file="images/noblesse oblige/2.png")
        self.noblesse_sands_img = PhotoImage(file="images/noblesse oblige/3.png")
        self.noblesse_goblet_img = PhotoImage(file="images/noblesse oblige/4.png")
        self.noblesse_circlet_img = PhotoImage(file="images/noblesse oblige/5.png")
        self.chivarly_flower_img = PhotoImage(file="images/bloodstained chivalry/1.png")
        self.chivarly_feather_img = PhotoImage(file="images/bloodstained chivalry/2.png")
        self.chivarly_sands_img = PhotoImage(file="images/bloodstained chivalry/3.png")
        self.chivarly_goblet_img = PhotoImage(file="images/bloodstained chivalry/4.png")
        self.chivarly_circlet_img = PhotoImage(file="images/bloodstained chivalry/5.png")
        self.maiden_flower_img = PhotoImage(file="images/maiden beloved/1.png")
        self.maiden_feather_img = PhotoImage(file="images/maiden beloved/2.png")
        self.maiden_sands_img = PhotoImage(file="images/maiden beloved/3.png")
        self.maiden_goblet_img = PhotoImage(file="images/maiden beloved/4.png")
        self.maiden_circlet_img = PhotoImage(file="images/maiden beloved/5.png")
        self.venerer_flower_img = PhotoImage(file="images/viridescent venerer/1.png")
        self.venerer_feather_img = PhotoImage(file="images/viridescent venerer/2.png")
        self.venerer_sands_img = PhotoImage(file="images/viridescent venerer/3.png")
        self.venerer_goblet_img = PhotoImage(file="images/viridescent venerer/4.png")
        self.venerer_circlet_img = PhotoImage(file="images/viridescent venerer/5.png")
        self.petra_flower_img = PhotoImage(file="images/archaic petra/1.png")
        self.petra_feather_img = PhotoImage(file="images/archaic petra/2.png")
        self.petra_sands_img = PhotoImage(file="images/archaic petra/3.png")
        self.petra_goblet_img = PhotoImage(file="images/archaic petra/4.png")
        self.petra_circlet_img = PhotoImage(file="images/archaic petra/5.png")
        self.bolide_flower_img = PhotoImage(file="images/retracing bolide/1.png")
        self.bolide_feather_img = PhotoImage(file="images/retracing bolide/2.png")
        self.bolide_sands_img = PhotoImage(file="images/retracing bolide/3.png")
        self.bolide_goblet_img = PhotoImage(file="images/retracing bolide/4.png")
        self.bolide_circlet_img = PhotoImage(file="images/retracing bolide/5.png")
        self.thundersoother_flower_img = PhotoImage(file="images/thundersoother/1.png")
        self.thundersoother_feather_img = PhotoImage(file="images/thundersoother/2.png")
        self.thundersoother_sands_img = PhotoImage(file="images/thundersoother/3.png")
        self.thundersoother_goblet_img = PhotoImage(file="images/thundersoother/4.png")
        self.thundersoother_circlet_img = PhotoImage(file="images/thundersoother/5.png")
        self.thundering_flower_img = PhotoImage(file="images/thundering fury/1.png")
        self.thundering_feather_img = PhotoImage(file="images/thundering fury/2.png")
        self.thundering_sands_img = PhotoImage(file="images/thundering fury/3.png")
        self.thundering_goblet_img = PhotoImage(file="images/thundering fury/4.png")
        self.thundering_circlet_img = PhotoImage(file="images/thundering fury/5.png")
        self.lavawalker_flower_img = PhotoImage(file="images/lavawalker/1.png")
        self.lavawalker_feather_img = PhotoImage(file="images/lavawalker/2.png")
        self.lavawalker_sands_img = PhotoImage(file="images/lavawalker/3.png")
        self.lavawalker_goblet_img = PhotoImage(file="images/lavawalker/4.png")
        self.lavawalker_circlet_img = PhotoImage(file="images/lavawalker/5.png")
        self.crimson_flower_img = PhotoImage(file="images/crimson witch of flames/1.png")
        self.crimson_feather_img = PhotoImage(file="images/crimson witch of flames/2.png")
        self.crimson_sands_img = PhotoImage(file="images/crimson witch of flames/3.png")
        self.crimson_goblet_img = PhotoImage(file="images/crimson witch of flames/4.png")
        self.crimson_circlet_img = PhotoImage(file="images/crimson witch of flames/5.png")
        self.blizzard_flower_img = PhotoImage(file="images/blizzard strayer/1.png")
        self.blizzard_feather_img = PhotoImage(file="images/blizzard strayer/2.png")
        self.blizzard_sands_img = PhotoImage(file="images/blizzard strayer/3.png")
        self.blizzard_goblet_img = PhotoImage(file="images/blizzard strayer/4.png")
        self.blizzard_circlet_img = PhotoImage(file="images/blizzard strayer/5.png")
        self.hod_flower_img = PhotoImage(file="images/heart of depth/1.png")
        self.hod_feather_img = PhotoImage(file="images/heart of depth/2.png")
        self.hod_sands_img = PhotoImage(file="images/heart of depth/3.png")
        self.hod_goblet_img = PhotoImage(file="images/heart of depth/4.png")
        self.hod_circlet_img = PhotoImage(file="images/heart of depth/5.png")
        self.tenacity_flower_img = PhotoImage(file="images/tenacity of the millelith/1.png")
        self.tenacity_feather_img = PhotoImage(file="images/tenacity of the millelith/2.png")
        self.tenacity_sands_img = PhotoImage(file="images/tenacity of the millelith/3.png")
        self.tenacity_goblet_img = PhotoImage(file="images/tenacity of the millelith/4.png")
        self.tenacity_circlet_img = PhotoImage(file="images/tenacity of the millelith/5.png")
        self.paleflame_flower_img = PhotoImage(file="images/pale flame/1.png")
        self.paleflame_feather_img = PhotoImage(file="images/pale flame/2.png")
        self.paleflame_sands_img = PhotoImage(file="images/pale flame/3.png")
        self.paleflame_goblet_img = PhotoImage(file="images/pale flame/4.png")
        self.paleflame_circlet_img = PhotoImage(file="images/pale flame/5.png")
        self.shimenawa_flower_img = PhotoImage(file="images/shimenawa's reminiscence/1.png")
        self.shimenawa_feather_img = PhotoImage(file="images/shimenawa's reminiscence/2.png")
        self.shimenawa_sands_img = PhotoImage(file="images/shimenawa's reminiscence/3.png")
        self.shimenawa_goblet_img = PhotoImage(file="images/shimenawa's reminiscence/4.png")
        self.shimenawa_circlet_img = PhotoImage(file="images/shimenawa's reminiscence/5.png")
        self.emblem_flower_img = PhotoImage(file="images/emblem of severed fate/1.png")
        self.emblem_feather_img = PhotoImage(file="images/emblem of severed fate/2.png")
        self.emblem_sands_img = PhotoImage(file="images/emblem of severed fate/3.png")
        self.emblem_goblet_img = PhotoImage(file="images/emblem of severed fate/4.png")
        self.emblem_circlet_img = PhotoImage(file="images/emblem of severed fate/5.png")
        self.husk_flower_img = PhotoImage(file="images/husk of opulent dreams/1.png")
        self.husk_feather_img = PhotoImage(file="images/husk of opulent dreams/2.png")
        self.husk_sands_img = PhotoImage(file="images/husk of opulent dreams/3.png")
        self.husk_goblet_img = PhotoImage(file="images/husk of opulent dreams/4.png")
        self.husk_circlet_img = PhotoImage(file="images/husk of opulent dreams/5.png")
        self.oceanclam_flower_img = PhotoImage(file="images/ocean-hued clam/1.png")
        self.oceanclam_feather_img = PhotoImage(file="images/ocean-hued clam/2.png")
        self.oceanclam_sands_img = PhotoImage(file="images/ocean-hued clam/3.png")
        self.oceanclam_goblet_img = PhotoImage(file="images/ocean-hued clam/4.png")
        self.oceanclam_circlet_img = PhotoImage(file="images/ocean-hued clam/5.png")
        self.vermillion_flower_img = PhotoImage(file="images/vermillion hereafter/1.png")
        self.vermillion_feather_img = PhotoImage(file="images/vermillion hereafter/2.png")
        self.vermillion_sands_img = PhotoImage(file="images/vermillion hereafter/3.png")
        self.vermillion_goblet_img = PhotoImage(file="images/vermillion hereafter/4.png")
        self.vermillion_circlet_img = PhotoImage(file="images/vermillion hereafter/5.png")
        self.echoes_flower_img = PhotoImage(file="images/echoes of an offering/1.png")
        self.echoes_feather_img = PhotoImage(file="images/echoes of an offering/2.png")
        self.echoes_sands_img = PhotoImage(file="images/echoes of an offering/3.png")
        self.echoes_goblet_img = PhotoImage(file="images/echoes of an offering/4.png")
        self.echoes_circlet_img = PhotoImage(file="images/echoes of an offering/5.png")
        # IMPORT IMAGES FOR mainframe2_five_star_artifacts Labelfrane BUTTONS END

        # build ui
        self.main_window = ttk.Frame(master)

        # main_tabs_notebook // Create Main Tabs
        self.main_tabs_notebook = ttk.Notebook(root)
        self.main_tabs_notebook.grid(row=0,column=0)

        # artifact_tabs_notebook // Create Tabs for Create Artifact Tab Section
        self.artifact_tabs_notebook = ttk.Notebook(self.main_tabs_notebook)
        self.artifact_tabs_notebook.grid(row=0,column=0)

        # mainframe1_edit_tab Labelframe
        self.mainframe1_edit_tab = ttk.Labelframe(self.artifact_tabs_notebook)
        self.mainframe1_edit_tab.configure(borderwidth="0",text="")
        self.mainframe1_edit_tab.grid(column="0",ipadx="0",ipady="0",padx="0",pady="0",row="0",sticky="nw")

        # bigframe1_edit_tab Labelframe
        self.bigframe1_edit_tab = ttk.Labelframe(self.mainframe1_edit_tab)
        self.bigframe1_edit_tab.configure(borderwidth="0",text="")
        self.bigframe1_edit_tab.grid(column="0", ipadx="0", ipady="0", padx="0", pady="0", row="0")

        # frame1_edit_tab Labelframe
        self.frame1_edit_tab = ttk.Labelframe(self.bigframe1_edit_tab)
        self.frame1_edit_tab.configure(height="200", width="200",text="")
        self.frame1_edit_tab.grid(column="0", ipadx="75", ipady="5", padx="10", pady="10", row="0", sticky="nw")
        self.uid_label = ttk.Label(self.frame1_edit_tab)
        self.uid_label.configure(text="UID")
        self.uid_label.grid(column="0", row="0")
        self.uid_entry = ttk.Entry(self.frame1_edit_tab)
        self.uid_entry.grid(column="1", pady="5", row="0")
        self.artifact_label = ttk.Label(self.frame1_edit_tab)
        self.artifact_label.configure(text="Artifact ID")
        self.artifact_label.grid(column="0", row="1")
        self.artifact_entry = ttk.Entry(self.frame1_edit_tab)
        self.artifact_entry.grid(column="1", pady="5", row="1")

        # Selected Artifact
        self.selected_artifact_label = ttk.Label(self.frame1_edit_tab)
        self.selected_artifact_label.configure(text="Selected Artifact")
        self.selected_artifact_label.grid(column="0", ipadx="0", ipady="0", padx="10", pady="10", row="3")
        self.selected_artifact_button = ttk.Button(self.frame1_edit_tab)
        self.selected_artifact_button.configure(text="Click Here to Select",command=self.go_to_tab,bootstyle='primary-outline',image=self.crimson_flower_img,compound=LEFT)
        self.selected_artifact_button.grid(column="1", row="3", ipadx="0", ipady="0", padx="10", pady="10")

        # Artifact Level
        self.artifactlevel_label = ttk.Label(self.frame1_edit_tab)
        self.artifactlevel_label.configure(text="Artifact Level")
        self.artifactlevel_label.grid(column="0", padx="5", pady="5", row="4")
        self.spinbox1 = ttk.Spinbox(self.frame1_edit_tab)
        self.spinbox1_defaultvalue = tk.IntVar(value="20")
        self.spinbox1.configure(from_="0", increment="1", textvariable=self.spinbox1_defaultvalue, to="20",width="5", state = "readonly")
        self.spinbox1.grid(column="1", pady="0", row="4")

        # More Substat Options Checkbutton/Switch
        self.switch = ttk.Checkbutton(self.frame1_edit_tab)
        self.switchvar = IntVar()
        self.switch.configure(text="More Substat Options",variable=self.switchvar ,command=self.switchfunction,bootstyle="round-toggle")
        self.switch.grid(row=5, column=0, padx=5, pady=10, sticky="nsew")

        # Advance Substat Upgrade Checkbutton/Switch
        self.switch2 = ttk.Checkbutton(self.frame1_edit_tab)
        self.switchvar2 = IntVar()
        self.switch2.configure(text="Advance Substat Roll Upgrade",variable=self.switchvar2 ,command=self.switch2function,bootstyle="round-toggle")
        self.switch2.grid(row=6, column=0, padx=5, pady=10, sticky="nsew")

        # frame2 inside mainframe
        self.frame2_edit_tab = ttk.Labelframe(self.bigframe1_edit_tab)
        self.frame2_edit_tab.configure(text="Select Stats and Substat Roll Upgrades",height="0", width="0")
        self.frame2_edit_tab.grid(column="1",ipadx="20",ipady="5",padx="10", pady="10",row="0",sticky="nw")
        self.mainstat_label = ttk.Label(self.frame2_edit_tab)
        self.mainstat_label.configure(text="Main Stat :")
        self.mainstat_label.grid(column="0", padx="10", pady="10", row="0")
        self.mainstat_combobox = ttk.Combobox(self.frame2_edit_tab)
        self.mainstat_combobox.configure(values=main_stat_list, state="readonly")
        self.mainstat_combobox.bind("<<ComboboxSelected>>", lambda _: self.mainstat_combobox.selection_clear())
        self.mainstat_combobox.grid(column="1", row="0")
        self.substat1_label = ttk.Label(self.frame2_edit_tab)
        self.substat1_label.configure(text="Sub Stat #1 :")
        self.substat1_label.grid(column="0", padx="10", pady="10", row="1")
        self.substat1_combobox = ttk.Combobox(self.frame2_edit_tab)
        self.substat1_combobox.configure(values=sub_stat_list, postcommand=self.clear_subplus_comboboxes, state="readonly")
        self.substat1_combobox.bind("<<ComboboxSelected>>", lambda _: self.substat1_combobox.selection_clear())
        self.substat1_combobox.grid(column="1", row="1")
        self.substat2_label = ttk.Label(self.frame2_edit_tab)
        self.substat2_label.configure(text="Sub Stat #2 :")
        self.substat2_label.grid(column="0", padx="10", pady="10", row="2")
        self.substat2_combobox = ttk.Combobox(self.frame2_edit_tab)
        self.substat2_combobox.configure(values=sub_stat_list, postcommand=self.clear_subplus_comboboxes, state="readonly")
        self.substat2_combobox.bind("<<ComboboxSelected>>", lambda _: self.substat2_combobox.selection_clear())
        self.substat2_combobox.grid(column="1", row="2")
        self.substat3_label = ttk.Label(self.frame2_edit_tab)
        self.substat3_label.configure(text="Sub Stat #3 :")
        self.substat3_label.grid(column="0", padx="10", pady="10", row="3")
        self.substat3_combobox = ttk.Combobox(self.frame2_edit_tab)
        self.substat3_combobox.configure(values=sub_stat_list, postcommand=self.clear_subplus_comboboxes, state="readonly")
        self.substat3_combobox.bind("<<ComboboxSelected>>", lambda _: self.substat3_combobox.selection_clear())
        self.substat3_combobox.grid(column="1", row="3")
        self.substat4_label = ttk.Label(self.frame2_edit_tab)
        self.substat4_label.configure(text="Sub Stat #4 :")
        self.substat4_label.grid(column="0", padx="10", pady="10", row="4")
        self.substat4_combobox = ttk.Combobox(self.frame2_edit_tab)
        self.substat4_combobox.configure(values=sub_stat_list, postcommand=self.clear_subplus_comboboxes, state="readonly")
        self.substat4_combobox.bind("<<ComboboxSelected>>", lambda _: self.substat4_combobox.selection_clear())
        self.substat4_combobox.grid(column="1", row="4")
        # Sub Plus Section
        self.subplus1_label = ttk.Label(self.frame2_edit_tab)
        self.subplus1_label.configure(text="Sub Stat +4 :")
        self.subplus1_label.grid(column="3", padx="10", pady="10", row="0")
        self.subplus1_combobox = ttk.Combobox(self.frame2_edit_tab)
        self.subplus1_combobox.configure(values="", postcommand=self.get_substats, state="readonly")
        self.subplus1_combobox.bind("<<ComboboxSelected>>", lambda _: self.subplus1_combobox.selection_clear())
        self.subplus1_combobox.grid(column="4", row="0")
        self.subplus2_label = ttk.Label(self.frame2_edit_tab)
        self.subplus2_label.configure(text="Sub Stat +8 :")
        self.subplus2_label.grid(column="3", padx="10", pady="10", row="1")
        self.subplus2_combobox = ttk.Combobox(self.frame2_edit_tab)
        self.subplus2_combobox.configure(values="", postcommand=self.get_substats, state="readonly")
        self.subplus2_combobox.bind("<<ComboboxSelected>>", lambda _: self.subplus2_combobox.selection_clear())
        self.subplus2_combobox.grid(column="4", row="1")
        self.subplus3_label = ttk.Label(self.frame2_edit_tab)
        self.subplus3_label.configure(text="Sub Stat +12 :")
        self.subplus3_label.grid(column="3", padx="10", pady="10", row="2")
        self.subplus3_combobox = ttk.Combobox(self.frame2_edit_tab)
        self.subplus3_combobox.configure(values="", postcommand=self.get_substats, state="readonly")
        self.subplus3_combobox.bind("<<ComboboxSelected>>", lambda _: self.subplus3_combobox.selection_clear())
        self.subplus3_combobox.grid(column="4", row="2")
        self.subplus4_label = ttk.Label(self.frame2_edit_tab)
        self.subplus4_label.configure(text="Sub Stat +16 :")
        self.subplus4_label.grid(column="3", padx="10", pady="10", row="3")
        self.subplus4_combobox = ttk.Combobox(self.frame2_edit_tab)
        self.subplus4_combobox.configure(values="", postcommand=self.get_substats, state="readonly")
        self.subplus4_combobox.bind("<<ComboboxSelected>>", lambda _: self.subplus4_combobox.selection_clear())
        self.subplus4_combobox.grid(column="4", row="3")
        self.subplus5_label = ttk.Label(self.frame2_edit_tab)
        self.subplus5_label.configure(text="Sub Stat +20 :")
        self.subplus5_label.grid(column="3", padx="10", pady="10", row="4")
        self.subplus5_combobox = ttk.Combobox(self.frame2_edit_tab)
        self.subplus5_combobox.configure(values="", postcommand=self.get_substats, state="readonly")
        self.subplus5_combobox.bind("<<ComboboxSelected>>", lambda _: self.subplus5_combobox.selection_clear())
        self.subplus5_combobox.grid(column="4", row="4")

        # frame3_edit_tab Labelframe
        self.frame3_edit_tab = ttk.Labelframe(self.mainframe1_edit_tab)
        self.frame3_edit_tab.configure(text="",height="200", width="200",borderwidth="1")
        self.frame3_edit_tab.grid( column="0",row="3", ipadx="0",ipady="0",padx="10",pady="0",sticky="nw")
        self.final_result = tk.Text(self.frame3_edit_tab)
        self.final_result.configure(height="1", width="100")
        _text_ = "gart @ [Result will be shown here]"
        self.final_result.insert("0.0", _text_)
        self.final_result.grid(column="0", padx="5", pady="5", row="0")

        # frame4 inside frame3
        self.frame4_edit_tab = ttk.Labelframe(self.frame3_edit_tab)
        self.frame4_edit_tab.configure(height="200", width="200",text="")
        self.frame4_edit_tab.grid(column="0", padx="10", pady="10", row="2", sticky="nw")
        self.submit_button_artifact = ttk.Button(self.frame4_edit_tab)
        self.submit_button_artifact.configure(text="Generate Command")
        self.submit_button_artifact.grid(column="0", ipadx="0", ipady="0", padx="5", pady="5", row="0", sticky="nw")
        self.submit_button_artifact.configure(command=self.artifact_command_result)
        self.copy_button = ttk.Button(self.frame4_edit_tab)
        self.copy_button.configure(text="Copy Result")
        self.copy_button.grid(column="1", ipadx="0", ipady="0", padx="5", pady="5", row="0", sticky="nw")
        self.copy_button.configure(command=self.copy_function_artifact)
        self.clear_button = ttk.Button(self.frame4_edit_tab)
        self.clear_button.configure(text="Clear")
        self.clear_button.grid(column="2", ipadx="0", ipady="0", padx="5", pady="5", row="0", sticky="nw")
        self.clear_button.configure(command=self.clear_function)

        # Button Hu Tao Artifact Tab
        self.button1_hu_tao = ttk.Button(self.mainframe1_edit_tab)
        self.hu_tao_img1 = PhotoImage(file="images/artifact.png")
        self.button1_hu_tao.configure(image=self.hu_tao_img1,bootstyle="info-outline",command=self.artifact_command_result)
        self.button1_hu_tao.grid(column="1",row="0",ipadx="0",ipady="0",padx="10",pady="10",sticky="NW")


        # mainframe2_five_star_artifacts // Create a frame for the 5* Artifact tab
        self.mainframe2_five_star_artifacts = ttk.Labelframe(self.artifact_tabs_notebook)
        self.mainframe2_five_star_artifacts.configure(height="200", text="Select Artifact", width="200",borderwidth="0")
        self.mainframe2_five_star_artifacts.grid(column="0", padx="10", pady="10",row="4", sticky="nw")
        # Gladiator's finale Frame
        self.gladiator_frame = ttk.Labelframe(self.mainframe2_five_star_artifacts)
        self.gladiator_button1 = ttk.Button(self.gladiator_frame)
        self.gladiator_button1.configure(image=self.gladiator_flower_img,command=self.gladiator_click1,bootstyle="dark-outline")
        self.gladiator_button1.grid(column="0", row="0", pady=2, padx=2)
        self.gladiator_button2 = ttk.Button(self.gladiator_frame)
        self.gladiator_button2.configure(image=self.gladiator_feather_img,command=self.gladiator_click2,bootstyle="dark-outline")
        self.gladiator_button2.grid(column="1", row="0", pady=2, padx=2)
        self.gladiator_button3 = ttk.Button(self.gladiator_frame)
        self.gladiator_button3.configure(image=self.gladiator_sands_img,command=self.gladiator_click3,bootstyle="dark-outline")
        self.gladiator_button3.grid(column="2", row="0", pady=2, padx=2)
        self.gladiator_button4 = ttk.Button(self.gladiator_frame)
        self.gladiator_button4.configure(image=self.gladiator_goblet_img,command=self.gladiator_click4,bootstyle="dark-outline")
        self.gladiator_button4.grid(column="3", row="0", pady=2, padx=2)
        self.gladiator_button5 = ttk.Button(self.gladiator_frame)
        self.gladiator_button5.configure(image=self.gladiator_circlet_img,command=self.gladiator_click5,bootstyle="dark-outline")
        self.gladiator_button5.grid(column="4", row="0", pady=2, padx=2)
        self.gladiator_frame.configure(height="200", text="Gladiator's Finale", width="200")
        self.gladiator_frame.grid(column="0", ipadx="5", ipady="5", padx="5", pady="5", row="0")
        # Wanderer's Troupe Frame
        self.wanderer_frame = ttk.Labelframe(self.mainframe2_five_star_artifacts)
        self.wanderer_button1 = ttk.Button(self.wanderer_frame)
        self.wanderer_button1.configure(image=self.wanderer_flower_img,command=self.wanderer_click1,bootstyle="dark-outline")
        self.wanderer_button1.grid(column="0", row="0", pady=2, padx=2)
        self.wanderer_button2 = ttk.Button(self.wanderer_frame)
        self.wanderer_button2.configure(image=self.wanderer_feather_img,command=self.wanderer_click2,bootstyle="dark-outline")
        self.wanderer_button2.grid(column="1", row="0", pady=2, padx=2)
        self.wanderer_button3 = ttk.Button(self.wanderer_frame)
        self.wanderer_button3.configure(image=self.wanderer_sands_img,command=self.wanderer_click3,bootstyle="dark-outline")
        self.wanderer_button3.grid(column="2", row="0", pady=2, padx=2)
        self.wanderer_button4 = ttk.Button(self.wanderer_frame)
        self.wanderer_button4.configure(image=self.wanderer_goblet_img,command=self.wanderer_click4,bootstyle="dark-outline")
        self.wanderer_button4.grid(column="3", row="0", pady=2, padx=2)
        self.wanderer_button5 = ttk.Button(self.wanderer_frame)
        self.wanderer_button5.configure(image=self.wanderer_circlet_img,command=self.wanderer_click5,bootstyle="dark-outline")
        self.wanderer_button5.grid(column="4", row="0", pady=2, padx=2)
        self.wanderer_frame.configure(height="200", text="Wanderer's Troupe", width="200")
        self.wanderer_frame.grid( column="0", ipadx="5", ipady="5", padx="5", pady="5", row="1")
        # Noblesse Oblige Frame
        self.noblesse_frame = ttk.Labelframe(self.mainframe2_five_star_artifacts)
        self.noblesse_button1 = ttk.Button(self.noblesse_frame)
        self.noblesse_button1.configure(image=self.noblesse_flower_img,command=self.noblesse_click1,bootstyle="dark-outline")
        self.noblesse_button1.grid(column="0", padx="2", pady="2", row="0")
        self.noblesse_button2 = ttk.Button(self.noblesse_frame)
        self.noblesse_button2.configure(image=self.noblesse_feather_img,command=self.noblesse_click2,bootstyle="dark-outline")
        self.noblesse_button2.grid(column="1", padx="2", pady="2", row="0")
        self.noblesse_button3 = ttk.Button(self.noblesse_frame)
        self.noblesse_button3.configure(image=self.noblesse_sands_img,command=self.noblesse_click3,bootstyle="dark-outline")
        self.noblesse_button3.grid(column="2", padx="2", pady="2", row="0")
        self.noblesse_button4 = ttk.Button(self.noblesse_frame)
        self.noblesse_button4.configure(image=self.noblesse_goblet_img,command=self.noblesse_click4,bootstyle="dark-outline")
        self.noblesse_button4.grid(column="3", padx="2", pady="2", row="0")
        self.noblesse_button5 = ttk.Button(self.noblesse_frame)
        self.noblesse_button5.configure(image=self.noblesse_circlet_img,command=self.noblesse_click5,bootstyle="dark-outline")
        self.noblesse_button5.grid(column="4", padx="2", pady="2", row="0")
        self.noblesse_frame.configure(height="200", text="Noblesse Oblige", width="200")
        self.noblesse_frame.grid( column="0", ipadx="5", ipady="5", padx="5", pady="5", row="2")
        # Bloodstained Chivalry Frame
        self.chivarly_frame = ttk.Labelframe(self.mainframe2_five_star_artifacts)
        self.chivarly_button1 = ttk.Button(self.chivarly_frame)
        self.chivarly_button1.configure(image=self.chivarly_flower_img,command=self.chivarly_click1,bootstyle="dark-outline")
        self.chivarly_button1.grid(column="0", padx="2", pady="2", row="0")
        self.chivarly_button2 = ttk.Button(self.chivarly_frame)
        self.chivarly_button2.configure(image=self.chivarly_feather_img,command=self.chivarly_click2,bootstyle="dark-outline")
        self.chivarly_button2.grid(column="1", padx="2", pady="2", row="0")
        self.chivarly_button3 = ttk.Button(self.chivarly_frame)
        self.chivarly_button3.configure(image=self.chivarly_sands_img,command=self.chivarly_click3,bootstyle="dark-outline")
        self.chivarly_button3.grid(column="2", padx="2", pady="2", row="0")
        self.chivarly_button4 = ttk.Button(self.chivarly_frame)
        self.chivarly_button4.configure(image=self.chivarly_goblet_img,command=self.chivarly_click4,bootstyle="dark-outline")
        self.chivarly_button4.grid(column="3", padx="2", pady="2", row="0")
        self.chivarly_button5 = ttk.Button(self.chivarly_frame)
        self.chivarly_button5.configure(image=self.chivarly_circlet_img,command=self.chivarly_click5,bootstyle="dark-outline")
        self.chivarly_button5.grid(column="4", padx="2", pady="2", row="0")
        self.chivarly_frame.configure(height="200", text="Bloodstained Chivalry", width="200")
        self.chivarly_frame.grid(column="0", ipadx="5", ipady="5", padx="5", pady="5", row="3")
        # Maiden Beloved Frame
        self.maiden_frame = ttk.Labelframe(self.mainframe2_five_star_artifacts)
        self.maiden_button1 = ttk.Button(self.maiden_frame)
        self.maiden_button1.configure(image=self.maiden_flower_img,command=self.maiden_click1,bootstyle="dark-outline")
        self.maiden_button1.grid(column="0", padx="2", pady="2", row="0")
        self.maiden_button2 = ttk.Button(self.maiden_frame)
        self.maiden_button2.configure(image=self.maiden_feather_img,command=self.maiden_click2,bootstyle="dark-outline")
        self.maiden_button2.grid(column="1", padx="2", pady="2", row="0")
        self.maiden_button3 = ttk.Button(self.maiden_frame)
        self.maiden_button3.configure(image=self.maiden_sands_img,command=self.maiden_click3,bootstyle="dark-outline")
        self.maiden_button3.grid(column="2", padx="2", pady="2", row="0")
        self.maiden_button4 = ttk.Button(self.maiden_frame)
        self.maiden_button4.configure(image=self.maiden_goblet_img,command=self.maiden_click4,bootstyle="dark-outline")
        self.maiden_button4.grid(column="3", padx="2", pady="2", row="0")
        self.maiden_button5 = ttk.Button(self.maiden_frame)
        self.maiden_button5.configure(image=self.maiden_circlet_img,command=self.maiden_click5,bootstyle="dark-outline")
        self.maiden_button5.grid(column="4", padx="2", pady="2", row="0")
        self.maiden_frame.configure(height="200", text="Maiden Beloved", width="200")
        self.maiden_frame.grid(column="0", ipadx="5", ipady="5", padx="5", pady="5", row="4")
        # Viridescent Venerer Frame
        self.venerer_frame = ttk.Labelframe(self.mainframe2_five_star_artifacts)
        self.venerer_button1 = ttk.Button(self.venerer_frame)
        self.venerer_button1.configure(image=self.venerer_flower_img,command=self.venerer_click1,bootstyle="dark-outline")
        self.venerer_button1.grid(column="0", padx="2", pady="2", row="0")
        self.venerer_button2 = ttk.Button(self.venerer_frame)
        self.venerer_button2.configure(image=self.venerer_feather_img,command=self.venerer_click2,bootstyle="dark-outline")
        self.venerer_button2.grid(column="1", padx="2", pady="2", row="0")
        self.venerer_button3 = ttk.Button(self.venerer_frame)
        self.venerer_button3.configure(image=self.venerer_sands_img,command=self.venerer_click3,bootstyle="dark-outline")
        self.venerer_button3.grid(column="2", padx="2", pady="2", row="0")
        self.venerer_button4 = ttk.Button(self.venerer_frame)
        self.venerer_button4.configure(image=self.venerer_goblet_img,command=self.venerer_click4,bootstyle="dark-outline")
        self.venerer_button4.grid(column="3", padx="2", pady="2", row="0")
        self.venerer_button5 = ttk.Button(self.venerer_frame)
        self.venerer_button5.configure(image=self.venerer_circlet_img,command=self.venerer_click5,bootstyle="dark-outline")
        self.venerer_button5.grid(column="4", padx="2", pady="2", row="0")
        self.venerer_frame.configure(height="200", text="Viridescent Venerer", width="200")
        self.venerer_frame.grid(column="1", ipadx="5", ipady="5", padx="5", pady="5", row="0")
        # Archaic Petra Frame
        self.petra_frame = ttk.Labelframe(self.mainframe2_five_star_artifacts)
        self.petra_button1 = ttk.Button(self.petra_frame)
        self.petra_button1.configure(image=self.petra_flower_img,command=self.petra_click1,bootstyle="dark-outline")
        self.petra_button1.grid(column="0", padx="2", pady="2", row="0")
        self.petra_button2 = ttk.Button(self.petra_frame)
        self.petra_button2.configure(image=self.petra_feather_img,command=self.petra_click2,bootstyle="dark-outline")
        self.petra_button2.grid(column="1", padx="2", pady="2", row="0")
        self.petra_button3 = ttk.Button(self.petra_frame)
        self.petra_button3.configure(image=self.petra_sands_img,command=self.petra_click3,bootstyle="dark-outline")
        self.petra_button3.grid(column="2", padx="2", pady="2", row="0")
        self.petra_button4 = ttk.Button(self.petra_frame)
        self.petra_button4.configure(image=self.petra_goblet_img,command=self.petra_click4,bootstyle="dark-outline")
        self.petra_button4.grid(column="3", padx="2", pady="2", row="0")
        self.petra_button5 = ttk.Button(self.petra_frame)
        self.petra_button5.configure(image=self.petra_circlet_img,command=self.petra_click5,bootstyle="dark-outline")
        self.petra_button5.grid(column="4", padx="2", pady="2", row="0")
        self.petra_frame.configure(height="200", text="Archaic Petra", width="200")
        self.petra_frame.grid(column="1", ipadx="5", ipady="5", padx="5", pady="5", row="1")
        # Retracing Bolide Frame
        self.bolide_frame = ttk.Labelframe(self.mainframe2_five_star_artifacts)
        self.bolide_button1 = ttk.Button(self.bolide_frame)
        self.bolide_button1.configure(image=self.bolide_flower_img,command=self.bolide_click1,bootstyle="dark-outline")
        self.bolide_button1.grid(column="0", padx="2", pady="2", row="0")
        self.bolide_button2 = ttk.Button(self.bolide_frame)
        self.bolide_button2.configure(image=self.bolide_feather_img,command=self.bolide_click2,bootstyle="dark-outline")
        self.bolide_button2.grid(column="1", padx="2", pady="2", row="0")
        self.bolide_button3 = ttk.Button(self.bolide_frame)
        self.bolide_button3.configure(image=self.bolide_sands_img,command=self.bolide_click3,bootstyle="dark-outline")
        self.bolide_button3.grid(column="2", padx="2", pady="2", row="0")
        self.bolide_button4 = ttk.Button(self.bolide_frame)
        self.bolide_button4.configure(image=self.bolide_goblet_img,command=self.bolide_click4,bootstyle="dark-outline")
        self.bolide_button4.grid(column="3", padx="2", pady="2", row="0")
        self.bolide_button5 = ttk.Button(self.bolide_frame)
        self.bolide_button5.configure(image=self.bolide_circlet_img,command=self.bolide_click5,bootstyle="dark-outline")
        self.bolide_button5.grid(column="4", padx="2", pady="2", row="0")
        self.bolide_frame.configure(height="200", text="Retracing Bolide", width="200")
        self.bolide_frame.grid(column="1", ipadx="5", ipady="5", padx="5", pady="5", row="2")
        # Thundersoother Frame
        self.thundersoother_frame = ttk.Labelframe(self.mainframe2_five_star_artifacts)
        self.thundersoother_button1 = ttk.Button(self.thundersoother_frame)
        self.thundersoother_button1.configure(image=self.thundersoother_flower_img,command=self.thundersoother_click1,bootstyle="dark-outline")
        self.thundersoother_button1.grid(column="0", padx="2", pady="2", row="0")
        self.thundersoother_button2 = ttk.Button(self.thundersoother_frame)
        self.thundersoother_button2.configure(image=self.thundersoother_feather_img,command=self.thundersoother_click2,bootstyle="dark-outline")
        self.thundersoother_button2.grid(column="1", padx="2", pady="2", row="0")
        self.thundersoother_button3 = ttk.Button(self.thundersoother_frame)
        self.thundersoother_button3.configure(image=self.thundersoother_sands_img,command=self.thundersoother_click3,bootstyle="dark-outline")
        self.thundersoother_button3.grid(column="2", padx="2", pady="2", row="0")
        self.thundersoother_button4 = ttk.Button(self.thundersoother_frame)
        self.thundersoother_button4.configure(image=self.thundersoother_goblet_img,command=self.thundersoother_click4,bootstyle="dark-outline")
        self.thundersoother_button4.grid(column="3", padx="2", pady="2", row="0")
        self.thundersoother_button5 = ttk.Button(self.thundersoother_frame)
        self.thundersoother_button5.configure(image=self.thundersoother_circlet_img,command=self.thundersoother_click5,bootstyle="dark-outline")
        self.thundersoother_button5.grid(column="4", padx="2", pady="2", row="0")
        self.thundersoother_frame.configure(height="200", text="Thundersoother", width="200")
        self.thundersoother_frame.grid(column="1", ipadx="5", ipady="5", padx="5", pady="5", row="3")
        # Thundering Fury Frame
        self.thundering_fury_frame = ttk.Labelframe(self.mainframe2_five_star_artifacts)
        self.thundering_button1 = ttk.Button(self.thundering_fury_frame)
        self.thundering_button1.configure(image=self.thundering_flower_img,command=self.thundering_click1,bootstyle="dark-outline")
        self.thundering_button1.grid(column="0", padx="2", pady="2", row="0")
        self.thundering_button2 = ttk.Button(self.thundering_fury_frame)
        self.thundering_button2.configure(image=self.thundering_feather_img,command=self.thundering_click2,bootstyle="dark-outline")
        self.thundering_button2.grid(column="1", padx="2", pady="2", row="0")
        self.thundering_button3 = ttk.Button(self.thundering_fury_frame)
        self.thundering_button3.configure(image=self.thundering_sands_img,command=self.thundering_click3,bootstyle="dark-outline")
        self.thundering_button3.grid(column="2", padx="2", pady="2", row="0")
        self.thundering_button4 = ttk.Button(self.thundering_fury_frame)
        self.thundering_button4.configure(image=self.thundering_goblet_img,command=self.thundering_click4,bootstyle="dark-outline")
        self.thundering_button4.grid(column="3", padx="2", pady="2", row="0")
        self.thundering_button5 = ttk.Button(self.thundering_fury_frame)
        self.thundering_button5.configure(image=self.thundering_circlet_img,command=self.thundering_click5,bootstyle="dark-outline")
        self.thundering_button5.grid(column="4", padx="2", pady="2", row="0")
        self.thundering_fury_frame.configure(height="200", text="Thundering Fury", width="200")
        self.thundering_fury_frame.grid(column="1", ipadx="5", ipady="5", padx="5", pady="5", row="4")
        # Lava Walker Frame
        self.lavawalker_frame = ttk.Labelframe(self.mainframe2_five_star_artifacts)
        self.lavawalker_button1 = ttk.Button(self.lavawalker_frame)
        self.lavawalker_button1.configure(image=self.lavawalker_flower_img,command=self.lavawalker_click1,bootstyle="dark-outline")
        self.lavawalker_button1.grid(column="0", padx="2", pady="2", row="0")
        self.lavawalker_button2 = ttk.Button(self.lavawalker_frame)
        self.lavawalker_button2.configure(image=self.lavawalker_feather_img,command=self.lavawalker_click2,bootstyle="dark-outline")
        self.lavawalker_button2.grid(column="1", padx="2", pady="2", row="0")
        self.lavawalker_button3 = ttk.Button(self.lavawalker_frame)
        self.lavawalker_button3.configure(image=self.lavawalker_sands_img,command=self.lavawalker_click3,bootstyle="dark-outline")
        self.lavawalker_button3.grid(column="2", padx="2", pady="2", row="0")
        self.lavawalker_button4 = ttk.Button(self.lavawalker_frame)
        self.lavawalker_button4.configure(image=self.lavawalker_goblet_img,command=self.lavawalker_click4,bootstyle="dark-outline")
        self.lavawalker_button4.grid(column="3", padx="2", pady="2", row="0")
        self.lavawalker_button5 = ttk.Button(self.lavawalker_frame)
        self.lavawalker_button5.configure(image=self.lavawalker_circlet_img,command=self.lavawalker_click5,bootstyle="dark-outline")
        self.lavawalker_button5.grid(column="4", padx="2", pady="2", row="0")
        self.lavawalker_frame.configure(height="200", text="Lavawalker", width="200")
        self.lavawalker_frame.grid(column="2", ipadx="5", ipady="5", padx="5", pady="5", row="0")
        # Crimson Witch of Flames Frame
        self.crimson_witch_frame = ttk.Labelframe(self.mainframe2_five_star_artifacts)
        self.crimson_button1 = ttk.Button(self.crimson_witch_frame)
        self.crimson_button1.configure(image=self.crimson_flower_img,command=self.crimson_click1,bootstyle="dark-outline")
        self.crimson_button1.grid(column="0", padx="2", pady="2", row="0")
        self.crimson_button2 = ttk.Button(self.crimson_witch_frame)
        self.crimson_button2.configure(image=self.crimson_feather_img,command=self.crimson_click2,bootstyle="dark-outline")
        self.crimson_button2.grid(column="1", padx="2", pady="2", row="0")
        self.crimson_button3 = ttk.Button(self.crimson_witch_frame)
        self.crimson_button3.configure(image=self.crimson_sands_img,command=self.crimson_click3,bootstyle="dark-outline")
        self.crimson_button3.grid(column="2", padx="2", pady="2", row="0")
        self.crimson_button4 = ttk.Button(self.crimson_witch_frame)
        self.crimson_button4.configure(image=self.crimson_goblet_img,command=self.crimson_click4,bootstyle="dark-outline")
        self.crimson_button4.grid(column="3", padx="2", pady="2", row="0")
        self.crimson_button5 = ttk.Button(self.crimson_witch_frame)
        self.crimson_button5.configure(image=self.crimson_circlet_img,command=self.crimson_click5,bootstyle="dark-outline")
        self.crimson_button5.grid(column="4", padx="2", pady="2", row="0")
        self.crimson_witch_frame.configure(height="200", text="Crimson Witch of Flames", width="200")
        self.crimson_witch_frame.grid(column="2", ipadx="5", ipady="5", padx="5", pady="5", row="1")
        # Blizzard Strayer Frame
        self.blizzard_frame = ttk.Labelframe(self.mainframe2_five_star_artifacts)
        self.blizzard_button1 = ttk.Button(self.blizzard_frame)
        self.blizzard_button1.configure(image=self.blizzard_flower_img,command=self.blizzard_click1,bootstyle="dark-outline")
        self.blizzard_button1.grid(column="0", padx="2", pady="2", row="0")
        self.blizzard_button2 = ttk.Button(self.blizzard_frame)
        self.blizzard_button2.configure(image=self.blizzard_feather_img,command=self.blizzard_click2,bootstyle="dark-outline")
        self.blizzard_button2.grid(column="1", padx="2", pady="2", row="0")
        self.blizzard_button3 = ttk.Button(self.blizzard_frame)
        self.blizzard_button3.configure(image=self.blizzard_sands_img,command=self.blizzard_click3,bootstyle="dark-outline")
        self.blizzard_button3.grid(column="2", padx="2", pady="2", row="0")
        self.blizzard_button4 = ttk.Button(self.blizzard_frame)
        self.blizzard_button4.configure(image=self.blizzard_goblet_img,command=self.blizzard_click4,bootstyle="dark-outline")
        self.blizzard_button4.grid(column="3", padx="2", pady="2", row="0")
        self.blizzard_button5 = ttk.Button(self.blizzard_frame)
        self.blizzard_button5.configure(image=self.blizzard_circlet_img,command=self.blizzard_click5,bootstyle="dark-outline")
        self.blizzard_button5.grid(column="4", padx="2", pady="2", row="0")
        self.blizzard_frame.configure(height="200", text="Blizzard Strayer", width="200")
        self.blizzard_frame.grid(column="2", ipadx="5", ipady="5", padx="5", pady="5", row="2")
        # Heart of Depth Frame
        self.heart_of_depth_frame = ttk.Labelframe(self.mainframe2_five_star_artifacts)
        self.hod_button1 = ttk.Button(self.heart_of_depth_frame)
        self.hod_button1.configure(image=self.hod_flower_img,command=self.hod_click1,bootstyle="dark-outline")
        self.hod_button1.grid(column="0", padx="2", pady="2", row="0")
        self.hod_button2 = ttk.Button(self.heart_of_depth_frame)
        self.hod_button2.configure(image=self.hod_feather_img,command=self.hod_click2,bootstyle="dark-outline")
        self.hod_button2.grid(column="1", padx="2", pady="2", row="0")
        self.hod_button3 = ttk.Button(self.heart_of_depth_frame)
        self.hod_button3.configure(image=self.hod_sands_img,command=self.hod_click3,bootstyle="dark-outline")
        self.hod_button3.grid(column="2", padx="2", pady="2", row="0")
        self.hod_button4 = ttk.Button(self.heart_of_depth_frame)
        self.hod_button4.configure(image=self.hod_goblet_img,command=self.hod_click4,bootstyle="dark-outline")
        self.hod_button4.grid(column="3", padx="2", pady="2", row="0")
        self.hod_button5 = ttk.Button(self.heart_of_depth_frame)
        self.hod_button5.configure(image=self.hod_circlet_img,command=self.hod_click5,bootstyle="dark-outline")
        self.hod_button5.grid(column="4", padx="2", pady="2", row="0")
        self.heart_of_depth_frame.configure(height="200", text="Heart of Depth", width="200")
        self.heart_of_depth_frame.grid(column="2", ipadx="5", ipady="5", padx="5", pady="5", row="3")
        # Tenacity of the Millelith Frame
        self.tenacity_frame = ttk.Labelframe(self.mainframe2_five_star_artifacts)
        self.tenacity_button1 = ttk.Button(self.tenacity_frame)
        self.tenacity_button1.configure(image=self.tenacity_flower_img,command=self.tenacity_click1,bootstyle="dark-outline")
        self.tenacity_button1.grid(column="0", padx="2", pady="2", row="0")
        self.tenacity_button2 = ttk.Button(self.tenacity_frame)
        self.tenacity_button2.configure(image=self.tenacity_feather_img,command=self.tenacity_click2,bootstyle="dark-outline")
        self.tenacity_button2.grid(column="1", padx="2", pady="2", row="0")
        self.tenacity_button3 = ttk.Button(self.tenacity_frame)
        self.tenacity_button3.configure(image=self.tenacity_sands_img,command=self.tenacity_click3,bootstyle="dark-outline")
        self.tenacity_button3.grid(column="2", padx="2", pady="2", row="0")
        self.tenacity_button4 = ttk.Button(self.tenacity_frame)
        self.tenacity_button4.configure(image=self.tenacity_goblet_img,command=self.tenacity_click4,bootstyle="dark-outline")
        self.tenacity_button4.grid(column="3", padx="2", pady="2", row="0")
        self.tenacity_button5 = ttk.Button(self.tenacity_frame)
        self.tenacity_button5.configure(image=self.tenacity_circlet_img,command=self.tenacity_click5,bootstyle="dark-outline")
        self.tenacity_button5.grid(column="4", padx="2", pady="2", row="0")
        self.tenacity_frame.configure(height="200", text="Tenacity of the Millelith", width="200")
        self.tenacity_frame.grid(column="2", ipadx="5", ipady="5", padx="5", pady="5", row="4")
        # Pale Flame Frame
        self.pale_flame_frame = ttk.Labelframe(self.mainframe2_five_star_artifacts)
        self.pale_flame_button1 = ttk.Button(self.pale_flame_frame)
        self.pale_flame_button1.configure(image=self.paleflame_flower_img,command=self.paleflame_click1,bootstyle="dark-outline")
        self.pale_flame_button1.grid(column="0", padx="2", pady="2", row="0")
        self.pale_flame_button2 = ttk.Button(self.pale_flame_frame)
        self.pale_flame_button2.configure(image=self.paleflame_feather_img,command=self.paleflame_click2,bootstyle="dark-outline")
        self.pale_flame_button2.grid(column="1", padx="2", pady="2", row="0")
        self.pale_flame_button3 = ttk.Button(self.pale_flame_frame)
        self.pale_flame_button3.configure(image=self.paleflame_sands_img,command=self.paleflame_click3,bootstyle="dark-outline")
        self.pale_flame_button3.grid(column="2", padx="2", pady="2", row="0")
        self.pale_flame_button4 = ttk.Button(self.pale_flame_frame)
        self.pale_flame_button4.configure(image=self.paleflame_goblet_img,command=self.paleflame_click4,bootstyle="dark-outline")
        self.pale_flame_button4.grid(column="3", padx="2", pady="2", row="0")
        self.pale_flame_button5 = ttk.Button(self.pale_flame_frame)
        self.pale_flame_button5.configure(image=self.paleflame_circlet_img,command=self.paleflame_click5,bootstyle="dark-outline")
        self.pale_flame_button5.grid(column="4", padx="2", pady="2", row="0")
        self.pale_flame_frame.configure(height="200", text="Pale Flame", width="200")
        self.pale_flame_frame.grid(column="3", ipadx="5", ipady="5", padx="5", pady="5", row="0")
        # Shimenawa's Reminiscence Frame
        self.shimenawa_frame = ttk.Labelframe(self.mainframe2_five_star_artifacts)
        self.shimenawa_button1 = ttk.Button(self.shimenawa_frame)
        self.shimenawa_button1.configure(image=self.shimenawa_flower_img,command=self.shimenawa_click1,bootstyle="dark-outline")
        self.shimenawa_button1.grid(column="0", padx="2", pady="2", row="0")
        self.shimenawa_button2 = ttk.Button(self.shimenawa_frame)
        self.shimenawa_button2.configure(image=self.shimenawa_feather_img,command=self.shimenawa_click2,bootstyle="dark-outline")
        self.shimenawa_button2.grid(column="1", padx="2", pady="2", row="0")
        self.shimenawa_button3 = ttk.Button(self.shimenawa_frame)
        self.shimenawa_button3.configure(image=self.shimenawa_sands_img,command=self.shimenawa_click3,bootstyle="dark-outline")
        self.shimenawa_button3.grid(column="2", padx="2", pady="2", row="0")
        self.shimenawa_button4 = ttk.Button(self.shimenawa_frame)
        self.shimenawa_button4.configure(image=self.shimenawa_goblet_img,command=self.shimenawa_click4,bootstyle="dark-outline")
        self.shimenawa_button4.grid(column="3", padx="2", pady="2", row="0")
        self.shimenawa_button5 = ttk.Button(self.shimenawa_frame)
        self.shimenawa_button5.configure(image=self.shimenawa_circlet_img,command=self.shimenawa_click5,bootstyle="dark-outline")
        self.shimenawa_button5.grid(column="4", padx="2", pady="2", row="0")
        self.shimenawa_frame.configure(height="200", text="Shimenawas Reminiscence", width="200")
        self.shimenawa_frame.grid(column="3", ipadx="5", ipady="5", padx="5", pady="5", row="1")
        # Emblem of Severed Fate Frame
        self.emblem_frame = ttk.Labelframe(self.mainframe2_five_star_artifacts)
        self.emblem_button1 = ttk.Button(self.emblem_frame)
        self.emblem_button1.configure(image=self.emblem_flower_img,command=self.emblem_click1,bootstyle="dark-outline")
        self.emblem_button1.grid(column="0", padx="2", pady="2", row="0")
        self.emblem_button2 = ttk.Button(self.emblem_frame)
        self.emblem_button2.configure(image=self.emblem_feather_img,command=self.emblem_click2,bootstyle="dark-outline")
        self.emblem_button2.grid(column="1", padx="2", pady="2", row="0")
        self.emblem_button3 = ttk.Button(self.emblem_frame)
        self.emblem_button3.configure(image=self.emblem_sands_img,command=self.emblem_click3,bootstyle="dark-outline")
        self.emblem_button3.grid(column="2", padx="2", pady="2", row="0")
        self.emblem_button4 = ttk.Button(self.emblem_frame)
        self.emblem_button4.configure(image=self.emblem_goblet_img,command=self.emblem_click4,bootstyle="dark-outline")
        self.emblem_button4.grid(column="3", padx="2", pady="2", row="0")
        self.emblem_button5 = ttk.Button(self.emblem_frame)
        self.emblem_button5.configure(image=self.emblem_circlet_img,command=self.emblem_click5,bootstyle="dark-outline")
        self.emblem_button5.grid(column="4", padx="2", pady="2", row="0")
        self.emblem_frame.configure(height="200", text="Emblem of Severed Fate", width="200")
        self.emblem_frame.grid(column="3", ipadx="5", ipady="5", padx="5", pady="5", row="2")
        # Husk of Opulent Dreams Frame
        self.husk_frame = ttk.Labelframe(self.mainframe2_five_star_artifacts)
        self.husk_button1 = ttk.Button(self.husk_frame)
        self.husk_button1.configure(image=self.husk_flower_img,command=self.husk_click1,bootstyle="dark-outline")
        self.husk_button1.grid(column="0", padx="2", pady="2", row="0")
        self.husk_button2 = ttk.Button(self.husk_frame)
        self.husk_button2.configure(image=self.husk_feather_img,command=self.husk_click2,bootstyle="dark-outline")
        self.husk_button2.grid(column="1", padx="2", pady="2", row="0")
        self.husk_button3 = ttk.Button(self.husk_frame)
        self.husk_button3.configure(image=self.husk_sands_img,command=self.husk_click3,bootstyle="dark-outline")
        self.husk_button3.grid(column="2", padx="2", pady="2", row="0")
        self.husk_button4 = ttk.Button(self.husk_frame)
        self.husk_button4.configure(image=self.husk_goblet_img,command=self.husk_click4,bootstyle="dark-outline")
        self.husk_button4.grid(column="3", padx="2", pady="2", row="0")
        self.husk_button5 = ttk.Button(self.husk_frame)
        self.husk_button5.configure(image=self.husk_circlet_img,command=self.husk_click5,bootstyle="dark-outline")
        self.husk_button5.grid(column="4", padx="2", pady="2", row="0")
        self.husk_frame.configure(height="200", text="Husk of Opulent Dreams", width="200")
        self.husk_frame.grid(column="3", ipadx="5", ipady="5", padx="5", pady="5", row="3")
        # Ocean-Hued Clam Frame
        self.ocean_clam_frame = ttk.Labelframe(self.mainframe2_five_star_artifacts)
        self.ocean_clam_button1 = ttk.Button(self.ocean_clam_frame)
        self.ocean_clam_button1.configure(image=self.oceanclam_flower_img,command=self.oceanclam_click1,bootstyle="dark-outline")
        self.ocean_clam_button1.grid(column="0", padx="2", pady="2", row="0")
        self.ocean_clam_button2 = ttk.Button(self.ocean_clam_frame)
        self.ocean_clam_button2.configure(image=self.oceanclam_feather_img,command=self.oceanclam_click2,bootstyle="dark-outline")
        self.ocean_clam_button2.grid(column="1", padx="2", pady="2", row="0")
        self.ocean_clam_button3 = ttk.Button(self.ocean_clam_frame)
        self.ocean_clam_button3.configure(image=self.oceanclam_sands_img,command=self.oceanclam_click3,bootstyle="dark-outline")
        self.ocean_clam_button3.grid(column="2", padx="2", pady="2", row="0")
        self.ocean_clam_button4 = ttk.Button(self.ocean_clam_frame)
        self.ocean_clam_button4.configure(image=self.oceanclam_goblet_img,command=self.oceanclam_click4,bootstyle="dark-outline")
        self.ocean_clam_button4.grid(column="3", padx="2", pady="2", row="0")
        self.ocean_clam_button5 = ttk.Button(self.ocean_clam_frame)
        self.ocean_clam_button5.configure(image=self.oceanclam_circlet_img,command=self.oceanclam_click5,bootstyle="dark-outline")
        self.ocean_clam_button5.grid(column="4", padx="2", pady="2", row="0")
        self.ocean_clam_frame.configure(height="200", text="Ocean-Hued Clam", width="200")
        self.ocean_clam_frame.grid(column="3", ipadx="5", ipady="5", padx="5", pady="5", row="4")
        # Vermillion Hereafter Frame
        self.vermillion_frame = ttk.Labelframe(self.mainframe2_five_star_artifacts)
        self.vermillion_button1 = ttk.Button(self.vermillion_frame)
        self.vermillion_button1.configure(image=self.vermillion_flower_img,command=self.vermillion_click1,bootstyle="dark-outline")
        self.vermillion_button1.grid(column="0", padx="2", pady="2", row="0")
        self.vermillion_button2 = ttk.Button(self.vermillion_frame)
        self.vermillion_button2.configure(image=self.vermillion_feather_img,command=self.vermillion_click2,bootstyle="dark-outline")
        self.vermillion_button2.grid(column="1", padx="2", pady="2", row="0")
        self.vermillion_button3 = ttk.Button(self.vermillion_frame)
        self.vermillion_button3.configure(image=self.vermillion_sands_img,command=self.vermillion_click3,bootstyle="dark-outline")
        self.vermillion_button3.grid(column="2", padx="2", pady="2", row="0")
        self.vermillion_button4 = ttk.Button(self.vermillion_frame)
        self.vermillion_button4.configure(image=self.vermillion_goblet_img,command=self.vermillion_click4,bootstyle="dark-outline")
        self.vermillion_button4.grid(column="3", padx="2", pady="2", row="0")
        self.vermillion_button5 = ttk.Button(self.vermillion_frame)
        self.vermillion_button5.configure(image=self.vermillion_circlet_img,command=self.vermillion_click5,bootstyle="dark-outline")
        self.vermillion_button5.grid(column="4", padx="2", pady="2", row="0")
        self.vermillion_frame.configure(height="200", text="Vermillion Hereafter", width="200")
        self.vermillion_frame.grid(column="1", ipadx="5", ipady="5", padx="5", pady="5", row="5")
        # Echoes of an Offering Frame
        self.echoes_offering_frame = ttk.Labelframe(self.mainframe2_five_star_artifacts)
        self.echoes_button1 = ttk.Button(self.echoes_offering_frame)
        self.echoes_button1.configure(image=self.echoes_flower_img,command=self.echoes_click1,bootstyle="dark-outline")
        self.echoes_button1.grid(column="0", padx="2", pady="2", row="0")
        self.echoes_button2 = ttk.Button(self.echoes_offering_frame)
        self.echoes_button2.configure(image=self.echoes_feather_img,command=self.echoes_click2,bootstyle="dark-outline")
        self.echoes_button2.grid(column="1", padx="2", pady="2", row="0")
        self.echoes_button3 = ttk.Button(self.echoes_offering_frame)
        self.echoes_button3.configure(image=self.echoes_sands_img,command=self.echoes_click3,bootstyle="dark-outline")
        self.echoes_button3.grid(column="2", padx="2", pady="2", row="0")
        self.echoes_button4 = ttk.Button(self.echoes_offering_frame)
        self.echoes_button4.configure(image=self.echoes_goblet_img,command=self.echoes_click4,bootstyle="dark-outline")
        self.echoes_button4.grid(column="3", padx="2", pady="2", row="0")
        self.echoes_button5 = ttk.Button(self.echoes_offering_frame)
        self.echoes_button5.configure(image=self.echoes_circlet_img,command=self.echoes_click5,bootstyle="dark-outline")
        self.echoes_button5.grid(column="4", padx="2", pady="2", row="0")
        self.echoes_offering_frame.configure(height="200", text="Echoes of an Offering", width="200")
        self.echoes_offering_frame.grid(column="2", ipadx="5", ipady="5", padx="5", pady="5", row="5")

        # mainframe2_five_star_artifacts config and grid

        # MAINFRAME2 END

        # Spawn Entity // Main Tab 2
        self.mainframe1_spawn_entity = ttk.Labelframe(self.main_tabs_notebook)
        self.mainframe1_spawn_entity.configure(height="200", text="", width="200",borderwidth="0")
        self.mainframe1_spawn_entity.grid(column="0", row="0",padx="5",pady="5")
        # bigframe1_spawn_entity
        self.bigframe1_spawn_entity = ttk.Labelframe(self.mainframe1_spawn_entity)
        self.bigframe1_spawn_entity.configure(height="200", text="", width="200")
        self.bigframe1_spawn_entity.grid(column="0", ipadx="50", ipady="50", padx="10", pady="10", row="0")

        self.select_entity_label = ttk.Label(self.bigframe1_spawn_entity)
        self.select_entity_label.configure(text="Select Elite Enemy")
        self.select_entity_label.grid(column="0", padx="5", pady="5", row="0")
        self.select_entity_combobox = ttk.Combobox(self.bigframe1_spawn_entity)
        self.select_entity_combobox.configure(width="50",values=elite_enemies_list,state="readonly")
        self.select_entity_combobox.grid(column="1", padx="5", pady="5", row="0")
        self.amount_label = ttk.Label(self.bigframe1_spawn_entity)
        self.amount_label.configure(text="Amount")
        self.amount_label.grid(column="2", padx="5", pady="5", row="0")

        self.amount_spixbox_spawn_entity = ttk.Spinbox(self.bigframe1_spawn_entity)
        self.amount_spixbox_defaultvalue = tk.IntVar(value="1")
        self.amount_spixbox_spawn_entity.configure(from_="1", increment="1", to="100", width="5",textvariable=self.amount_spixbox_defaultvalue)
        self.amount_spixbox_spawn_entity.grid(column="3", padx="5", pady="5", row="0")
        self.level_label = ttk.Label(self.bigframe1_spawn_entity)
        self.level_label.configure(text="Enemy Level")
        self.level_label.grid(column="4", padx="5", pady="5", row="0")
        self.level_spinbox_spawn_entity = ttk.Spinbox(self.bigframe1_spawn_entity)
        self.level_spinbox_spawn_entity_defaultvalue = tk.IntVar(value="90")
        self.level_spinbox_spawn_entity.configure(from_="0", increment="10", to="200", width="5",textvariable=self.level_spinbox_spawn_entity_defaultvalue)
        self.level_spinbox_spawn_entity.grid(column="5", row="0")
        # bigframe2_spawn_entity
        self.bigframe2_spawn_entity = ttk.Labelframe(self.mainframe1_spawn_entity)
        self.bigframe2_spawn_entity.configure(height="200", text="", width="200")
        self.bigframe2_spawn_entity.grid(column="0", row="1", ipadx="10", ipady="10", padx="10", pady="10",sticky="nw")
        self.spawn_entity_command_text = tk.Text(self.bigframe2_spawn_entity)
        self.spawn_entity_command_text.configure(height="1", width="55")
        default_text_spawn_entity = """/spawn"""
        self.spawn_entity_command_text.insert("0.0", default_text_spawn_entity)
        self.spawn_entity_command_text.grid(column="0", padx="5", pady="5", row="0")
        self.frame1_spawn_entity = ttk.Labelframe(self.bigframe2_spawn_entity)
        self.frame1_spawn_entity.configure(height="200", text="", width="200")
        self.frame1_spawn_entity.grid(column="0", row="1")
        self.submit_button_spawn_entity = ttk.Button(self.frame1_spawn_entity)
        self.submit_button_spawn_entity.configure(text="Generate Command",command=self.spawn_entity_result)
        self.submit_button_spawn_entity.grid(column="0", padx="5", pady="5", row="0")
        self.copy_button_spawn_entity = ttk.Button(self.frame1_spawn_entity)
        self.copy_button_spawn_entity.configure(text="Copy",command=self.copy_function_spawn_entity)
        self.copy_button_spawn_entity.grid(column="1", padx="5", pady="5", row="0")
        self.reset_button_spawn_entity = ttk.Button(self.frame1_spawn_entity)
        self.reset_button_spawn_entity.configure(text="Reset",command=self.reset_function_spawn_entity)
        self.reset_button_spawn_entity.grid(column="2", padx="5", pady="5", row="0")

        # Hu tao Button Spawn Enemy Tab
        self.button2_hu_tao = ttk.Button(self.mainframe1_spawn_entity)
        self.hu_tao_img2 = PhotoImage(file="images/enemy.png")
        self.button2_hu_tao.configure(image=self.hu_tao_img2,bootstyle="info-outline",command=self.hu_tao_prank1)
        self.button2_hu_tao.grid(column="1",row="0",ipadx="0",ipady="0",padx="10",pady="10",sticky="NW")

        # Give Item Tab
        self.mainframe1_give_item = ttk.Labelframe(self.main_tabs_notebook)
        self.mainframe1_give_item.configure(height="200", width="200",borderwidth="0")
        self.mainframe1_give_item.grid(column="0", row="0")

        self.bigframe1_give_item = ttk.Labelframe(self.mainframe1_give_item)
        self.bigframe1_give_item.configure(height="200", text="", width="200")
        self.bigframe1_give_item.grid(column="0", padx="10", pady="5", row="0",ipadx="25",ipady="25")

        self.uid_label_give_item = ttk.Label(self.bigframe1_give_item)
        self.uid_label_give_item.configure(text="UID :")
        self.uid_label_give_item.grid(column="0", padx="5", pady="5", row="0")

        self.uid_entry1_give_item = ttk.Entry(self.bigframe1_give_item)
        self.uid_entry1_give_item.grid(column="1", padx="5", pady="5", row="0")

        self.select_item_list_label = ttk.Label(self.bigframe1_give_item)
        self.select_item_list_label.configure(text="Select Item List")
        self.select_item_list_label.grid(column="2", padx="5", pady="5", row="1")

        self.optionmenu1_var = tk.StringVar()
        self.optionmenu1_var.set(optionmenu1_list[0])

        self.optionmenu1_give_item = tk.OptionMenu(self.bigframe1_give_item,self.optionmenu1_var, *optionmenu1_list ,command=self.get_selected_optionmenu1)
        self.optionmenu1_give_item.grid(column="3", padx="5", pady="5", row="1")

        self.item_label_give_item = ttk.Label(self.bigframe1_give_item)
        self.item_label_give_item.configure(text="Item :")
        self.item_label_give_item.grid(column="2", padx="5", pady="5", row="0")

        self.item_combobox_give_item = ttk.Combobox(self.bigframe1_give_item)
        self.item_combobox_give_item.set("Aquila Favonia")
        self.item_combobox_give_item.configure(state="readonly",values=five_star_swords_list,width="30")
        self.item_combobox_give_item.grid(column="3", padx="5", pady="5", row="0")

        self.amount_label_give_item = ttk.Label(self.bigframe1_give_item)
        self.amount_label_give_item.configure(text="Amount :")
        self.amount_label_give_item.grid(column="4", row="0")

        self.amount_spinbox1_default_value = tk.IntVar(value="1")
        self.amount_spinbox1_give_item = ttk.Spinbox(self.bigframe1_give_item)
        self.amount_spinbox1_give_item.configure(from_="1", increment="1", to="100", width="10",textvariable=self.amount_spinbox1_default_value)
        self.amount_spinbox1_give_item.grid(column="5", padx="5", pady="5", row="0")

        self.level_label_give_item = ttk.Label(self.bigframe1_give_item)
        self.level_label_give_item.configure(text="Level :")
        self.level_label_give_item.grid(column="6", padx="5", pady="5", row="0")

        self.level_entry_give_item = ttk.Entry(self.bigframe1_give_item)
        self.level_entry_give_item.configure(width="10")
        self.level_entry_give_item.insert("0","90")
        self.level_entry_give_item.grid(column="7", padx="5", pady="5", row="0")

        self.refinement_label_give_item = ttk.Label(self.bigframe1_give_item)
        self.refinement_label_give_item.configure(text="Refinement :")
        self.refinement_label_give_item.grid(column="8", padx="5", pady="5", row="0")

        self.refinement_entry_give_item = ttk.Entry(self.bigframe1_give_item)
        self.refinement_entry_give_item.configure(width="10")
        self.refinement_entry_give_item.insert("0","5")
        self.refinement_entry_give_item.grid(column="9", padx="5", pady="5", row="0")

        self.bigframe2_give_item = ttk.Labelframe(self.mainframe1_give_item)
        self.bigframe2_give_item.configure(height="200", text="", width="200")
        self.bigframe2_give_item.grid(column="0", padx="10", pady="5", row="1",sticky="nw")

        self.give_item_command_text1 = tk.Text(self.bigframe2_give_item)
        self.give_item_command_text1.configure(height="1", width="60")
        _text_ = """/give @"""
        self.give_item_command_text1.insert("0.0", _text_)
        self.give_item_command_text1.grid(column="0", row="0")
        self.frame1_give_item = ttk.Labelframe(self.bigframe2_give_item)
        self.frame1_give_item.configure(height="200", text="", width="200")
        self.frame1_give_item.grid(column="0", row="1")
        self.submit_button_give_item = ttk.Button(self.frame1_give_item)
        self.submit_button_give_item.configure(text="Generate Command",command=self.give_item_result_function)
        self.submit_button_give_item.grid(column="0", padx="5", pady="5", row="0")
        self.copy_button_give_item = ttk.Button(self.frame1_give_item)
        self.copy_button_give_item.configure(text="Copy",command=self.copy_function_give_item)
        self.copy_button_give_item.grid(column="1", padx="5", pady="5", row="0")

        # Hu Tao Button Give Weapon Tab

        self.button3_hu_tao = ttk.Button(self.mainframe1_give_item)
        self.hu_tao_img3 = PhotoImage(file="images/weapon.png")
        self.button3_hu_tao.configure(image=self.hu_tao_img3,bootstyle="info-outline",command=self.hu_tao_prank2)
        self.button3_hu_tao.grid(column="1",row="0",ipadx="0",ipady="0",padx="10",pady="10",sticky="NW")

        # About Tab
        self.mainframe1_about_tab = ttk.Labelframe(self.main_tabs_notebook,borderwidth="0")
        self.button4_hu_tao = ttk.Button(self.mainframe1_about_tab)
        self.hu_tao_img4 = PhotoImage(file="images/uwu.png")
        self.button4_hu_tao.configure(image=self.hu_tao_img4,bootstyle="info-outline",command=self.hu_tao_prank3)
        self.button4_hu_tao.grid(column="0",row="0",ipadx="500",ipady="100",padx="0",pady="10")
        self.about_label = ttk.Label(self.mainframe1_about_tab)
        self.about_label.configure(text="Thank you for using my program <3 Report bugs in my DM's and feedbacks are welcome too",font=50)
        self.about_label.grid(column="0",row="1")




        # Notebook Add Tabs
        self.main_tabs_notebook.add(self.artifact_tabs_notebook,text="Create Artifact")
        self.main_tabs_notebook.add(self.mainframe1_spawn_entity, text="Spawn Elite Enemy")
        self.main_tabs_notebook.add(self.mainframe1_give_item, text="Give Weapon")
        self.main_tabs_notebook.add(self.mainframe1_about_tab, text="About")

        self.artifact_tabs_notebook.add(self.mainframe1_edit_tab, text="Edit Artifact")
        self.artifact_tabs_notebook.add(self.mainframe2_five_star_artifacts,text="5* Artifacts")
        # main_window config and grid
        #self.main_window.configure(height="600", width="600")
        self.main_window.grid(column="0", row="0")
        # Main widget
        self.mainwindow = self.main_window

    def run(self):
        self.mainwindow.mainloop()

    def hu_tao_prank1(self):
        self.spawn_entity_command_text.delete("0.0","end")
        self.spawn_entity_command_text.insert("0.0","wow such many empty space")

    def hu_tao_prank2(self):
        self.give_item_command_text1.delete("0.0","end")
        self.give_item_command_text1.insert("0.0","犬も食わない")

    def hu_tao_prank3(self):
        clipboard.copy("https://youtu.be/UIp6_0kct_U")
        self.main_window.bell()

    def copy_function_give_item(self):
        clipboard.copy(str(self.give_item_command_text1.get("0.0", "end")))
        self.main_window.bell()

    def give_item_result_function(self):
        listvar = [
            str(self.item_combobox_give_item.get())
        ]
        item_final_translation = ""
        for line in listvar:
            line = line.rstrip()
            if not line:
                continue
            for item_name, item_id in item_translation.items():
                if item_name in line:
                    line = line.replace(item_name, str(item_id))
                    item_final_translation = item_final_translation + " " + line
        item_command_result = f"/give @{self.uid_entry1_give_item.get()}{item_final_translation} {self.amount_spinbox1_give_item.get()} {self.level_entry_give_item.get()} {self.refinement_entry_give_item.get()}"
        self.give_item_command_text1.delete("0.0", "end")
        self.give_item_command_text1.insert("0.0", item_command_result)


    def get_selected_optionmenu1(self,selected_option):
        if selected_option == "5 Star Swords":
            self.item_combobox_give_item.set("")
            self.item_combobox_give_item.configure(values=five_star_swords_list)
        elif selected_option == "4 Star Swords":
            self.item_combobox_give_item.set("")
            self.item_combobox_give_item.configure(values=four_star_swords_list)
        elif selected_option == "3 Star Swords":
            self.item_combobox_give_item.set("")
            self.item_combobox_give_item.configure(values=three_star_swords_list)
        elif selected_option == "5 Star Claymores":
            self.item_combobox_give_item.set("")
            self.item_combobox_give_item.configure(values=five_star_claymore_list)
        elif selected_option == "4 Star Claymores":
            self.item_combobox_give_item.set("")
            self.item_combobox_give_item.configure(values=four_star_claymore_list)
        elif selected_option == "3 Star Claymores":
            self.item_combobox_give_item.set("")
            self.item_combobox_give_item.configure(values=three_star_claymore_list)
        elif selected_option == "5 Star Polearms":
            self.item_combobox_give_item.set("")
            self.item_combobox_give_item.configure(values=five_star_polearm_list)
        elif selected_option == "4 Star Polearms":
            self.item_combobox_give_item.set("")
            self.item_combobox_give_item.configure(values=four_star_polearm_list)
        elif selected_option == "3 Star Polearms":
            self.item_combobox_give_item.set("")
            self.item_combobox_give_item.configure(values=three_star_polearm_list)
        elif selected_option == "5 Star Catalysts":
            self.item_combobox_give_item.set("")
            self.item_combobox_give_item.configure(values=five_star_catalyst_list)
        elif selected_option == "4 Star Catalysts":
            self.item_combobox_give_item.set("")
            self.item_combobox_give_item.configure(values=four_star_catalyst_list)
        elif selected_option == "3 Star Catalysts":
            self.item_combobox_give_item.set("")
            self.item_combobox_give_item.configure(values=three_star_catalyst_list)
        elif selected_option == "5 Star Bows":
            self.item_combobox_give_item.set("")
            self.item_combobox_give_item.configure(values=five_star_bow_list)
        elif selected_option == "4 Star Bows":
            self.item_combobox_give_item.set("")
            self.item_combobox_give_item.configure(values=four_star_bow_list)
        elif selected_option == "3 Star Bows":
            self.item_combobox_give_item.set("")
            self.item_combobox_give_item.configure(values=three_star_bow_list)

    def artifact_command_result(self):
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
        artifact_level = int(self.spinbox1.get()) + 1
        for line in listvar:
            line = line.rstrip()
            if not line:
                continue
            for stat_name, stat_id in stat_translation.items():
                if stat_name in line:
                    line = line.replace(stat_name, str(stat_id))
                    stats_final_translation = stats_final_translation + " " + line
        final_command_result = f"gart @{self.uid_entry.get()} {self.artifact_entry.get()}{stats_final_translation} {artifact_level}"
        self.final_result.delete("0.0", "end")
        self.final_result.insert("0.0", final_command_result)



    def spawn_entity_result(self):
        listvar = [
            str(self.select_entity_combobox.get())
        ]
        enemy_final_translation = ""
        for line in listvar:
            line = line.rstrip()
            if not line:
                continue
            for enemy_name, enemy_id in all_enemies_list_translation.items():
                if enemy_name in line:
                    line = line.replace(enemy_name, str(enemy_id))
                    enemy_final_translation = enemy_final_translation + " " + line
        spawn_command_result = f"/spawn{enemy_final_translation} {self.amount_spixbox_spawn_entity.get()} {self.level_spinbox_spawn_entity.get()}"
        self.spawn_entity_command_text.delete("0.0","end")
        self.spawn_entity_command_text.insert("0.0",spawn_command_result)

    def copy_function_artifact(self):
        clipboard.copy(str(self.final_result.get("0.0","end")))
        self.main_window.bell()

    def copy_function_spawn_entity(self):
        clipboard.copy(str(self.spawn_entity_command_text.get("0.0","end")))
        self.main_window.bell()

    def clear_function(self):
        self.artifact_entry.delete(0, "end")
        self.selected_artifact_button.configure(image="",text="Click Here to Select")
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

    def reset_function_spawn_entity(self):
        self.spawn_entity_command_text.delete("0.0","end")
        self.select_entity_combobox.set("")
        self.amount_spixbox_spawn_entity

    def go_to_tab(self):
        self.artifact_tabs_notebook.select(1)

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

    def clear_subplus_comboboxes(self): # clear subplus1-5 comboboxes function
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

    # 5* Artifacts Tab Buttons Functions
    def gladiator_click1(self):
        self.artifact_entry.delete(0,"end")
        self.artifact_entry.insert(0,23414)
        self.selected_artifact_button.configure(image=self.gladiator_flower_img,text="Flower", compound=LEFT)
        self.artifact_tabs_notebook.select(0)

    def gladiator_click2(self):
        self.artifact_entry.delete(0,"end")
        self.artifact_entry.insert(0,23412)
        self.selected_artifact_button.configure(image=self.gladiator_feather_img,text="Feather", compound=LEFT)
        self.artifact_tabs_notebook.select(0)

    def gladiator_click3(self):
        self.artifact_entry.delete(0, "end")
        self.artifact_entry.insert(0, 23415)
        self.selected_artifact_button.configure(image=self.gladiator_sands_img,text="Sands", compound=LEFT)
        self.artifact_tabs_notebook.select(0)

    def gladiator_click4(self):
        self.artifact_entry.delete(0, "end")
        self.artifact_entry.insert(0, 23411)
        self.selected_artifact_button.configure(image=self.gladiator_goblet_img,text="Goblet", compound=LEFT)
        self.artifact_tabs_notebook.select(0)

    def gladiator_click5(self):
        self.artifact_entry.delete(0, "end")
        self.artifact_entry.insert(0, 23413)
        self.selected_artifact_button.configure(image=self.gladiator_circlet_img,text="Circlet", compound=LEFT)
        self.artifact_tabs_notebook.select(0)

    def wanderer_click1(self):
        self.artifact_entry.delete(0, "end")
        self.artifact_entry.insert(0, 23394)
        self.selected_artifact_button.configure(image=self.wanderer_flower_img, text="Flower", compound=LEFT)
        self.artifact_tabs_notebook.select(0)

    def wanderer_click2(self):
        self.artifact_entry.delete(0, "end")
        self.artifact_entry.insert(0, 23392)
        self.selected_artifact_button.configure(image=self.wanderer_feather_img, text="Feather", compound=LEFT)
        self.artifact_tabs_notebook.select(0)

    def wanderer_click3(self):
        self.artifact_entry.delete(0, "end")
        self.artifact_entry.insert(0, 23395)
        self.selected_artifact_button.configure(image=self.wanderer_sands_img, text="Sands", compound=LEFT)
        self.artifact_tabs_notebook.select(0)

    def wanderer_click4(self):
        self.artifact_entry.delete(0, "end")
        self.artifact_entry.insert(0, 23391)
        self.selected_artifact_button.configure(image=self.wanderer_goblet_img, text="Goblet", compound=LEFT)
        self.artifact_tabs_notebook.select(0)

    def wanderer_click5(self):
        self.artifact_entry.delete(0, "end")
        self.artifact_entry.insert(0, 23393)
        self.selected_artifact_button.configure(image=self.wanderer_circlet_img, text="Circlet", compound=LEFT)
        self.artifact_tabs_notebook.select(0)

    def noblesse_click1(self):
        self.artifact_entry.delete(0, "end")
        self.artifact_entry.insert(0, 23354)
        self.selected_artifact_button.configure(image=self.noblesse_flower_img, text="Flower", compound=LEFT)
        self.artifact_tabs_notebook.select(0)

    def noblesse_click2(self):
        self.artifact_entry.delete(0, "end")
        self.artifact_entry.insert(0, 23352)
        self.selected_artifact_button.configure(image=self.noblesse_feather_img, text="Feather", compound=LEFT)
        self.artifact_tabs_notebook.select(0)

    def noblesse_click3(self):
        self.artifact_entry.delete(0, "end")
        self.artifact_entry.insert(0, 23355)
        self.selected_artifact_button.configure(image=self.noblesse_sands_img, text="Sands", compound=LEFT)
        self.artifact_tabs_notebook.select(0)

    def noblesse_click4(self):
        self.artifact_entry.delete(0, "end")
        self.artifact_entry.insert(0, 23351)
        self.selected_artifact_button.configure(image=self.noblesse_goblet_img, text="Goblet", compound=LEFT)
        self.artifact_tabs_notebook.select(0)

    def noblesse_click5(self):
        self.artifact_entry.delete(0, "end")
        self.artifact_entry.insert(0, 23353)
        self.selected_artifact_button.configure(image=self.noblesse_circlet_img, text="Circlet", compound=LEFT)
        self.artifact_tabs_notebook.select(0)

    def chivarly_click1(self):
        self.artifact_entry.delete(0, "end")
        self.artifact_entry.insert(0, 23344)
        self.selected_artifact_button.configure(image=self.chivarly_flower_img, text="Flower", compound=LEFT)
        self.artifact_tabs_notebook.select(0)

    def chivarly_click2(self):
        self.artifact_entry.delete(0, "end")
        self.artifact_entry.insert(0, 23342)
        self.selected_artifact_button.configure(image=self.chivarly_feather_img, text="Feather", compound=LEFT)
        self.artifact_tabs_notebook.select(0)

    def chivarly_click3(self):
        self.artifact_entry.delete(0, "end")
        self.artifact_entry.insert(0, 23345)
        self.selected_artifact_button.configure(image=self.chivarly_sands_img, text="Sands", compound=LEFT)
        self.artifact_tabs_notebook.select(0)

    def chivarly_click4(self):
        self.artifact_entry.delete(0, "end")
        self.artifact_entry.insert(0, 23341)
        self.selected_artifact_button.configure(image=self.chivarly_goblet_img, text="Goblet", compound=LEFT)
        self.artifact_tabs_notebook.select(0)

    def chivarly_click5(self):
        self.artifact_entry.delete(0, "end")
        self.artifact_entry.insert(0, 23343)
        self.selected_artifact_button.configure(image=self.chivarly_circlet_img, text="Circlet", compound=LEFT)
        self.artifact_tabs_notebook.select(0)

    def maiden_click1(self):
        self.artifact_entry.delete(0, "end")
        self.artifact_entry.insert(0, 23424)
        self.selected_artifact_button.configure(image=self.maiden_flower_img, text="Flower", compound=LEFT)
        self.artifact_tabs_notebook.select(0)

    def maiden_click2(self):
        self.artifact_entry.delete(0, "end")
        self.artifact_entry.insert(0, 23422)
        self.selected_artifact_button.configure(image=self.maiden_feather_img, text="Feather", compound=LEFT)
        self.artifact_tabs_notebook.select(0)

    def maiden_click3(self):
        self.artifact_entry.delete(0, "end")
        self.artifact_entry.insert(0, 23425)
        self.selected_artifact_button.configure(image=self.maiden_sands_img, text="Sands", compound=LEFT)
        self.artifact_tabs_notebook.select(0)

    def maiden_click4(self):
        self.artifact_entry.delete(0, "end")
        self.artifact_entry.insert(0, 23421)
        self.selected_artifact_button.configure(image=self.maiden_goblet_img, text="Goblet", compound=LEFT)
        self.artifact_tabs_notebook.select(0)

    def maiden_click5(self):
        self.artifact_entry.delete(0, "end")
        self.artifact_entry.insert(0, 23423)
        self.selected_artifact_button.configure(image=self.maiden_circlet_img, text="Circlet", compound=LEFT)
        self.artifact_tabs_notebook.select(0)

    def venerer_click1(self):
        self.artifact_entry.delete(0, "end")
        self.artifact_entry.insert(0, 23404)
        self.selected_artifact_button.configure(image=self.venerer_flower_img, text="Flower", compound=LEFT)
        self.artifact_tabs_notebook.select(0)

    def venerer_click2(self):
        self.artifact_entry.delete(0, "end")
        self.artifact_entry.insert(0, 23402)
        self.selected_artifact_button.configure(image=self.venerer_feather_img, text="Feather", compound=LEFT)
        self.artifact_tabs_notebook.select(0)

    def venerer_click3(self):
        self.artifact_entry.delete(0, "end")
        self.artifact_entry.insert(0, 23405)
        self.selected_artifact_button.configure(image=self.venerer_sands_img, text="Sands", compound=LEFT)
        self.artifact_tabs_notebook.select(0)

    def venerer_click4(self):
        self.artifact_entry.delete(0, "end")
        self.artifact_entry.insert(0, 23401)
        self.selected_artifact_button.configure(image=self.venerer_goblet_img, text="Goblet", compound=LEFT)
        self.artifact_tabs_notebook.select(0)

    def venerer_click5(self):
        self.artifact_entry.delete(0, "end")
        self.artifact_entry.insert(0, 23403)
        self.selected_artifact_button.configure(image=self.venerer_circlet_img, text="Circlet", compound=LEFT)
        self.artifact_tabs_notebook.select(0)

    def petra_click1(self):
        self.artifact_entry.delete(0, "end")
        self.artifact_entry.insert(0, 23494)
        self.selected_artifact_button.configure(image=self.petra_flower_img, text="Flower", compound=LEFT)
        self.artifact_tabs_notebook.select(0)

    def petra_click2(self):
        self.artifact_entry.delete(0, "end")
        self.artifact_entry.insert(0, 23492)
        self.selected_artifact_button.configure(image=self.petra_feather_img, text="Feather", compound=LEFT)
        self.artifact_tabs_notebook.select(0)

    def petra_click3(self):
        self.artifact_entry.delete(0, "end")
        self.artifact_entry.insert(0, 23495)
        self.selected_artifact_button.configure(image=self.petra_sands_img, text="Sands", compound=LEFT)
        self.artifact_tabs_notebook.select(0)

    def petra_click4(self):
        self.artifact_entry.delete(0, "end")
        self.artifact_entry.insert(0, 23491)
        self.selected_artifact_button.configure(image=self.petra_goblet_img, text="Goblet", compound=LEFT)
        self.artifact_tabs_notebook.select(0)

    def petra_click5(self):
        self.artifact_entry.delete(0, "end")
        self.artifact_entry.insert(0, 23493)
        self.selected_artifact_button.configure(image=self.petra_circlet_img, text="Circlet", compound=LEFT)
        self.artifact_tabs_notebook.select(0)

    def bolide_click1(self):
        self.artifact_entry.delete(0, "end")
        self.artifact_entry.insert(0, 23504)
        self.selected_artifact_button.configure(image=self.bolide_flower_img, text="Flower", compound=LEFT)
        self.artifact_tabs_notebook.select(0)

    def bolide_click2(self):
        self.artifact_entry.delete(0, "end")
        self.artifact_entry.insert(0, 23502)
        self.selected_artifact_button.configure(image=self.bolide_feather_img, text="Feather", compound=LEFT)
        self.artifact_tabs_notebook.select(0)

    def bolide_click3(self):
        self.artifact_entry.delete(0, "end")
        self.artifact_entry.insert(0, 23505)
        self.selected_artifact_button.configure(image=self.bolide_sands_img, text="Sands", compound=LEFT)
        self.artifact_tabs_notebook.select(0)

    def bolide_click4(self):
        self.artifact_entry.delete(0, "end")
        self.artifact_entry.insert(0, 23501)
        self.selected_artifact_button.configure(image=self.bolide_goblet_img, text="Goblet", compound=LEFT)
        self.artifact_tabs_notebook.select(0)

    def bolide_click5(self):
        self.artifact_entry.delete(0, "end")
        self.artifact_entry.insert(0, 23503)
        self.selected_artifact_button.configure(image=self.bolide_circlet_img, text="Circlet", compound=LEFT)
        self.artifact_tabs_notebook.select(0)

    def thundersoother_click1(self):
        self.artifact_entry.delete(0, "end")
        self.artifact_entry.insert(0, 23444)
        self.selected_artifact_button.configure(image=self.thundersoother_flower_img, text="Flower", compound=LEFT)
        self.artifact_tabs_notebook.select(0)

    def thundersoother_click2(self):
        self.artifact_entry.delete(0, "end")
        self.artifact_entry.insert(0, 23442)
        self.selected_artifact_button.configure(image=self.thundersoother_feather_img, text="Feather", compound=LEFT)
        self.artifact_tabs_notebook.select(0)

    def thundersoother_click3(self):
        self.artifact_entry.delete(0, "end")
        self.artifact_entry.insert(0, 23445)
        self.selected_artifact_button.configure(image=self.thundersoother_sands_img, text="Sands", compound=LEFT)
        self.artifact_tabs_notebook.select(0)

    def thundersoother_click4(self):
        self.artifact_entry.delete(0, "end")
        self.artifact_entry.insert(0, 23441)
        self.selected_artifact_button.configure(image=self.thundersoother_goblet_img, text="Goblet", compound=LEFT)
        self.artifact_tabs_notebook.select(0)

    def thundersoother_click5(self):
        self.artifact_entry.delete(0, "end")
        self.artifact_entry.insert(0, 23443)
        self.selected_artifact_button.configure(image=self.thundersoother_circlet_img, text="Circlet", compound=LEFT)
        self.artifact_tabs_notebook.select(0)

    def thundering_click1(self):
        self.artifact_entry.delete(0, "end")
        self.artifact_entry.insert(0, 23374)
        self.selected_artifact_button.configure(image=self.thundering_flower_img, text="Flower", compound=LEFT)
        self.artifact_tabs_notebook.select(0)

    def thundering_click2(self):
        self.artifact_entry.delete(0, "end")
        self.artifact_entry.insert(0, 23372)
        self.selected_artifact_button.configure(image=self.thundering_feather_img, text="Feather", compound=LEFT)
        self.artifact_tabs_notebook.select(0)

    def thundering_click3(self):
        self.artifact_entry.delete(0, "end")
        self.artifact_entry.insert(0, 23375)
        self.selected_artifact_button.configure(image=self.thundering_sands_img, text="Sands", compound=LEFT)
        self.artifact_tabs_notebook.select(0)

    def thundering_click4(self):
        self.artifact_entry.delete(0, "end")
        self.artifact_entry.insert(0, 23371)
        self.selected_artifact_button.configure(image=self.thundering_goblet_img, text="Goblet", compound=LEFT)
        self.artifact_tabs_notebook.select(0)

    def thundering_click5(self):
        self.artifact_entry.delete(0, "end")
        self.artifact_entry.insert(0, 23373)
        self.selected_artifact_button.configure(image=self.thundering_circlet_img, text="Circlet", compound=LEFT)
        self.artifact_tabs_notebook.select(0)

    def lavawalker_click1(self):
        self.artifact_entry.delete(0, "end")
        self.artifact_entry.insert(0, 23434)
        self.selected_artifact_button.configure(image=self.thundering_flower_img, text="Flower", compound=LEFT)
        self.artifact_tabs_notebook.select(0)

    def lavawalker_click2(self):
        self.artifact_entry.delete(0, "end")
        self.artifact_entry.insert(0, 23432)
        self.selected_artifact_button.configure(image=self.lavawalker_feather_img, text="Feather", compound=LEFT)
        self.artifact_tabs_notebook.select(0)

    def lavawalker_click3(self):
        self.artifact_entry.delete(0, "end")
        self.artifact_entry.insert(0, 23435)
        self.selected_artifact_button.configure(image=self.lavawalker_sands_img, text="Sands", compound=LEFT)
        self.artifact_tabs_notebook.select(0)

    def lavawalker_click4(self):
        self.artifact_entry.delete(0, "end")
        self.artifact_entry.insert(0, 23431)
        self.selected_artifact_button.configure(image=self.lavawalker_goblet_img, text="Goblet", compound=LEFT)
        self.artifact_tabs_notebook.select(0)

    def lavawalker_click5(self):
        self.artifact_entry.delete(0, "end")
        self.artifact_entry.insert(0, 23433)
        self.selected_artifact_button.configure(image=self.lavawalker_circlet_img, text="Circlet", compound=LEFT)
        self.artifact_tabs_notebook.select(0)

    def crimson_click1(self):
        self.artifact_entry.delete(0, "end")
        self.artifact_entry.insert(0, 23364)
        self.selected_artifact_button.configure(image=self.crimson_flower_img, text="Flower", compound=LEFT)
        self.artifact_tabs_notebook.select(0)

    def crimson_click2(self):
        self.artifact_entry.delete(0, "end")
        self.artifact_entry.insert(0, 23362)
        self.selected_artifact_button.configure(image=self.crimson_feather_img, text="Feather", compound=LEFT)
        self.artifact_tabs_notebook.select(0)

    def crimson_click3(self):
        self.artifact_entry.delete(0, "end")
        self.artifact_entry.insert(0, 23365)
        self.selected_artifact_button.configure(image=self.crimson_sands_img, text="Sands", compound=LEFT)
        self.artifact_tabs_notebook.select(0)

    def crimson_click4(self):
        self.artifact_entry.delete(0, "end")
        self.artifact_entry.insert(0, 23361)
        self.selected_artifact_button.configure(image=self.crimson_goblet_img, text="Goblet", compound=LEFT)
        self.artifact_tabs_notebook.select(0)

    def crimson_click5(self):
        self.artifact_entry.delete(0, "end")
        self.artifact_entry.insert(0, 23363)
        self.selected_artifact_button.configure(image=self.crimson_circlet_img, text="Circlet", compound=LEFT)
        self.artifact_tabs_notebook.select(0)

    def blizzard_click1(self):
        self.artifact_entry.delete(0, "end")
        self.artifact_entry.insert(0, 23454)
        self.selected_artifact_button.configure(image=self.blizzard_flower_img, text="Flower", compound=LEFT)
        self.artifact_tabs_notebook.select(0)

    def blizzard_click2(self):
        self.artifact_entry.delete(0, "end")
        self.artifact_entry.insert(0, 23452)
        self.selected_artifact_button.configure(image=self.blizzard_feather_img, text="Feather", compound=LEFT)
        self.artifact_tabs_notebook.select(0)

    def blizzard_click3(self):
        self.artifact_entry.delete(0, "end")
        self.artifact_entry.insert(0, 23455)
        self.selected_artifact_button.configure(image=self.blizzard_sands_img, text="Sands", compound=LEFT)
        self.artifact_tabs_notebook.select(0)

    def blizzard_click4(self):
        self.artifact_entry.delete(0, "end")
        self.artifact_entry.insert(0, 23451)
        self.selected_artifact_button.configure(image=self.blizzard_goblet_img, text="Goblet", compound=LEFT)
        self.artifact_tabs_notebook.select(0)

    def blizzard_click5(self):
        self.artifact_entry.delete(0, "end")
        self.artifact_entry.insert(0, 23453)
        self.selected_artifact_button.configure(image=self.blizzard_circlet_img, text="Circlet", compound=LEFT)
        self.artifact_tabs_notebook.select(0)

    def hod_click1(self):
        self.artifact_entry.delete(0, "end")
        self.artifact_entry.insert(0, 23534)
        self.selected_artifact_button.configure(image=self.hod_flower_img, text="Flower", compound=LEFT)
        self.artifact_tabs_notebook.select(0)

    def hod_click2(self):
        self.artifact_entry.delete(0, "end")
        self.artifact_entry.insert(0, 23532)
        self.selected_artifact_button.configure(image=self.hod_feather_img, text="Feather", compound=LEFT)
        self.artifact_tabs_notebook.select(0)

    def hod_click3(self):
        self.artifact_entry.delete(0, "end")
        self.artifact_entry.insert(0, 23535)
        self.selected_artifact_button.configure(image=self.hod_sands_img, text="Sands", compound=LEFT)
        self.artifact_tabs_notebook.select(0)

    def hod_click4(self):
        self.artifact_entry.delete(0, "end")
        self.artifact_entry.insert(0, 23531)
        self.selected_artifact_button.configure(image=self.hod_goblet_img, text="Goblet", compound=LEFT)
        self.artifact_tabs_notebook.select(0)

    def hod_click5(self):
        self.artifact_entry.delete(0, "end")
        self.artifact_entry.insert(0, 23533)
        self.selected_artifact_button.configure(image=self.hod_circlet_img, text="Circlet", compound=LEFT)
        self.artifact_tabs_notebook.select(0)

    def tenacity_click1(self):
        self.artifact_entry.delete(0, "end")
        self.artifact_entry.insert(0, 23544)
        self.selected_artifact_button.configure(image=self.tenacity_flower_img, text="Flower", compound=LEFT)
        self.artifact_tabs_notebook.select(0)

    def tenacity_click2(self):
        self.artifact_entry.delete(0, "end")
        self.artifact_entry.insert(0, 23542)
        self.selected_artifact_button.configure(image=self.tenacity_feather_img, text="Feather", compound=LEFT)
        self.artifact_tabs_notebook.select(0)

    def tenacity_click3(self):
        self.artifact_entry.delete(0, "end")
        self.artifact_entry.insert(0, 23545)
        self.selected_artifact_button.configure(image=self.tenacity_sands_img, text="Sands", compound=LEFT)
        self.artifact_tabs_notebook.select(0)

    def tenacity_click4(self):
        self.artifact_entry.delete(0, "end")
        self.artifact_entry.insert(0, 23541)
        self.selected_artifact_button.configure(image=self.tenacity_goblet_img, text="Goblet", compound=LEFT)
        self.artifact_tabs_notebook.select(0)

    def tenacity_click5(self):
        self.artifact_entry.delete(0, "end")
        self.artifact_entry.insert(0, 23543)
        self.selected_artifact_button.configure(image=self.tenacity_circlet_img, text="Circlet", compound=LEFT)
        self.artifact_tabs_notebook.select(0)

    def paleflame_click1(self):
        self.artifact_entry.delete(0, "end")
        self.artifact_entry.insert(0, 23554)
        self.selected_artifact_button.configure(image=self.paleflame_flower_img, text="Flower", compound=LEFT)
        self.artifact_tabs_notebook.select(0)

    def paleflame_click2(self):
        self.artifact_entry.delete(0, "end")
        self.artifact_entry.insert(0, 23552)
        self.selected_artifact_button.configure(image=self.paleflame_feather_img, text="Feather", compound=LEFT)
        self.artifact_tabs_notebook.select(0)

    def paleflame_click3(self):
        self.artifact_entry.delete(0, "end")
        self.artifact_entry.insert(0, 23555)
        self.selected_artifact_button.configure(image=self.paleflame_sands_img, text="Sands", compound=LEFT)
        self.artifact_tabs_notebook.select(0)

    def paleflame_click4(self):
        self.artifact_entry.delete(0, "end")
        self.artifact_entry.insert(0, 23551)
        self.selected_artifact_button.configure(image=self.paleflame_goblet_img, text="Goblet", compound=LEFT)
        self.artifact_tabs_notebook.select(0)

    def paleflame_click5(self):
        self.artifact_entry.delete(0, "end")
        self.artifact_entry.insert(0, 23553)
        self.selected_artifact_button.configure(image=self.paleflame_circlet_img, text="Circlet", compound=LEFT)
        self.artifact_tabs_notebook.select(0)

    def shimenawa_click1(self):
        self.artifact_entry.delete(0, "end")
        self.artifact_entry.insert(0, 23564)
        self.selected_artifact_button.configure(image=self.shimenawa_flower_img, text="Flower", compound=LEFT)
        self.artifact_tabs_notebook.select(0)

    def shimenawa_click2(self):
        self.artifact_entry.delete(0, "end")
        self.artifact_entry.insert(0, 23562)
        self.selected_artifact_button.configure(image=self.shimenawa_feather_img, text="Feather", compound=LEFT)
        self.artifact_tabs_notebook.select(0)

    def shimenawa_click3(self):
        self.artifact_entry.delete(0, "end")
        self.artifact_entry.insert(0, 23565)
        self.selected_artifact_button.configure(image=self.shimenawa_sands_img, text="Sands", compound=LEFT)
        self.artifact_tabs_notebook.select(0)

    def shimenawa_click4(self):
        self.artifact_entry.delete(0, "end")
        self.artifact_entry.insert(0, 23561)
        self.selected_artifact_button.configure(image=self.shimenawa_goblet_img, text="Goblet", compound=LEFT)
        self.artifact_tabs_notebook.select(0)

    def shimenawa_click5(self):
        self.artifact_entry.delete(0, "end")
        self.artifact_entry.insert(0, 23563)
        self.selected_artifact_button.configure(image=self.shimenawa_circlet_img, text="Circlet", compound=LEFT)
        self.artifact_tabs_notebook.select(0)

    def emblem_click1(self):
        self.artifact_entry.delete(0, "end")
        self.artifact_entry.insert(0, 23574)
        self.selected_artifact_button.configure(image=self.emblem_flower_img, text="Flower", compound=LEFT)
        self.artifact_tabs_notebook.select(0)

    def emblem_click2(self):
        self.artifact_entry.delete(0, "end")
        self.artifact_entry.insert(0, 23572)
        self.selected_artifact_button.configure(image=self.emblem_feather_img, text="Feather", compound=LEFT)
        self.artifact_tabs_notebook.select(0)

    def emblem_click3(self):
        self.artifact_entry.delete(0, "end")
        self.artifact_entry.insert(0, 23575)
        self.selected_artifact_button.configure(image=self.emblem_sands_img, text="Sands", compound=LEFT)
        self.artifact_tabs_notebook.select(0)

    def emblem_click4(self):
        self.artifact_entry.delete(0, "end")
        self.artifact_entry.insert(0, 23571)
        self.selected_artifact_button.configure(image=self.emblem_goblet_img, text="Goblet", compound=LEFT)
        self.artifact_tabs_notebook.select(0)

    def emblem_click5(self):
        self.artifact_entry.delete(0, "end")
        self.artifact_entry.insert(0, 23573)
        self.selected_artifact_button.configure(image=self.emblem_circlet_img, text="Circlet", compound=LEFT)
        self.artifact_tabs_notebook.select(0)

    def husk_click1(self):
        self.artifact_entry.delete(0, "end")
        self.artifact_entry.insert(0, 23584)
        self.selected_artifact_button.configure(image=self.husk_flower_img, text="Flower", compound=LEFT)
        self.artifact_tabs_notebook.select(0)

    def husk_click2(self):
        self.artifact_entry.delete(0, "end")
        self.artifact_entry.insert(0, 23582)
        self.selected_artifact_button.configure(image=self.husk_feather_img, text="Feather", compound=LEFT)
        self.artifact_tabs_notebook.select(0)

    def husk_click3(self):
        self.artifact_entry.delete(0, "end")
        self.artifact_entry.insert(0, 23585)
        self.selected_artifact_button.configure(image=self.husk_sands_img, text="Sands", compound=LEFT)
        self.artifact_tabs_notebook.select(0)

    def husk_click4(self):
        self.artifact_entry.delete(0, "end")
        self.artifact_entry.insert(0, 23581)
        self.selected_artifact_button.configure(image=self.husk_goblet_img, text="Goblet", compound=LEFT)
        self.artifact_tabs_notebook.select(0)

    def husk_click5(self):
        self.artifact_entry.delete(0, "end")
        self.artifact_entry.insert(0, 23583)
        self.selected_artifact_button.configure(image=self.husk_circlet_img, text="Circlet", compound=LEFT)
        self.artifact_tabs_notebook.select(0)

    def oceanclam_click1(self):
        self.artifact_entry.delete(0, "end")
        self.artifact_entry.insert(0, 23594)
        self.selected_artifact_button.configure(image=self.oceanclam_flower_img, text="Flower", compound=LEFT)
        self.artifact_tabs_notebook.select(0)

    def oceanclam_click2(self):
        self.artifact_entry.delete(0, "end")
        self.artifact_entry.insert(0, 23592)
        self.selected_artifact_button.configure(image=self.oceanclam_feather_img, text="Feather", compound=LEFT)
        self.artifact_tabs_notebook.select(0)

    def oceanclam_click3(self):
        self.artifact_entry.delete(0, "end")
        self.artifact_entry.insert(0, 23595)
        self.selected_artifact_button.configure(image=self.oceanclam_sands_img, text="Sands", compound=LEFT)
        self.artifact_tabs_notebook.select(0)

    def oceanclam_click4(self):
        self.artifact_entry.delete(0, "end")
        self.artifact_entry.insert(0, 23591)
        self.selected_artifact_button.configure(image=self.oceanclam_goblet_img, text="Goblet", compound=LEFT)
        self.artifact_tabs_notebook.select(0)

    def oceanclam_click5(self):
        self.artifact_entry.delete(0, "end")
        self.artifact_entry.insert(0, 23593)
        self.selected_artifact_button.configure(image=self.oceanclam_circlet_img, text="Circlet", compound=LEFT)
        self.artifact_tabs_notebook.select(0)

    def vermillion_click1(self):
        self.artifact_entry.delete(0, "end")
        self.artifact_entry.insert(0, 23604)
        self.selected_artifact_button.configure(image=self.vermillion_flower_img, text="Flower", compound=LEFT)
        self.artifact_tabs_notebook.select(0)

    def vermillion_click2(self):
        self.artifact_entry.delete(0, "end")
        self.artifact_entry.insert(0, 23602)
        self.selected_artifact_button.configure(image=self.vermillion_feather_img, text="Feather", compound=LEFT)
        self.artifact_tabs_notebook.select(0)

    def vermillion_click3(self):
        self.artifact_entry.delete(0, "end")
        self.artifact_entry.insert(0, 23605)
        self.selected_artifact_button.configure(image=self.vermillion_sands_img, text="Sands", compound=LEFT)
        self.artifact_tabs_notebook.select(0)

    def vermillion_click4(self):
        self.artifact_entry.delete(0, "end")
        self.artifact_entry.insert(0, 23601)
        self.selected_artifact_button.configure(image=self.vermillion_goblet_img, text="Goblet", compound=LEFT)
        self.artifact_tabs_notebook.select(0)

    def vermillion_click5(self):
        self.artifact_entry.delete(0, "end")
        self.artifact_entry.insert(0, 23603)
        self.selected_artifact_button.configure(image=self.vermillion_circlet_img, text="Circlet", compound=LEFT)
        self.artifact_tabs_notebook.select(0)

    def echoes_click1(self):
        self.artifact_entry.delete(0, "end")
        self.artifact_entry.insert(0, 23614)
        self.selected_artifact_button.configure(image=self.echoes_flower_img, text="Flower", compound=LEFT)
        self.artifact_tabs_notebook.select(0)

    def echoes_click2(self):
        self.artifact_entry.delete(0, "end")
        self.artifact_entry.insert(0, 23612)
        self.selected_artifact_button.configure(image=self.echoes_feather_img, text="Feather", compound=LEFT)
        self.artifact_tabs_notebook.select(0)

    def echoes_click3(self):
        self.artifact_entry.delete(0, "end")
        self.artifact_entry.insert(0, 23615)
        self.selected_artifact_button.configure(image=self.echoes_sands_img, text="Sands", compound=LEFT)
        self.artifact_tabs_notebook.select(0)

    def echoes_click4(self):
        self.artifact_entry.delete(0, "end")
        self.artifact_entry.insert(0, 23611)
        self.selected_artifact_button.configure(image=self.echoes_goblet_img, text="Goblet", compound=LEFT)
        self.artifact_tabs_notebook.select(0)

    def echoes_click5(self):
        self.artifact_entry.delete(0, "end")
        self.artifact_entry.insert(0, 23613)
        self.selected_artifact_button.configure(image=self.echoes_circlet_img, text="Circlet", compound=LEFT)
        self.artifact_tabs_notebook.select(0)


if __name__ == "__main__":
    root = ttk.Window(themename="hu_tao3")
    root.title("Artifact Command Generator by Keithy")
    root.iconbitmap("images/icon.ico")
    root.resizable(False,False)
    app = Artifact_GeneratorApp(root)
    app.run()









