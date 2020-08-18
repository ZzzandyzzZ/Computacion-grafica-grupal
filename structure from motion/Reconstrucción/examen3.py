import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import cv2
from camera import Camera


def reconstruct_points(p1, p2, m1, m2):
    num_points = p1.shape[1]
    res = np.ones((4, num_points))

    for i in range(num_points):
        res[:, i] = reconstruct_one_point(p1[:, i], p2[:, i], m1, m2)

    return res


def reconstruct_one_point(pt1, pt2, m1, m2):

    A = np.vstack([
        np.dot(skew(pt1), m1),
        np.dot(skew(pt2), m2)
    ])
    U, S, V = np.linalg.svd(A)
    P = np.ravel(V[-1, :4])

    return P / P[3]


def linear_triangulation(p1, p2, m1, m2):

    num_points = p1.shape[1]
    res = np.ones((4, num_points))

    for i in range(num_points):
        A = np.asarray([
            (p1[0, i] * m1[2, :] - m1[0, :]),
            (p1[1, i] * m1[2, :] - m1[1, :]),
            (p2[0, i] * m2[2, :] - m2[0, :]),
            (p2[1, i] * m2[2, :] - m2[1, :])
        ])

        _, _, V = np.linalg.svd(A)
        X = V[-1, :4]
        res[:, i] = X / X[3]

    return res


def compute_epipole(F):
    U, S, V = np.linalg.svd(F)
    e = V[-1]
    return e / e[2]


def plot_epipolar_lines(p1, p2, F, show_epipole=False):
    plt.figure()
    plt.suptitle('Epipolar lines', fontsize=16)

    plt.subplot(1, 2, 1, aspect='equal')
    plot_epipolar_line(p1, p2, F, show_epipole)
    plt.subplot(1, 2, 2, aspect='equal')

    plot_epipolar_line(p2, p1, F.T, show_epipole)


def plot_epipolar_line(p1, p2, F, show_epipole=False):

    lines = np.dot(F, p2)
    pad = np.ptp(p1, 1) * 0.01
    mins = np.min(p1, 1)
    maxes = np.max(p1, 1)

    xpts = np.linspace(mins[0] - pad[0], maxes[0] + pad[0], 100)
    for line in lines.T:
        ypts = np.asarray([(line[2] + line[0] * p) / (-line[1]) for p in xpts])
        valid_idx = ((ypts >= mins[1] - pad[1]) & (ypts <= maxes[1] + pad[1]))
        plt.plot(xpts[valid_idx], ypts[valid_idx], linewidth=1)
        plt.plot(p1[0], p1[1], 'ro')

    if show_epipole:
        epipole = compute_epipole(F)
        plt.plot(epipole[0] / epipole[2], epipole[1] / epipole[2], 'r*')


def skew(x):

    return np.array([
        [0, -x[2], x[1]],
        [x[2], 0, -x[0]],
        [-x[1], x[0], 0]
    ])


def compute_P(p2d, p3d):
    n = p2d.shape[1]
    if p3d.shape[1] != n:
        raise ValueError('Tamaños incorrectos')

    M = np.zeros((3 * n, 12 + n))
    for i in range(n):
        M[3 * i, 0:4] = p3d[:, i]
        M[3 * i + 1, 4:8] = p3d[:, i]
        M[3 * i + 2, 8:12] = p3d[:, i]
        M[3 * i:3 * i + 3, i + 12] = -p2d[:, i]

    U, S, V = np.linalg.svd(M)
    return V[-1, :12].reshape((3, 4))


def compute_P_from_fundamental(F):
 
    e = compute_epipole(F.T)  # left epipole
    Te = skew(e)
    return np.vstack((np.dot(Te, F.T).T, e)).T


def compute_P_from_essential(E):

    U, S, V = np.linalg.svd(E)


    if np.linalg.det(np.dot(U, V)) < 0:
        V = -V

 
    W = np.array([[0, -1, 0], [1, 0, 0], [0, 0, 1]])
    P2s = [np.vstack((np.dot(U, np.dot(W, V)).T, U[:, 2])).T,
          np.vstack((np.dot(U, np.dot(W, V)).T, -U[:, 2])).T,
          np.vstack((np.dot(U, np.dot(W.T, V)).T, U[:, 2])).T,
          np.vstack((np.dot(U, np.dot(W.T, V)).T, -U[:, 2])).T]

    return P2s


def correspondence_matrix(p1, p2):
    p1x, p1y = p1[:2]
    p2x, p2y = p2[:2]

    return np.array([
        p1x * p2x, p1x * p2y, p1x,
        p1y * p2x, p1y * p2y, p1y,
        p2x, p2y, np.ones(len(p1x))
    ]).T

    return np.array([
        p2x * p1x, p2x * p1y, p2x,
        p2y * p1x, p2y * p1y, p2y,
        p1x, p1y, np.ones(len(p1x))
    ]).T


def compute_image_to_image_matrix(x1, x2, compute_essential=False):

    A = correspondence_matrix(x1, x2)

    U, S, V = np.linalg.svd(A)
    F = V[-1].reshape(3, 3)

    U, S, V = np.linalg.svd(F)
    S[-1] = 0
    if compute_essential:
        S = [1, 1, 0] 
    F = np.dot(U, np.dot(np.diag(S), V))

    return F


def scale_and_translate_points(points):
    x = points[0]
    y = points[1]
    center = points.mean(axis=1)  # mean of each row
    cx = x - center[0] # center the points
    cy = y - center[1]
    dist = np.sqrt(np.power(cx, 2) + np.power(cy, 2))
    scale = np.sqrt(2) / dist.mean()
    norm3d = np.array([
        [scale, 0, -scale * center[0]],
        [0, scale, -scale * center[1]],
        [0, 0, 1]
    ])

    return np.dot(norm3d, points), norm3d


def compute_normalized_image_to_image_matrix(p1, p2, compute_essential=False):
    n = p1.shape[1]
    if p2.shape[1] != n:
        raise ValueError('Number of points do not match.')

    p1n, T1 = scale_and_translate_points(p1)
    p2n, T2 = scale_and_translate_points(p2)

    F = compute_image_to_image_matrix(p1n, p2n, compute_essential)

    F = np.dot(T1.T, np.dot(F, T2))

    return F / F[2, 2]


def compute_fundamental_normalized(p1, p2):
    return compute_normalized_image_to_image_matrix(p1, p2)


def compute_essential_normalized(p1, p2):
    return compute_normalized_image_to_image_matrix(p1, p2, compute_essential=True)


def read_matrix(path, astype=np.float64):
    with open(path, 'r') as f:
        arr = []
        for line in f:
            arr.append([(token if token != '*' else -1)
                        for token in line.strip().split()])
        return np.asarray(arr).astype(astype)


def cart2hom(arr):
    if arr.ndim == 1:
        return np.hstack([arr, 1])
    return np.asarray(np.vstack([arr, np.ones(arr.shape[1])]))


def hom2cart(arr):
    num_rows = len(arr)
    if num_rows == 1 or arr.ndim == 1:
        return arr

    return np.asarray(arr[:num_rows - 1] / arr[num_rows - 1])


def find_correspondence_points(img1, img2):
    sift = cv2.xfeatures2d.SIFT_create()

    kp1, des1 = sift.detectAndCompute(
        cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY), None)
    kp2, des2 = sift.detectAndCompute(
        cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY), None)
    FLANN_INDEX_KDTREE = 0
    index_params = dict(algorithm=FLANN_INDEX_KDTREE, trees=5)
    search_params = dict(checks=50)
    flann = cv2.FlannBasedMatcher(index_params, search_params)
    matches = flann.knnMatch(des1, des2, k=2)

    good = []
    for m, n in matches:
        if m.distance < 0.8 * n.distance:
            good.append(m)

    src_pts = np.asarray([kp1[m.queryIdx].pt for m in good])
    dst_pts = np.asarray([kp2[m.trainIdx].pt for m in good])

    retval, mask = cv2.findHomography(src_pts, dst_pts, cv2.RANSAC, 100.0)
    mask = mak.ravel()

    pts1 = src_pts[mask == 1]
    pts2 = dst_pts[mask == 1]

    return pts1.T, pts2.T



def start():
    
    img1 = cv2.imread('cup (3).jpg')
    img2 = cv2.imread('cup (6).jpg')
    pts1, pts2 = find_correspondence_points(img1, img2)
    points1 = cart2hom(pts1)
    points2 = cart2hom(pts2)

    fig, ax = plt.subplots(1, 2)
    ax[0].autoscale_view('tight')
    ax[0].imshow(cv2.cvtColor(img1, cv2.COLOR_BGR2RGB))
    ax[0].plot(points1[0], points1[1], 'r.')
    ax[1].autoscale_view('tight')
    ax[1].imshow(cv2.cvtColor(img2, cv2.COLOR_BGR2RGB))
    ax[1].plot(points2[0], points2[1], 'r.')
    fig.show()

    height, width, ch = img1.shape
    intrinsic = np.array([ 
        [2000, 0, width / 2],
        [0, 2000, height / 2],
        [0, 0, 1]])

    return points1, points2, intrinsic

def writeTxt(name,points):
    print("TAMAÑO",len(points))
    f=open(name,"w")
    for i in range(len(points[0])):
        f.write(str(points[0][i])+","+str(points[1][i])+","+str(points[2][i])+","+"\n")
    f.close()

points1, points2, intrinsic = start()

points1n = np.dot(np.linalg.inv(intrinsic), points1)
points2n = np.dot(np.linalg.inv(intrinsic), points2)
E = compute_essential_normalized(points1n, points2n)
print('Computed essential matrix:', (-E / E[0][1]))

s
P1 = np.array([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0]])
P2s = compute_P_from_essential(E)

ind = -1
for i, P2 in enumerate(P2s):
    d1 = reconstruct_one_point(
        points1n[:, 0], points2n[:, 0], P1, P2)

    P2_homogenous = np.linalg.inv(np.vstack([P2, [0, 0, 0, 1]]))
    d2 = np.dot(P2_homogenous[:3, :4], d1)

    if d1[2] > 0 and d2[2] > 0:
        ind = i

P2 = np.linalg.inv(np.vstack([P2s[ind], [0, 0, 0, 1]]))[:3, :4]

tripoints3d = linear_triangulation(points1n, points2n, P1, P2)

fig = plt.figure()
fig.suptitle('3D reconstructed', fontsize=16)
ax = fig.gca(projection='3d')
ax.plot(tripoints3d[0], tripoints3d[1], tripoints3d[2], 'b.')
ax.set_xlabel('x axis')
ax.set_ylabel('y axis')
ax.set_zlabel('z axis')
ax.view_init(elev=135, azim=90)
plt.show()


writeTxt("points.txt",tripoints3d)