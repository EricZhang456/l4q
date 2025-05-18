"""Map thumbnail utility."""

THUMBNAIL_NAMES = {
    # Dead Center
    "#L4D360UI_CampaignName_C1": {
        "coop": {
            1: "c1m1_hotel",
            2: "c1m2_streets",
            3: "c1m3_mall",
            4: "c1m4_atrium"
        },
        "survival": {
            1: "c1m2_gunshop",
            2: "c1m4_atrium"
        },
        "scavenge": {
            1: "c1m4_atrium"
        }
    },
    # Dark Carnival
    "#L4D360UI_CampaignName_C2": {
        "coop": {
            1: "c2m1_highway",
            2: "c2m2_fairgrounds",
            3: "c2m3_coaster",
            4: "c2m4_barns",
            5: "c2m5_concert"
        },
        "survival": {
            1: "c2m1_motel",
            2: "c2m4_barns",
            3: "c2m5_concert"
        },
        "scavenge": {
            1: "c2m1_motel"
        }
    },
    # Swamp Fever
    "#L4D360UI_CampaignName_C3": {
        "coop": {
            1: "c3m1_plankcountry",
            2: "c3m2_swamp",
            3: "c3m3_shantytown",
            4: "c3m4_plantation"
        },
        "survival": {
            1: "c3m1_village",
            2: "c3m3_shantytown",
            3: "c3m4_plantation"
        },
        "scavenge": {
            1: "c3m1_plankcountry"
        }
    },
    # Hard Rain
    "#L4D360UI_CampaignName_C4" : {
        "coop": {
            1: "c4m1_milltown_a",
            2: "c4m2_sugarmill_a",
            3: "c4m3_sugarmill_b",
            4: "c4m4_milltown_b",
            5: "c4m5_milltown_escape"
        },
        "survival": {
            1: "c4m1_burgertank",
            2: "c4m2_sugarmill_a",
            3: "c4m3_sugarmill_b"
        },
        "scavenge": {
            1: "c4m1_milltown_a",
            2: "c4m2_sugarmill_a",
            3: "c4m3_sugarmill_b"
        }
    },
    # The Parish
    "#L4D360UI_CampaignName_C5": {
        "coop": {
            1: "c5m1_waterfront",
            2: "c5m2_park",
            3: "c5m3_cemetery",
            4: "c5m4_quarter",
            5: "c5m5_bridge"
        },
        "survival": {
            1: "c5m1_waterfront_survival",
            2: "c5m2_busdepot",
            3: "c5m3_cemetery",
            4: "c5m4_float",
            5: "c5m5_bridge_end"
        },
        "scavenge": {
            1: "c5m2_park"
        }
    },
    # The Passing
    "#L4D360UI_CampaignName_C6": {
        "coop": {
            1: "c6m1_riverbank",
            2: "c6m2_bedlam",
            3: "c6m3_port"
        },
        "survival": {
            1: "c6m1_riverbank_survival",
            2: "c6m2_bedlam_survival",
            3: "c6m3_port"
        },
        "scavenge": {
            1: "c6m1_riverbank",
            2: "c6m2_bedlam",
            3: "c6m3_port"
        }
    },
    # The Sacrifice
    "#L4D360UI_CampaignName_C7": {
        "coop": {
            1: "l4d_river01_docks",
            2: "l4d_river02_barge",
            3: "l4d_river03_port"
        },
        "survival": {
            1: "l4d_river01_tankcar",
            2: "l4d_river02_barge",
            3: "l4d_river03_port"
        },
        "scavenge": {
            1: "c7m1_docks_scavenge",
            2: "c7m2_barge_scavenge"
        }
    },
    # No Mercy
    "#L4D360UI_CampaignName_C8": {
        "coop": {
            1: "l4d_hospital01_apartment",
            2: "l4d_hospital02_subway",
            3: "l4d_hospital03_sewers",
            4: "l4d_hospital04_interior",
            5: "l4d_hospital05_rooftop"
        },
        "survival": {
            1: "l4d_hospital02_subway",
            2: "l4d_hospital03_sewers",
            3: "l4d_hospital04_interior",
            4: "l4d_hospital05_rooftop"
        },
        "scavenge": {
            1: "c8m1_apartment_scavenge",
            2: "c8m5_rooftop_scavenge"
        }
    },
    # Crash Course
    "#L4D360UI_CampaignName_C9": {
        "coop": {
            1: "c9m1_alleys",
            2: "c9m2_lots"
        },
        "survival": {
            1: "c9m1_bridge",
            2: "c9m2_depot"
        },
        "scavenge": {
            1: "c9m1_alleys"
        }
    },
    # Death Toll
    "#L4D360UI_CampaignName_C10": {
        "coop": {
            1: "c10m1_caves",
            2: "c10m2_drainage",
            3: "c10m3_ranchhouse",
            4: "c10m4_mainstreet",
            5: "c10m5_houseboat"
        },
        "survival": {
            1: "c10m2_drains",
            2: "c10m3_ranchhouse",
            3: "c10m4_mainstreet",
            4: "c10m5_houseboat"
        },
        "scavenge": {
            1: "c10m3_ranchhouse"
        }
    },
    # Dead Air
    "#L4D360UI_CampaignName_C11": {
        "coop": {
            1: "c11m1_greenhouse",
            2: "c11m2_offices",
            3: "c11m3_garage",
            4: "c11m4_terminal",
            5: "c11m5_runway"
        },
        "survival": {
            1: "c11m2_offices",
            2: "c11m3_garage",
            4: "c11m4_terminal",
            3: "c11m5_runway"
        },
        "scavenge": {
            1: "c11m4_terminal"
        }
    },
    # Blood Harvest
    "#L4D360UI_CampaignName_C12": {
        "coop": {
            1: "c12m1_hilltop",
            2: "c12m2_traintunnel",
            3: "c12m3_bridge",
            4: "c12m4_barn",
            5: "c12m5_cornfield"
        },
        "survival": {
            1: "c12m2_traintunnel",
            2: "c12m3_bridge",
            3: "c12m5_cornfield"
        },
        "scavenge": {
            1: "c12m5_cornfield"
        }
    },
    # Cold Stream
    "#L4D360UI_CampaignName_C13": {
        "coop": {
            1: "c13m1_alpinecreek",
            2: "c13m2_southpinestream",
            3: "c13m3_memorialbridge",
            4: "c13m4_cutthroatcreek"
        },
        "survival": {
            1: "c13m3_junkyard",
            2: "c13m4_waterworks"
        }
    },
    # The Last Stand
    "#L4D360UI_CampaignName_C14": {
        "coop": {
            1: "c14m1_junkyard",
            2: "c14m2_lighthouse"
        },
        "survival": {
            1: "c14m1_junkyard_survival",
            2: "c14m2_lighthouse_survival"
        },
        "scavenge": {
            1: "c14m1_junkyard_scavenge",
            2: "c14m2_lighthouse_scavenge"
        }
    },
    "Holdout Training": {
        "holdout": {
            1: "c10m3_ranchhouse",
            2: "c10m5_houseboat"
        }
    },
    "Holdout Challenge": {
        "holdout": {
            1: "c3m1_plankcountry",
            2: "c4m1_milltown_a"
        }
    },
    "Parish Dash": {
        "dash": {
            1: "c5m2_park",
            2: "c5m3_quarter"
        }
    },
    "Carnival Shoot Zones": {
        "shootzones": {
            1: "c2m2_fairgrounds"
        }
    }
}

def get_map_thumbnail(chapter_disp_name: str,
                      chapter: int,
                      game_mode: str) -> str:
    """Get the thumbnail of current chapter.
    
    :param str chapter_disp_name: Chapter display string.
    :param int chapter: The current chapter.
    :param str game_mode: Game mode string.
    :return: URL of the map thumbnail relative to static.
    :rtype: str
    """
    generic_thumbnail = "images/addon.png"
    chapter_dict: dict = THUMBNAIL_NAMES.get(chapter_disp_name)
    if chapter_dict is None:
        return generic_thumbnail
    if game_mode.startswith("l4d1"):
        if game_mode == "l4d1vs":
            game_mode = "coop"
        else:
            game_mode = game_mode.removeprefix("l4d1")
    # Follow the Liter and Room For One mutation
    if game_mode == {"mutation10", "mutation13"}:
        game_mode = "scavenge"
    # Versus Survival and Nightmare mode
    if game_mode == {"mutation15", "community4"}:
        game_mode = "survival"
    game_mode_dict: dict = chapter_dict.get(game_mode)
    if game_mode_dict is None:
        game_mode_dict = chapter_dict.get("coop")
    thumbnail_url = f"images/thumbnails/{game_mode_dict.get(chapter)}.png"
    if thumbnail_url is None:
        return generic_thumbnail
    return thumbnail_url
