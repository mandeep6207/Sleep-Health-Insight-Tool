from __future__ import annotations

import json
from dataclasses import dataclass

import pandas as pd


@dataclass(frozen=True)
class FactorResult:
    name: str
    value: float
    score: float


def _clamp(value: float, minimum: float = 0.0, maximum: float = 1.0) -> float:
    return max(minimum, min(maximum, value))


def _sleep_duration_score(duration_hours: float) -> float:
    if 7.0 <= duration_hours <= 8.0:
        return 40.0

    ideal_midpoint = 7.5
    max_distance = 4.0
    closeness = 1 - abs(duration_hours - ideal_midpoint) / max_distance
    return round(_clamp(closeness) * 40, 2)


def _screen_time_score(screen_time_hours: float) -> float:
    inverse_score = 1 - (screen_time_hours / 5.0)
    return round(_clamp(inverse_score) * 20, 2)


def _caffeine_score(cups_per_day: float) -> float:
    inverse_score = 1 - (cups_per_day / 6.0)
    return round(_clamp(inverse_score) * 20, 2)


def _stress_score(stress_level: float) -> float:
    inverse_score = 1 - ((stress_level - 1) / 9.0)
    return round(_clamp(inverse_score) * 20, 2)


def _category(score: float) -> str:
    if score <= 40:
        return "Poor Sleep"
    if score <= 70:
        return "Average Sleep"
    return "Good Sleep"


def _insights(values: dict[str, float]) -> list[str]:
    insights = []
    if values["screen_time"] >= 3:
        insights.append("High screen time reduces sleep quality.")
    if values["caffeine_intake"] >= 2:
        insights.append("High caffeine intake impacts sleep.")
    if values["stress_level"] >= 7:
        insights.append("High stress lowers sleep quality.")
    if values["sleep_duration"] < 6.5:
        insights.append("Short sleep duration is hurting recovery.")
    if values["sleep_duration"] > 8.5:
        insights.append("Very long sleep duration may indicate irregular sleep habits.")
    return insights or ["Your current pattern looks balanced across the tracked factors."]


def _suggestions(values: dict[str, float]) -> list[str]:
    suggestions = [
        "Reduce screen time before bed.",
        "Limit caffeine intake.",
        "Maintain a consistent sleep schedule.",
    ]
    if values["stress_level"] >= 7:
        suggestions.append("Add a short wind-down routine to lower stress before sleep.")
    if values["sleep_duration"] < 7:
        suggestions.append("Aim for 7 to 8 hours of sleep each night.")
    return suggestions


def analyze_sleep(form_values: dict[str, float]) -> dict:
    frame = pd.DataFrame([form_values])
    record = frame.iloc[0].to_dict()

    factor_results = [
        FactorResult("Sleep duration", record["sleep_duration"], _sleep_duration_score(record["sleep_duration"])),
        FactorResult("Screen time", record["screen_time"], _screen_time_score(record["screen_time"])),
        FactorResult("Caffeine intake", record["caffeine_intake"], _caffeine_score(record["caffeine_intake"])),
        FactorResult("Stress level", record["stress_level"], _stress_score(record["stress_level"])),
    ]

    raw_score = sum(item.score for item in factor_results)
    total_score = round(_clamp(raw_score / 100.0) * 100, 2)
    category = _category(total_score)
    insight_list = _insights(record)
    suggestion_list = _suggestions(record)

    factor_df = pd.DataFrame(
        {
            "factor": [item.name for item in factor_results],
            "value": [item.value for item in factor_results],
            "score": [item.score for item in factor_results],
        }
    )

    chart_labels = factor_df["factor"].tolist()
    chart_scores = factor_df["score"].round(2).tolist()

    category_distribution = {
        "Score achieved": total_score,
        "Room to improve": round(100 - total_score, 2),
    }

    return {
        "score": total_score,
        "category": category,
        "insights": insight_list,
        "suggestions": suggestion_list,
        "factors": factor_results,
        "bar_chart": {
            "labels": chart_labels,
            "values": chart_scores,
        },
        "pie_chart": {
            "labels": list(category_distribution.keys()),
            "values": list(category_distribution.values()),
        },
        "progress": total_score,
        "score_badge": "success" if total_score > 70 else "warning" if total_score > 40 else "danger",
        "insight_json": json.dumps(insight_list),
        "suggestion_json": json.dumps(suggestion_list),
    }
