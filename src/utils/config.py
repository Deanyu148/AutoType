import json

import yaml
from copy import deepcopy
from pathlib import Path
from uuid import uuid4
from datetime import datetime, timezone


class Config:
    DEFAULTS = {
        "language": "zh",
        "window": {
            "x": 150,
            "y": 100,
            "width": 980,
            "height": 720,
            "always_on_top": False,
            "maximized": False,
        },
        "typing": {
            "speed_cps": 50,
            "start_delay_seconds": 3,
            "mode": "realistic",
            "variance_percent": 15,
            "loop_enabled": False,
            "loop_interval_seconds": 2,
        },
        "hotkeys": {
            "start": "f6",
            "stop": "f7",
            "toggle": "f8",
        },
        "presets": [],
    }

    def __init__(self):
        self._data = deepcopy(self.DEFAULTS)
        self._file_path = self._get_config_path()

    # ── Persistence ────────────────────────────────────────────

    def load(self):
        if not self._file_path.exists():
            self.save()
            return

        try:
            with open(self._file_path, "r", encoding="utf-8") as f:
                loaded = json.load(f)
            self._data = self._deep_merge(deepcopy(self.DEFAULTS), loaded)
        except (json.JSONDecodeError, OSError):
            self.save()

    def save(self):
        self._file_path.parent.mkdir(parents=True, exist_ok=True)
        temp = self._file_path.with_suffix(".tmp")
        with open(temp, "w", encoding="utf-8") as f:
            json.dump(self._data, f, indent=2, ensure_ascii=False)
        temp.replace(self._file_path)

    @staticmethod
    def _get_config_path() -> Path:
        import sys

        if sys.platform == "win32":
            base = Path.home() / "AppData" / "Roaming"
        elif sys.platform == "darwin":
            base = Path.home() / "Library" / "Application Support"
        else:
            base = Path.home() / ".config"
        return base / "AutoType" / "config.json"

    @staticmethod
    def _deep_merge(base, override):
        for key, value in override.items():
            if key in base and isinstance(base[key], dict) and isinstance(value, dict):
                Config._deep_merge(base[key], value)
            else:
                base[key] = value
        return base

    # ── Window ─────────────────────────────────────────────────

    @property
    def window_x(self) -> int:
        return self._data["window"]["x"]

    @window_x.setter
    def window_x(self, value: int):
        self._data["window"]["x"] = value

    @property
    def window_y(self) -> int:
        return self._data["window"]["y"]

    @window_y.setter
    def window_y(self, value: int):
        self._data["window"]["y"] = value

    @property
    def window_width(self) -> int:
        return self._data["window"]["width"]

    @window_width.setter
    def window_width(self, value: int):
        self._data["window"]["width"] = value

    @property
    def window_height(self) -> int:
        return self._data["window"]["height"]

    @window_height.setter
    def window_height(self, value: int):
        self._data["window"]["height"] = value

    @property
    def always_on_top(self) -> bool:
        return self._data["window"]["always_on_top"]

    @always_on_top.setter
    def always_on_top(self, value: bool):
        self._data["window"]["always_on_top"] = value

    @property
    def window_maximized(self) -> bool:
        return self._data["window"]["maximized"]

    @window_maximized.setter
    def window_maximized(self, value: bool):
        self._data["window"]["maximized"] = value

    # ── Typing ─────────────────────────────────────────────────

    @property
    def speed_cps(self) -> int:
        return self._data["typing"]["speed_cps"]

    @speed_cps.setter
    def speed_cps(self, value: int):
        self._data["typing"]["speed_cps"] = value

    @property
    def start_delay(self) -> int:
        return self._data["typing"]["start_delay_seconds"]

    @start_delay.setter
    def start_delay(self, value: int):
        self._data["typing"]["start_delay_seconds"] = value

    @property
    def typing_mode(self) -> str:
        return self._data["typing"]["mode"]

    @typing_mode.setter
    def typing_mode(self, value: str):
        self._data["typing"]["mode"] = value

    @property
    def variance_percent(self) -> int:
        return self._data["typing"]["variance_percent"]

    @variance_percent.setter
    def variance_percent(self, value: int):
        self._data["typing"]["variance_percent"] = value

    @property
    def loop_enabled(self) -> bool:
        return self._data["typing"]["loop_enabled"]

    @loop_enabled.setter
    def loop_enabled(self, value: bool):
        self._data["typing"]["loop_enabled"] = value

    @property
    def loop_interval(self) -> int:
        return self._data["typing"]["loop_interval_seconds"]

    @loop_interval.setter
    def loop_interval(self, value: int):
        self._data["typing"]["loop_interval_seconds"] = value

    # ── Presets ────────────────────────────────────────────────

    def add_preset(self, name: str, text: str, params: dict | None = None) -> str:
        now = datetime.now(timezone.utc).isoformat()
        preset = {
            "id": uuid4().hex[:12],
            "name": name,
            "text": text,
            "params": params or {},
            "created": now,
            "modified": now,
        }
        self._data["presets"].append(preset)
        self.save()
        return preset["id"]

    def remove_preset(self, preset_id: str) -> bool:
        for i, p in enumerate(self._data["presets"]):
            if p["id"] == preset_id:
                del self._data["presets"][i]
                self.save()
                return True
        return False

    def rename_preset(self, preset_id: str, new_name: str) -> bool:
        for p in self._data["presets"]:
            if p["id"] == preset_id:
                p["name"] = new_name
                p["modified"] = datetime.now(timezone.utc).isoformat()
                self.save()
                return True
        return False

    def get_preset(self, preset_id: str) -> dict | None:
        for p in self._data["presets"]:
            if p["id"] == preset_id:
                return dict(p)
        return None

    def update_preset_text(self, preset_id: str, text: str) -> bool:
        for p in self._data["presets"]:
            if p["id"] == preset_id:
                p["text"] = text
                p["modified"] = datetime.now(timezone.utc).isoformat()
                self.save()
                return True
        return False

    def list_presets(self) -> list[dict]:
        return [dict(p) for p in self._data["presets"]]

    def export_presets_to_file(self, file_path: str, preset_ids: list[str] | None = None) -> int:
        """Export presets to a YAML file. Returns count of exported presets.
        If preset_ids is None, exports all presets."""
        presets = self.list_presets()
        if preset_ids is not None:
            id_set = set(preset_ids)
            presets = [p for p in presets if p["id"] in id_set]
        data = {"version": 1, "presets": presets}
        with open(file_path, "w", encoding="utf-8") as f:
            yaml.dump(data, f, allow_unicode=True, default_flow_style=False, sort_keys=False)
        return len(presets)

    @staticmethod
    def read_presets_from_file(file_path: str) -> list[dict]:
        """Read presets from a YAML file. Returns list of preset dicts (without id)."""
        with open(file_path, "r", encoding="utf-8") as f:
            data = yaml.safe_load(f)
        if not isinstance(data, dict) or "presets" not in data:
            raise ValueError("Invalid preset file format")
        presets = data["presets"]
        if not isinstance(presets, list):
            raise ValueError("Invalid preset file format")
        result = []
        for p in presets:
            if not isinstance(p, dict) or "name" not in p or "text" not in p:
                continue
            result.append({
                "name": p["name"],
                "text": p["text"],
                "params": p.get("params", {}),
            })
        return result
