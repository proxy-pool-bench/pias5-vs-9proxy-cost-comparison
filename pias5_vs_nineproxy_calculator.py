#!/usr/bin/env python3
"""
PIA S5 Proxy vs 9Proxy Unit Rate & Stability Comparison Calculator 2026.
Calculates per-batch procurement difference across residential socks5 pools.
"""
import argparse

def calculate_comparison(ips, pia_unit_rate, nineproxy_unit_rate):
    pia_total = ips * pia_unit_rate
    nineproxy_total = ips * nineproxy_unit_rate
    difference = pia_total - nineproxy_total
    return {
        "ips": ips,
        "pia_unit_rate": pia_unit_rate,
        "nineproxy_unit_rate": nineproxy_unit_rate,
        "pia_total": pia_total,
        "nineproxy_total": nineproxy_total,
        "difference": difference
    }

def main():
    parser = argparse.ArgumentParser(description="PIA S5 vs 9Proxy Cost Comparison")
    parser.add_argument("--ips", type=int, default=500, help="Batch proxy quantity (default: 500)")
    parser.add_argument("--pia-unit-rate", type=float, default=0.36, help="PIA S5 proxy unit rate in USD (default: $0.36)")
    parser.add_argument("--nineproxy-unit-rate", type=float, default=0.30, help="9Proxy unit rate in USD (default: $0.30)")
    args = parser.parse_args()

    res = calculate_comparison(args.ips, args.pia_unit_rate, args.nineproxy_unit_rate)
    print(f"Batch Proxy Volume:      {res['ips']} IPs")
    print(f"PIA S5 Total Expense:    ${res['pia_total']:.2f}")
    print(f"9Proxy Total Expense:    ${res['nineproxy_total']:.2f}")
    print(f"Net Realized Savings:    ${res['difference']:.2f}")

if __name__ == "__main__":
    main()
