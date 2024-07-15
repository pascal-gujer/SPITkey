"""Map address ranges to TPM registry names"""
from rangedict import RangeDict
fifo = RangeDict()
fifo[(0x0000, 0x0000)] = "TPM_ACCESS_0"
fifo[(0x0001, 0x0007)] = "Reserved"
fifo[(0x0008, 0x000b)] = "TPM_INT_ENABLE_0"
fifo[(0x000c, 0x000c)] = "TPM_INT_VECTOR_0"
fifo[(0x000d, 0x000f)] = "Reserved"
fifo[(0x0010, 0x0013)] = "TPM_INT_STATUS_0"
fifo[(0x0014, 0x0017)] = "TPM_INTF_CAPABILITY_0"
fifo[(0x0018, 0x001b)] = "TPM_STS_0"
fifo[(0x001c, 0x0023)] = "Reserved"
fifo[(0x0024, 0x0027)] = "TPM_DATA_FIFO_0"
fifo[(0x0028, 0x002f)] = "Reserved"
fifo[(0x0030, 0x0033)] = "TPM_INTERFACE_ID_0"
fifo[(0x0034, 0x007f)] = "Reserved"
fifo[(0x0080, 0x0083)] = "TPM_XDATA_FIFO_0"
fifo[(0x0084, 0x0881)] = "Reserved"
fifo[(0x0f00, 0x0f03)] = "TPM_DID_VID_0"
fifo[(0x0f04, 0x0f04)] = "TPM_RID_0"
fifo[(0x0f90, 0x0fff)] = "Reserved"
fifo[(0x1000, 0x1000)] = "TPM_ACCESS_1"
fifo[(0x1001, 0x1007)] = "Reserved"
fifo[(0x1008, 0x100b)] = "TPM_INT_ENABLE_1"
fifo[(0x100c, 0x100c)] = "TPM_INT_VECTOR_1"
fifo[(0x100d, 0x100f)] = "Reserved"
fifo[(0x1010, 0x1013)] = "TPM_INT_STATUS_1"
fifo[(0x1014, 0x1017)] = "TPM_INTF_CAPABILITY_1"
fifo[(0x1018, 0x101b)] = "TPM_STS_1"
fifo[(0x101c, 0x1023)] = "Reserved"
fifo[(0x1024, 0x1027)] = "TPM_DATA_FIFO_1"
fifo[(0x1028, 0x102f)] = "Reserved"
fifo[(0x1030, 0x1030)] = "TPM_INTERFACE_ID_1"
fifo[(0x1037, 0x107f)] = "Reserved"
fifo[(0x1080, 0x1083)] = "TPM_XDATA_FIFO_1"
fifo[(0x1084, 0x1eff)] = "Reserved"
fifo[(0x1f00, 0x1f03)] = "TPM_DID_VID_1"
fifo[(0x1f04, 0x1f04)] = "TPM_RID_1"
fifo[(0x1f05, 0x1fff)] = "Reserved"
fifo[(0x2000, 0x2000)] = "TPM_ACCESS_2"
fifo[(0x2001, 0x2007)] = "Reserved"
fifo[(0x2008, 0x200b)] = "TPM_INT_ENABLE_2"
fifo[(0x200c, 0x200c)] = "TPM_INT_VECTOR_2"
fifo[(0x200d, 0x200f)] = "Reserved"
fifo[(0x2010, 0x2013)] = "TPM_INT_STATUS_2"
fifo[(0x2014, 0x2017)] = "TPM_INTF_CAPABILITY_2"
fifo[(0x2018, 0x201b)] = "TPM_STS_2"
fifo[(0x201c, 0x2023)] = "Reserved"
fifo[(0x2024, 0x2027)] = "TPM_DATA_FIFO_2"
fifo[(0x2028, 0x202f)] = "Reserved"
fifo[(0x2030, 0x2033)] = "TPM_INTERFACE_ID_2"
fifo[(0x2034, 0x207f)] = "Reserved"
fifo[(0x2080, 0x2083)] = "TPM_XDATA_FIFO_2"
fifo[(0x2084, 0x2eff)] = "Reserved"
fifo[(0x2f00, 0x2f03)] = "TPM_DID_VID_2"
fifo[(0x2f04, 0x2f04)] = "TPM_RID_2"
fifo[(0x2f05, 0x2fff)] = "Reserved"
fifo[(0x3000, 0x3000)] = "TPM_ACCESS_3"
fifo[(0x3001, 0x3007)] = "Reserved"
fifo[(0x3008, 0x300b)] = "TPM_INT_ENABLE_3"
fifo[(0x300c, 0x300c)] = "TPM_INT_VECTOR_3"
fifo[(0x300d, 0x300f)] = "Reserved"
fifo[(0x3010, 0x3013)] = "TPM_INT_STATUS_3"
fifo[(0x3014, 0x3017)] = "TPM_INTF_CAPABILITY_3"
fifo[(0x3018, 0x301b)] = "TPM_STS_3"
fifo[(0x301c, 0x3023)] = "Reserved"
fifo[(0x3024, 0x3027)] = "TPM_DATA_FIFO_3"
fifo[(0x3028, 0x302f)] = "Reserved"
fifo[(0x3030, 0x3033)] = "TPM_INTERFACE_ID_3"
fifo[(0x3034, 0x307f)] = "Reserved"
fifo[(0x3080, 0x3083)] = "TPM_XDATA_FIFO_3"
fifo[(0x3084, 0x3eff)] = "Reserved"
fifo[(0x3f00, 0x3f03)] = "TPM_DID_VID_3"
fifo[(0x3f04, 0x3f04)] = "TPM_RID_3"
fifo[(0x3f05, 0x3fff)] = "Reserved"
fifo[(0x4000, 0x4000)] = "TPM_ACCESS_4"
fifo[(0x4001, 0x4007)] = "Reserved"
fifo[(0x4008, 0x400b)] = "TPM_INT_ENABLE_4"
fifo[(0x400c, 0x400c)] = "TPM_INT_VECTOR_4"
fifo[(0x400d, 0x400f)] = "Reserved"
fifo[(0x4010, 0x4013)] = "TPM_INT_STATUS_4"
fifo[(0x4014, 0x4017)] = "TPM_INTF_CAPABILITY_4"
fifo[(0x4018, 0x401b)] = "TPM_STS_4"
fifo[(0x401c, 0x401f)] = "Reserved"
fifo[(0x4020, 0x4023)] = "TPM_HASH_END"
fifo[(0x4024, 0x4027)] = "TPM_DATA_FIFO_4"
fifo[(0x4028, 0x402f)] = "TPM_HASH_START"
fifo[(0x4030, 0x4033)] = "TPM_INTERFACE_ID_4"
fifo[(0x4034, 0x407f)] = "Reserved"
fifo[(0x4080, 0x4083)] = "TPM_XDATA_FIFO_4"
fifo[(0x4084, 0x4eff)] = "Reserved"
fifo[(0x4f00, 0x4f03)] = "TPM_DID_VID_4"
fifo[(0x4f04, 0x4f04)] = "TPM_RID_4"
fifo[(0x4f05, 0x4fff)] = "Reserved"
fifo[(0x5000, 0x5fff)] = "Reserved"