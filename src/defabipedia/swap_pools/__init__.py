from ..types import Chain, ContractAbi, SwapPools, current_dir

class EthereumSwapPools:
    TriPool = SwapPools(
        address="0xbEbc44782C7dB0a1A60Cb6fe97d0b483032FF1C7",
        abi_path=current_dir() / "tri_pool.json",
        name="tri_pool",
        tokens=["DAI", "USDC", "USDT"],
        protocol="Curve"
    )
    Curve_stETH_ETH = SwapPools(
        address="0xDC24316b9AE028F1497c275EB9192a3Ea0f67022",
        abi_path=current_dir() / "stETH_ETH_pool_curve.json",
        name="stETH_ETH_pool_curve",
        tokens=["stETH", "ETH"],
        protocol="Curve"
    )
    Curve_stETH_ETH2 = SwapPools(
        address="0x21E27a5E5513D6e65C4f830167390997aA84843a",
        abi_path=current_dir() / "stETH_ETH_poo2_curve.json",
        name="stETH_ETH_pool2_curve",
        tokens=["stETH", "ETH"],
        protocol="Curve"
    )
    UniV3_USDC_USDT = SwapPools(
        address="0x3416cF6C708Da44DB2624D63ea0AAef7113527C6",
        abi_path=current_dir() / "USDC_USDT_pool.json",
        name="USDC_USDT_pool",
        tokens=["USDC", "USDT"],
        protocol="UniswapV3"
    )
    UniV3_DAI_USDC = SwapPools(
        address="0x5777d92f208679DB4b9778590Fa3CAB3aC9e2168",
        abi_path=current_dir() / "DAI_USDC_pool.json",
        name="DAI_USDC_pool",
        tokens=["DAI", "USDC"],
        protocol="UniswapV3"
    )
    UniV3_wstETH_ETH = SwapPools(
        address="0x109830a1AAaD605BbF02a9dFA7B0B92EC2FB7dAa",
        abi_path=current_dir() / "wstETH_ETH_pool.json",
        name="wstETH_ETH_pool",
        tokens=["wstETH", "ETH"],
        protocol="UniswapV3"
    )
    UniV3_DAI_USDC2 = SwapPools(
        address="0x6c6Bc977E13Df9b0de53b251522280BB72383700",
        abi_path=current_dir() / "DAI_USDC_pool_2.json",
        name="DAI_USDC_pool_2",
        tokens=["DAI", "USDC"],
        protocol="UniswapV3"
    )
    bal_rETH_WETH = SwapPools(
        address="0x1E19CF2D73a72Ef1332C882F20534B6519Be0276",
        abi_path=current_dir() / "rETH_WETH_pool.json",
        name="rETH_WETH_pool",
        tokens=["rETH", "WETH"],
        protocol="Balancer"
    )
    bal_wstETH_WETH2 = SwapPools(
        address="0x93d199263632a4EF4Bb438F1feB99e57b4b5f0BD",
        abi_path=current_dir() / "bal_wstETH_WETH_pool.json",
        name="bal_wstETH_WETH_pool",
        tokens=["wstETH", "WETH"],
        protocol="Balancer"
    )

class GnosisSwapPools:
    TriPool = SwapPools(
        address="0x7f90122BF0700F9E7e1F688fe926940E8839F353",
        abi_path=current_dir() / "tri_pool_gc.json",
        name="tri_pool_gc",
        tokens=["DAI", "USDC", "USDT"],
        protocol="Curve"
    )
    Curve_EURe_tripool = SwapPools(
        address="0x056c6c5e684cec248635ed86033378cc444459b0",
        abi_path=current_dir() / "EURe_tripool_pool_curve.json",
        name="EURe_tripool_pool_curve",
        tokens=["EURe", "WXDAI", "USDC", "USDT"],
        protocol="Curve"
    )
    bal_wstETH_WETH_pool = SwapPools(
        address="0xbAd20c15A773bf03ab973302F61FAbceA5101f0A",
        abi_path=current_dir() / "bal_wstETH_WETH_pool.json",
        name="bal_wstETH_WETH_pool",
        tokens=["wstETH", "WETH"],
        protocol="Balancer"
    )
    bal_USDT_USDC_sDAI_pool = SwapPools(
        address="0x7644fA5D0eA14FcF3E813Fdf93ca9544f8567655",
        abi_path=current_dir() / "bal_USDT_USDC_sDAI_pool.json",
        name="bal_USDT_USDC_sDAI_pool",
        tokens=["USDT", "USDC", "sDAI"],
        protocol="Balancer"
    )
    bal_stable_usd_pool = SwapPools(
        address="0x2086f52651837600180dE173B09470F54EF74910",
        abi_path=current_dir() / "bal_stable_usd_pool.json",
        name="bal_stable_usd_pool",
        tokens=["USDT", "USDC", "WXDAI"],
        protocol="Balancer"
    )


SwapPools = {Chain.ETHEREUM: EthereumSwapPools, Chain.GNOSIS: GnosisSwapPools}
