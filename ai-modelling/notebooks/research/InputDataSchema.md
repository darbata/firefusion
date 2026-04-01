# FireFusion Input Data — Schema Reference

## Sample Record

```json
{
  "type": "FeatureCollection",
  "name": "FireFusion_Training_Data_Sample",
  "crs": {
    "type": "name",
    "properties": {
      "name": "urn:ogc:def:crs:EPSG::4326"
    }
  },
  "features": [
    {
      "type": "Feature",
      "geometry": { "type": "Point", "coordinates": [145.47, -37.53] },
      "properties": {
        "cell_id": "VIC_GRID_0892",
        "suburb": "Toolangi",
        "static_terrain": {
          "elevation_m": 540,
          "slope_deg": 12,
          "aspect_deg": 315,
          "dist_to_water_m": 1200
        },
        "biological_fuel": {
          "veg_type": "Wet Sclerophyll",
          "ndvi_at_ignition": 0.31,
          "ndwi_at_ignition": null,
          "nbr_at_ignition": null
        },
        "ignition_risk": {
          "dist_to_powerlines_m": 420
        },
        "historical_fire_data": [
          {
            "fire_start_date": "2003-01-21",
            "fire_end_date": null,
            "severity": null,
            "ndvi_at_ignition": null,
            "area_ha_burned": null
          }
        ],
        "weather_sequence_7d": [
          { "day": -6, "max_temp_c": 33.1, "wind_speed_kmh": 28, "wind_dir_deg": 285, "rel_humidity_pct": 28, "precipitation_mm": 0.0, "evapotranspiration": 5.4, "soil_moisture": 0.15, "soil_temp_c": 28.0, "days_since_rain": 7 },
          "...",
          { "day": 0, "max_temp_c": 39.8, "wind_speed_kmh": 52, "wind_dir_deg": 315, "rel_humidity_pct": 9, "precipitation_mm": 0.0, "evapotranspiration": 7.8, "soil_moisture": 0.08, "soil_temp_c": 38.4, "days_since_rain": 13 }
        ],
        "target_labels": {
          "severity_class": 5,
          "area_ha_burned": 4375.0,
          "rate_of_spread_ha_per_day": 546.9
        }
      }
    }
  ]
}
```

---

## Variable Reference

| Variable | Block | Type | Unit | Description |
|---|---|---|---|---|
| `cell_id` | root | string | — | Unique identifier for the spatial grid cell |
| `suburb` | root | string | — | Nearest named locality to the cell centroid |
| `elevation_m` | static_terrain | float | metres | Height above sea level |
| `slope_deg` | static_terrain | float | degrees | Terrain slope angle; steeper slopes accelerate fire spread uphill |
| `aspect_deg` | static_terrain | float | degrees | Direction the slope faces (0=N, 90=E, 180=S, 270=W); north-facing slopes retain more moisture in the southern hemisphere |
| `dist_to_water_m` | static_terrain | float | metres | Distance to nearest river, stream, or water body; proximity to water moderates local humidity |
| `veg_type` | biological_fuel | string | — | Broad vegetation classification (e.g. Wet Sclerophyll, Dry Sclerophyll, Grassland) |
| `ndvi_at_ignition` | biological_fuel | float | unitless (−1 to 1) | Greenness and density of vegetation at ignition time; lower values indicate stressed, more flammable fuel |
| `ndwi_at_ignition` | biological_fuel | float | unitless (−1 to 1) | Canopy water content at ignition time; lower values indicate drier, more ignitable fuel |
| `nbr_at_ignition` | biological_fuel | float | unitless (−1 to 1) | Pre-fire burn ratio; captures fuel moisture and canopy health using shortwave infrared |
| `dist_to_powerlines_m` | ignition_risk | float | metres | Distance to nearest powerline infrastructure; a proxy for ignition likelihood from electrical faults |
| `fire_start_date` | historical_fire_data | date | ISO 8601 | Date the historical fire ignited in this cell |
| `fire_end_date` | historical_fire_data | date | ISO 8601 | Date the historical fire was extinguished or left the cell |
| `severity` | historical_fire_data | int | 1–5 | Severity class of the historical fire event |
| `ndvi_at_ignition` | historical_fire_data | float | unitless (−1 to 1) | NDVI recorded at the time of that past fire event, used as a historical feature |
| `area_ha_burned` | historical_fire_data | float | hectares | Total area burned in that historical fire event |
| `day` | weather_sequence_7d | int | — | Day offset relative to ignition (day 0 = ignition day, day −6 = six days prior) |
| `max_temp_c` | weather_sequence_7d | float | °C | Maximum air temperature for the day |
| `wind_speed_kmh` | weather_sequence_7d | float | km/h | Maximum or mean wind speed for the day |
| `wind_dir_deg` | weather_sequence_7d | float | degrees | Prevailing wind direction (meteorological convention, direction wind comes from) |
| `rel_humidity_pct` | weather_sequence_7d | float | % | Relative humidity; low values dramatically increase fire spread potential |
| `precipitation_mm` | weather_sequence_7d | float | mm | Total rainfall for the day |
| `evapotranspiration` | weather_sequence_7d | float | mm | Water lost from soil and vegetation to atmosphere; a proxy for atmospheric dryness and fuel stress |
| `soil_moisture` | weather_sequence_7d | float | m³/m³ | Volumetric water content of the soil; low values indicate dry fine fuel on the ground |
| `soil_temp_c` | weather_sequence_7d | float | °C | Soil surface temperature; elevated values accelerate surface fuel drying |
| `days_since_rain` | weather_sequence_7d | int | days | Consecutive days without meaningful rainfall; strong predictor of fine fuel dryness |
| `severity_class` | target_labels | int | 1–5 | Categorical fire severity outcome for the event (1=low, 5=catastrophic) |
| `area_ha_burned` | target_labels | float | hectares | Total area burned by the fire event originating from or passing through this cell |
| `rate_of_spread_ha_per_day` | target_labels | float | ha/day | Average rate at which the fire expanded; captures fire behaviour intensity |