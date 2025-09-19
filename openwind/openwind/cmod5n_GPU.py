
import warnings
import cupy

# Ignore overflow errors for wind calculations over land
warnings.simplefilter("ignore", RuntimeWarning)

def cmod5n_forward_gpu(v, phi, theta):
    from cupy import cos, exp, tanh
    DTOR = 57.29577951
    THETM = 40.0
    THETHR = 25.0
    ZPOW = 1.6
    C = [0, -0.6878, -0.7957, 0.3380, -0.1728, 0.0000, 0.0040, 0.1103, 0.0159,
         6.7329, 2.7713, -2.2885, 0.4971, -0.7250, 0.0450,
         0.0066, 0.3222, 0.0120, 22.7000, 2.0813, 3.0000, 8.3659,
         -3.3428, 1.3236, 6.2437, 2.3893, 0.3249, 4.1590, 1.6930]
    Y0 = C[19]
    PN = C[20]
    A = C[19] - (C[19] - 1) / C[20]
    B = 1.0 / (C[20] * (C[19] - 1.0) ** (3 - 1))
    FI = phi / DTOR
    CSFI = cos(FI)
    CS2FI = 2.00 * CSFI * CSFI - 1.00
    X = (theta - THETM) / THETHR
    XX = X * X
    A0 = C[1] + C[2] * X + C[3] * XX + C[4] * X * XX
    A1 = C[5] + C[6] * X
    A2 = C[7] + C[8] * X
    GAM = C[9] + C[10] * X + C[11] * XX
    S0 = C[12] + C[13] * X
    V = v
    S = A2 * V
    S_vec = S.copy()
    SlS0 = (S_vec < S0)
    S_vec[SlS0] = S0[SlS0]
    A3 = 1.0 / (1.0 + exp(-S_vec))
    SlS0 = (S < S0)
    A3[SlS0] = A3[SlS0] * (S[SlS0] / S0[SlS0]) ** (S0[SlS0] * (1.0 - A3[SlS0]))
    B0 = (A3 ** GAM) * 10.0 ** (A0 + A1 * V)
    B1 = C[15] * V * (0.5 + X - tanh(4.0 * (X + C[16] + C[17] * V)))
    B1 = C[14] * (1.0 + X) - B1
    B1 = B1 / (exp(0.34 * (V - C[18])) + 1.0)
    V0 = C[21] + C[22] * X + C[23] * XX
    D1 = C[24] + C[25] * X + C[26] * XX
    D2 = C[27] + C[28] * X
    V2 = (V / V0 + 1.0)
    V2ltY0 = V2 < Y0
    V2[V2ltY0] = A + B * (V2[V2ltY0] - 1.0) ** PN
    B2 = (-D1 + D2 * V2) * exp(-V2)
    CMOD5_N = B0 * (1.0 + B1 * CSFI + B2 * CS2FI) ** ZPOW
    return CMOD5_N

def cmod5n_inverse_gpu(sigma0_obs_cpu, phi_cpu, incidence_cpu, iterations=10):
    sigma0_obs = cupy.asarray(sigma0_obs_cpu)
    phi = cupy.asarray(phi_cpu)
    incidence = cupy.asarray(incidence_cpu)
    V = cupy.array([10.0]) * cupy.ones(sigma0_obs.shape)
    step = 10.0
    for iterno in range(iterations):
        sigma0_calc = cmod5n_forward_gpu(V, phi, incidence)
        ind = sigma0_calc - sigma0_obs > 0
        V = V + step
        V[ind] = V[ind] - 2 * step
        step = step / 2
    return cupy.asnumpy(V)
