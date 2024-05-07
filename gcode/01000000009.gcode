; generated by Slic3r 1.3.0 on 2024-05-07 at 19:33:07

; external perimeters extrusion width = 0.55mm (4.37mm^3/s)
; perimeters extrusion width = 0.70mm (11.44mm^3/s)
; infill extrusion width = 0.62mm (13.45mm^3/s)
; solid infill extrusion width = 0.70mm (3.81mm^3/s)
; top infill extrusion width = 0.70mm (2.86mm^3/s)

M107
M104 S200 ; set temperature
G28 ; home all axes
G1 Z5 F5000 ; lift nozzle

; Filament gcode

M109 S200 ; set temperature and wait for it to be reached
G21 ; set units to millimeters
G90 ; use absolute coordinates
M82 ; use absolute distances for extrusion
G92 E0
G1 Z0.350 F7800.000
G1 E-2.00000 F2400.00000
G92 E0
G1 X94.464 Y95.433 F7800.000
G1 E2.00000 F2400.00000
G1 F600
G1 X96.231 Y93.971 E2.07096
G1 X99.289 Y93.109 E2.16927
G1 X99.681 Y93.107 E2.18138
G1 X101.890 Y93.540 E2.25105
G1 X102.877 Y94.006 E2.28483
G1 X103.331 Y94.288 E2.30135
G1 X103.827 Y94.651 E2.32036
G1 X104.363 Y95.118 E2.34235
G1 X105.545 Y96.511 E2.39890
G1 X106.515 Y99.132 E2.48536
G1 X106.580 Y99.894 E2.50902
G1 X106.352 Y101.839 E2.56962
G1 X106.165 Y102.426 E2.58869
G1 X105.384 Y103.925 E2.64097
G1 X103.893 Y105.463 E2.70726
G1 X103.472 Y105.776 E2.72348
G1 X101.885 Y106.646 E2.77948
G1 X100.894 Y106.939 E2.81145
G1 X100.325 Y107.036 E2.82931
G1 X98.390 Y106.996 E2.88921
G1 X98.079 Y106.936 E2.89901
G1 X97.534 Y106.794 E2.91643
G1 X96.215 Y106.227 E2.96086
G1 X94.934 Y105.293 E3.00992
G1 X94.483 Y104.830 E3.02990
G1 X93.798 Y103.912 E3.06535
G1 X93.453 Y103.284 E3.08751
G1 X93.251 Y102.820 E3.10317
G1 X92.956 Y101.868 E3.13403
G1 X92.876 Y101.470 E3.14659
G1 X92.796 Y100.777 E3.16815
G1 X92.784 Y100.227 E3.18517
G1 X92.857 Y99.336 E3.21283
G1 X93.038 Y98.298 E3.24544
G1 X93.301 Y97.410 E3.27410
G1 X94.426 Y95.498 E3.34276
G1 E1.34276 F2400.00000
G92 E0
G1 X99.655 Y99.832 F7800.000
G1 E2.00000 F2400.00000
G1 F1800
G1 X99.617 Y100.013 E2.00110
G1 X99.666 Y100.110 E2.00175
G1 X99.918 Y100.169 E2.00329
G1 Z0.650 F7800.000
G1 E0.00329 F2400.00000
G92 E0
; Filament-specific end gcode 
;END gcode for filament

M104 S0 ; turn off temperature
G28 X0  ; home X axis
M84     ; disable motors

M140 S0 ; set bed temperature
; filament used = 1.3mm (0.0cm3)
; total filament cost = 0.0

; avoid_crossing_perimeters = 0
; bed_shape = 0x0,200x0,200x200,0x200
; bed_temperature = 0
; before_layer_gcode = 
; between_objects_gcode = 
; bridge_acceleration = 0
; bridge_fan_speed = 100
; brim_connections_width = 0
; brim_width = 0
; complete_objects = 0
; cooling = 1
; default_acceleration = 0
; disable_fan_first_layers = 3
; duplicate_distance = 6
; end_filament_gcode = "; Filament-specific end gcode \n;END gcode for filament\n"
; end_gcode = M104 S0 ; turn off temperature\nG28 X0  ; home X axis\nM84     ; disable motors\n
; extruder_clearance_height = 20
; extruder_clearance_radius = 20
; extruder_offset = 0x0
; extrusion_axis = E
; extrusion_multiplier = 1
; fan_always_on = 0
; fan_below_layer_time = 60
; filament_colour = #FFFFFF
; filament_cost = 0
; filament_density = 0
; filament_diameter = 3
; filament_max_volumetric_speed = 0
; filament_notes = ""
; first_layer_acceleration = 0
; first_layer_bed_temperature = 0
; first_layer_extrusion_width = 200%
; first_layer_speed = 30
; first_layer_temperature = 200
; gcode_arcs = 0
; gcode_comments = 0
; gcode_flavor = reprap
; has_heatbed = 1
; infill_acceleration = 0
; infill_first = 0
; interior_brim_width = 0
; layer_gcode = 
; max_fan_speed = 100
; max_layer_height = 0.3
; max_print_speed = 80
; max_volumetric_speed = 0
; min_fan_speed = 35
; min_layer_height = 0.15
; min_print_speed = 10
; min_skirt_length = 0
; notes = 
; nozzle_diameter = 0.5
; only_retract_when_crossing_perimeters = 1
; ooze_prevention = 0
; output_filename_format = [input_filename_base].gcode
; perimeter_acceleration = 0
; post_process = 
; pressure_advance = 0
; printer_notes = 
; resolution = 0
; retract_before_travel = 2
; retract_layer_change = 0
; retract_length = 2
; retract_length_toolchange = 10
; retract_lift = 0
; retract_lift_above = 0
; retract_lift_below = 0
; retract_restart_extra = 0
; retract_restart_extra_toolchange = 0
; retract_speed = 40
; skirt_distance = 6
; skirt_height = 1
; skirts = 1
; slowdown_below_layer_time = 5
; spiral_vase = 0
; standby_temperature_delta = -5
; start_filament_gcode = "; Filament gcode\n"
; start_gcode = G28 ; home all axes\nG1 Z5 F5000 ; lift nozzle\n
; temperature = 200
; threads = 4
; toolchange_gcode = 
; travel_speed = 130
; use_firmware_retraction = 0
; use_relative_e_distances = 0
; use_set_and_wait_bed = 0
; use_set_and_wait_extruder = 0
; use_volumetric_e = 0
; vibration_limit = 0
; wipe = 0
; z_offset = 0
; z_steps_per_mm = 0
; adaptive_slicing = 0
; adaptive_slicing_quality = 75%
; dont_support_bridges = 1
; extrusion_width = 0
; first_layer_height = 0.35
; infill_only_where_needed = 0
; interface_shells = 0
; layer_height = 0.3
; match_horizontal_surfaces = 0
; raft_layers = 0
; regions_overlap = 0
; seam_position = aligned
; sequential_print_priority = 0
; support_material = 0
; support_material_angle = 0
; support_material_buildplate_only = 0
; support_material_contact_distance = 0.2
; support_material_enforce_layers = 0
; support_material_extruder = 1
; support_material_extrusion_width = 0
; support_material_interface_extruder = 1
; support_material_interface_extrusion_width = 0
; support_material_interface_layers = 3
; support_material_interface_spacing = 0
; support_material_interface_speed = 100%
; support_material_max_layers = 0
; support_material_pattern = pillars
; support_material_spacing = 2.5
; support_material_speed = 60
; support_material_threshold = 60%
; xy_size_compensation = 0
; bottom_infill_pattern = rectilinear
; bottom_solid_layers = 3
; bridge_flow_ratio = 1
; bridge_speed = 60
; external_perimeter_extrusion_width = 0
; external_perimeter_speed = 50%
; external_perimeters_first = 0
; extra_perimeters = 1
; fill_angle = 45
; fill_density = 20%
; fill_gaps = 1
; fill_pattern = stars
; gap_fill_speed = 20
; infill_every_layers = 1
; infill_extruder = 1
; infill_extrusion_width = 0
; infill_overlap = 55%
; infill_speed = 80
; overhangs = 1
; perimeter_extruder = 1
; perimeter_extrusion_width = 0
; perimeter_speed = 60
; perimeters = 3
; small_perimeter_speed = 15
; solid_infill_below_area = 70
; solid_infill_every_layers = 0
; solid_infill_extruder = 1
; solid_infill_extrusion_width = 0
; solid_infill_speed = 20
; thin_walls = 1
; top_infill_extrusion_width = 0
; top_infill_pattern = rectilinear
; top_solid_infill_speed = 15
; top_solid_layers = 3
