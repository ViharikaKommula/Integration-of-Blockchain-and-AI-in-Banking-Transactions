// migrations/2_deploy_contracts.js
const SimpleTransaction = artifacts.require("SimpleTransaction");

module.exports = function (deployer) {
  deployer.deploy(SimpleTransaction);
};
