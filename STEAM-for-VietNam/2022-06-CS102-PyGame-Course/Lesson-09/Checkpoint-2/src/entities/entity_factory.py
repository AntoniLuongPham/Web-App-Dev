from __future__ import annotations

from common.types import FRIENDLY_NPC_TYPES, EntityType
from config import (
    ASSET_DIR,
    DialogueBoxConfig,
    GameConfig,
    NpcConfig,
    PlayerConfig,
    PlayerInventoryConfig,
    ShadowConfig,
)
from entities.base_entity import BaseEntity
from entities.dialogue_box import DialogueBox
from entities.friendly_npc import FriendlyNpc
from entities.player import Player
from entities.player_inventory import PlayerInventory
from entities.shadow import Shadow


class EntityFactory:
    """
    Since creating entities required specific config values for different entity types,
    we gather entity creation here.
    Whenever World needs a new entity, it can call this helper, for example:

    EntityFactory.create(EntityType.Player)

    EntityFactory.create(EntityType.Shadow, x=10, y=20)
    """

    @classmethod
    def create(cls, entity_type: EntityType, x: int = 0, y: int = 0):
        if entity_type == EntityType.PLAYER:
            return Player(
                entity_type=entity_type,
                gravity=PlayerConfig.GRAVITY,
                speed=PlayerConfig.SPEED,
                jump_vertical_speed=PlayerConfig.JUMP_VERTICAL_SPEED,
                jump_with_trampoline_speed=PlayerConfig.JUMP_WITH_TRAMPOLINE_SPEED,
                x=x,
                y=y,
                sprite_path=PlayerConfig.SPRITE_PATH,
                scale=PlayerConfig.SCALE,
                animation_interval_ms=PlayerConfig.ANIMATION_INTERVAL_MS,
            )
        elif entity_type == EntityType.PLAYER_INVENTORY:
            return PlayerInventory(
                entity_type=entity_type,
                x=PlayerInventoryConfig.X,
                y=PlayerInventoryConfig.Y,
                sprite_path=PlayerInventoryConfig.SPRITE_PATH,
                scale=PlayerInventoryConfig.SCALE,
            )
        elif entity_type == EntityType.SHADOW:
            return Shadow(
                entity_type=entity_type,
                x=x,
                y=y,
                sprite_path=ShadowConfig.SPRITE_PATH,
                scale=ShadowConfig.SCALE,
                animation_interval_ms=ShadowConfig.ANIMATION_INTERVAL_MS,
                speed=ShadowConfig.SPEED,
                damage=ShadowConfig.DAMAGE,
            )
        elif entity_type in FRIENDLY_NPC_TYPES:
            config: NpcConfig = NpcConfig(entity_type=entity_type)
            return FriendlyNpc(
                entity_type=entity_type,
                npc_config=config,
                x=x,
                y=y,
                sprite_path=config.sprite_path,
                scale=config.scale,
                animation_interval_ms=config.animation_interval_ms,
            )
        elif entity_type == EntityType.DIALOGUE_BOX:
            return DialogueBox(
                entity_type=entity_type,
                x=DialogueBoxConfig.X,
                y=DialogueBoxConfig.Y,
                sprite_path=DialogueBoxConfig.SPRITE_PATH,
                scale=DialogueBoxConfig.SCALE,
            )
        else:
            return BaseEntity(
                entity_type=entity_type,
                x=x,
                y=y,
                sprite_path=ASSET_DIR / "items" / f"{entity_type.name.lower()}.png",
                scale=(GameConfig.TILE_SIZE, GameConfig.TILE_SIZE),
            )
