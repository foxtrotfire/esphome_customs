import esphome.codegen as cg
import esphome.config_validation as cv
from esphome.components import i2c
from esphome.const import CONF_ID

CODEOWNERS = ["@KoenBreeman"]
DEPENDENCIES = ["i2c"]

MULTI_CONF = True

CONF_M5STACK4RELAY_ID = "m5stack4relay_id"

m5stack4relay_ns = cg.esphome_ns.namespace("m5stack4relay")
m5stack4relay = m5stack4relay_ns.class_("m5stack4relay", cg.Component, i2c.I2CDevice)

CONFIG_SCHEMA = (
    cv.Schema(
        {
            cv.GenerateID(): cv.declare_id(m5stack4relay),
        }
    )
    .extend(cv.COMPONENT_SCHEMA)
    .extend(i2c.i2c_device_schema(0x26))
)


async def to_code(config):
    var = cg.new_Pvariable(config[CONF_ID])
    await cg.register_component(var, config)
    await i2c.register_i2c_device(var, config)
