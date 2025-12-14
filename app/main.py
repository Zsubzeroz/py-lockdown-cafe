from cafe import Cafe
from errors import VaccineError, NotWearingMaskError


def go_to_cafe(friends: list, cafe: Cafe) -> str:
    masks_to_buy = 0

    for friend in friends:
        try:
            cafe.visit_cafe(friend)
        except VaccineError:
            # If any friend has a vaccine issue (missing or outdated),
            # we return this error immediately as it has priority.
            return "All friends should be vaccinated"
        except NotWearingMaskError:
            # If a friend is just missing a mask, we count it but
            # continue checking others in case someone else has a vaccine error.
            masks_to_buy += 1

    if masks_to_buy > 0:
        return f"Friends should buy {masks_to_buy} masks"

    return f"Friends can go to {cafe.name}"
